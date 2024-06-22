# pubsubplus-opentelemetry-integration
#
# Copyright 2024 Solace Corporation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains useful tools for processing context data, and is intended for internal use only.
"""
import logging.config
import re
from typing import Union, Tuple

from solace.messaging.errors.pubsubplus_client_error import PubSubPlusClientError

from solace_otel.messaging.trace.propagation._logging import SOLACE_OPEN_TELEMETRY_LOGGER

logger = logging.getLogger(SOLACE_OPEN_TELEMETRY_LOGGER)

TRACE_PARENT_KEY = "traceparent"
TRACE_STATE_KEY = "tracestate"
BAGGAGE_KEY = "baggage"
FAILED_TO_SET_KEY = "Failed to set key"
FAILED_TO_GET_KEY = "Failed to get key"
REASON_KEY_INVALID = "because the passed key was None, empty, or only whitespace"
REASON_VALUE_INVALID = "because the passed value was only witespace"
REASON_UNKNOWN_KEY = "because the passed key was not recognised"
REASON_PARSING_FAILED = "because the value could not be parsed"

class Parser:
    """
    This class contains the tools necessary for parsing various context data, including trace parent, trace state, and
    baggage.
    """
    _TRACE_STATE_DELIMITER = ","
    _KEY_VALUE_DELIMITER = "="
    _TRACE_PARENT_KEY_DELIMITER = "-"
    _STRING_ENCODING = "utf-8"
    _VERSION = "00"
    _MAX_MEMBERS = 32
    _SPAN_ID_LENGTH = 16
    _TRACE_ID_LENGTH = 32
    _TRACE_ID_NOT_FOUND_VALUE = bytes(b'\x00' * 16)
    _SPAN_ID_NOT_FOUND_VALUE = bytes(b'\x00' * 8)
    _PARSING_ERROR = "An error occurred while parsing the passed values"

    class ParserError(Exception):
        """
        This is the base error class to handle general parsing errors.
        """

    @staticmethod
    def concatenate_trace_states(creation_trace_state: str, transport_trace_state: str) -> str:
        """
        This function concatenates the creation trace state and transport trace state.

        Args:
            creation_trace state(str): The creation trace state to be concatenated.
            transport_trace_state(str): The transport trace state to be concatenated.

        Returns:
            str: The concatenated trace state.
        """
        # This function is used to isolate the Parser._TRACE_STATE_DELIMITER and parsing logic from the
        # InboundMessageSetter.
        return transport_trace_state + Parser._TRACE_STATE_DELIMITER + creation_trace_state

    @staticmethod
    def context_is_not_found(trace_id: Union[None, bytearray], span_id: Union[None, bytearray],
                             sampled_flag: Union[bool, None], trace_state: Union[str, None]) -> bool:
        """
        This function checks that the passed context components indicate that the context was found/previously set.

        Args:
            trace_id(Union[bytearray, None]): The trace ID of the context.
            span_id(Union[bytearray, None]): The span ID of the context.
            sampled_flag(Union[bool, None]): The sampled flag of the context.
            trace_state(Union[bool, None]): The trace state of the context.

        Returns:
            bool: True if the trace_id, span_id, or sampled_flag are None, False otherwise.

        Raises:
            ParserError: If an error was encountered during parsing.
        """
        # According to PSPPython API, trace state can be returned as None if it was not set, since it is not a
        # mandatory context field, so there is no reason to check it. It is included in the interface of this
        # function for the sake of future-compatibility
        if trace_id is None \
            or trace_id == Parser._TRACE_ID_NOT_FOUND_VALUE \
            or span_id is None \
            or span_id == Parser._SPAN_ID_NOT_FOUND_VALUE \
            or sampled_flag is None:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug("Context with trace id '%s', span id '%s', sampled_flag '%s', and " \
                             "trace state '%s' was not found.", trace_id, span_id, sampled_flag, trace_state)
            return True
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("Context with trace id '%s', span id '%s', sampled_flag '%s', and " \
                         "trace state '%s' was found.", trace_id, span_id, sampled_flag, trace_state)
        return False


    @staticmethod
    def is_empty(value: str):
        """
        This function evaluates if the passed string value is None, an empty string, or whitespace.

        Args:
            value(str): The value to evaluate.

        Returns:
            bool: True if the value is considered empty, False otherwise.
        """
        if value is None \
            or not isinstance(value, str) \
            or value == "" \
            or str.isspace(value):
            # value is empty
            return True
        return False

    @staticmethod
    def get_trace_parent_from_context(context_id: bytearray, span_id: bytearray, sampled_flag: bool) -> str:
        """
        This function converts trace context properties to a trace parent string.

        Args:
            context_id(bytearray): The context ID to convert.
            span_id(bytearray): The span ID to convert.
            sampled_flag(bool): The sampled flag to convert.

        Returns:
            str: The trace parent which resulted from the context property conversion.

        Raises:
            ParserError: If an error was encountered during parsing.
        """
        if sampled_flag:
            sampled_flag_as_string = "01"
        else:
            sampled_flag_as_string = "00"

        if context_id is None \
            or not isinstance(context_id, bytearray) \
            or span_id is None \
            or not isinstance(span_id, bytearray):
            raise Parser.ParserError(f"{Parser._PARSING_ERROR}.")

        trace_id_as_string = Parser.get_string_from_bytearray_without_delimiter(context_id)
        span_id_as_string = Parser.get_string_from_bytearray_without_delimiter(span_id)
        if Parser.is_empty(trace_id_as_string) \
            or Parser.is_empty(span_id_as_string) \
            or sampled_flag is None:
            raise Parser.ParserError(f"{Parser._PARSING_ERROR}.")

        trace_parent = \
            Parser._VERSION \
            + Parser._TRACE_PARENT_KEY_DELIMITER \
            + trace_id_as_string \
            + Parser._TRACE_PARENT_KEY_DELIMITER \
            + span_id_as_string \
            + Parser._TRACE_PARENT_KEY_DELIMITER \
            + sampled_flag_as_string
        return trace_parent

    @staticmethod
    def get_string_from_bytearray_without_delimiter(byte_array: bytearray, delimiter: str=None) -> str:
        """
        This function returns the given bytearray in string format after removing the given delimiter from that string.
        If no delimiter is passed, it is assumed that the passed byearray is a trace parent, and the trace parent
        delimiter, as given by Parser._TRACE_PARENT_KEY_DELIMITER, is removed from the formatted string.

        Args:
            byte_array: The bytearray to represent as a string.
            delmiter: The string delimiter to be removed from the string representation of the given byearray.

        Returns:
            str: The string representation of the given bytearray after the delimited has been removed.
        """
        if delimiter is None:
            delimiter = Parser._TRACE_PARENT_KEY_DELIMITER
        string = Parser.get_string_from_bytearray(byte_array)
        string.replace(delimiter, "")
        return string

    @staticmethod
    def get_string_from_bytearray(byte_array: bytearray) -> str:
        """
        This function returns the given bytearray in string format.

        Args:
            byte_array: The bytearray to represent as a string.

        Returns:
            str: The string format of the given byte array.
        """
        string = byte_array.hex()
        return string

    @staticmethod
    def get_context_from_trace_parent(trace_parent: str) -> Tuple[bytes, bytes, bool]:
        """
        This function converts a string-form trace parent into a tuple of context id, span id, and sampled flag.

        Args:
            trace_parent(str): The trace parent string to convert.

        Returns:
            Tuple[bytes, bytes, bool]: In order, the converted context id, span id, and sampled flag.
        """

        # NOTE: The length of the trace parent after being separated by its delimiter is 4, and we extract information
        # starting at index 1. This is because the format of a trace parent string is "VERSION-TRACE_ID-SPAN_ID-FLAGS".
        # An example of a valid value following this format would be
        # "00-75e792db89dec2cf3b3333a2f71869e4-982f925c36fb8a1c-01". The first entry in the trace parent is the version
        # number, but as of 2024-01-16, the version is fixed at "00", so this does not need to be parsed. This may need
        # to be revisited in the future if additional versions become supported.
        #
        # TLDR; dw, this function is supposed to start looking at index 1 instead of index 0.

        if Parser.is_empty(trace_parent):
            raise Parser.ParserError(f"{Parser._PARSING_ERROR}")
        trace_parent_as_list = re.split(Parser._TRACE_PARENT_KEY_DELIMITER, trace_parent)
        if len(trace_parent_as_list) != 4:
            raise Parser.ParserError(f"{Parser._PARSING_ERROR}")
        context_id_as_bytes = bytes.fromhex(trace_parent_as_list[1])
        span_id_as_bytes = bytes.fromhex(trace_parent_as_list[2])
        if trace_parent_as_list[3] == "00":
            sampled_flag = False
        else:
            sampled_flag = True
        return context_id_as_bytes, span_id_as_bytes, sampled_flag

    @staticmethod
    def is_trace_state_valid(trace_state: str):
        """
        This function validates a trace state. The criteria for a valid trace state are as follows:
            * not 'empty', see Parser.is_empty() for details
            * the number of entries in the trace state does not exceed the maximum, see Parser._MAX_MEMBERS for
              details
            * each entry in the trace state follows the required format of 'key=value'
        A valid trace state looks like the following:
        "key1=value1,key2=value2,key3=value3"
        NOTE: Each trace state entry is delimited by a comma.
        NOTE: Each trace state entry is a key/value pair delimited by an equals sign.

        Args:
            trace_state(str): The trace state to validate.

        Returns:
            bool: True if the passed trace state is valid, False otherwise.
        """

        if trace_state is None \
            or not isinstance(trace_state, str) \
            or str.isspace(trace_state):
            return False
        if trace_state == "":
            return True

        trace_state_as_list = re.split(Parser._TRACE_STATE_DELIMITER, trace_state)
        if len(trace_state_as_list) > Parser._MAX_MEMBERS:
            return False
        trace_state_builder = {}
        for member in trace_state_as_list:
            if member.find(Parser._KEY_VALUE_DELIMITER) == -1:
                return False
            member_as_list = re.split(Parser._KEY_VALUE_DELIMITER, member)
            key = member_as_list[0]
            value = member_as_list[1]
            trace_state_builder[key] = value
        if len(trace_state_builder) != len(trace_state_as_list):
            return False
        # If we got past all the checks, the trace state is valid
        return True

    @staticmethod
    def convert_dict_to_trace_state(trace_state_dict: dict) -> str:
        """
        This function converts a dictionary of key/value pairs into a delimited string according to the
        proper format.

        Args:
            trace_state_dict(dict): The dictionary to convert.

        Returns:
            str: The converted data as a delimted and formatted string.
        """
        if not isinstance(trace_state_dict, dict):
            raise Parser.ParserError(f"{Parser._PARSING_ERROR}.")

        trace_state_as_string = ""
        for key, value in trace_state_dict.items():
            trace_state_as_string += key
            trace_state_as_string += Parser._KEY_VALUE_DELIMITER
            trace_state_as_string += value
            trace_state_as_string += Parser._TRACE_STATE_DELIMITER
        return trace_state_as_string

def get(carrier, key, adapter: 'SolaceLoggingAdapter') -> 'typing.Any':  # pylint: disable=too-many-locals,too-many-return-statements,too-many-branches,too-many-statements,too-many-nested-blocks
    """
    This function retrieves the value associated with the given key, from the given carrier.

    Args:
        carrier(Union[InboundMessageCarrier, OutboundMessageCarrier]): The carrier to examine.
        key(str): The key to use during retrieval.
        adapter(SolaceLoggingAdapter): The adapter used to log imporant events.

    Returns:
        Any: The value associated with the given key.
    """
    # The architecture says that Any type should be returned, but for consistency we'll just return the same type as
    # the other returns, and we'll return a consistent default value as well.
    default_return_value = ""
    # If key is empty, log warning and return since we can't retrieve from an empty key.
    # An empty key is considered None, a non-string, or an empty string.
    if key is None or not isinstance(key, str) or key == "":
        if adapter.isEnabledFor(logging.WARNING):
            adapter.warning(f"{FAILED_TO_GET_KEY} {REASON_KEY_INVALID}")
        return default_return_value
    if key == TRACE_PARENT_KEY:  # pylint: disable=too-many-nested-blocks
        try:
            transport_trace_id, transport_span_id, transport_sampled_flag, transport_trace_state = \
                carrier._message.get_transport_trace_context()
        except PubSubPlusClientError as error:
            adapter.warning(f"An error was encountered while trying to retrieve the transport context as a part of " \
                            f"retrieving the trace parent: {error}")
            return default_return_value
        try:
            if Parser.context_is_not_found(transport_trace_id, transport_span_id,
                                            transport_sampled_flag, transport_trace_state):
                if adapter.isEnabledFor(logging.DEBUG):
                    adapter.debug("Did not find transport context when trying to retrieve trace parent.")
                # Transport context was empty, so we try creation context next
                try:
                    creation_trace_id, creation_span_id, creation_sampled_flag, creation_trace_state = \
                        carrier._message.get_creation_trace_context()
                except PubSubPlusClientError as error:
                    adapter.warning(f"An error was encountered while trying to retrieve the creation context as a" \
                                    f"part of retrieving the trace parent: {error}.")
                    return default_return_value
                try:
                    if Parser.context_is_not_found(creation_trace_id, creation_span_id,
                                                    creation_sampled_flag, creation_trace_state):
                        adapter.info("Failed to retrieve trace parent.")
                        if adapter.isEnabledFor(logging.DEBUG):
                            adapter.debug("Did not find creation context when trying to retrieve trace parent.")
                        # At this point, neither the creation nor transport contexts are found, so can return
                        return default_return_value
                    try:
                        trace_parent = Parser.get_trace_parent_from_context(creation_trace_id,
                                                                             creation_span_id,
                                                                             creation_sampled_flag)
                    except Parser.ParserError as error:
                        adapter.info("Failed to retrieve trace parent")
                        if adapter.isEnabledFor(logging.DEBUG):
                            adapter.debug("Failed to retrieve trace parent with error '%s'", error)
                        return default_return_value
                    if adapter.isEnabledFor(logging.DEBUG):
                        adapter.debug("Successfully retrieved trace parent '%s' from creation context.", trace_parent)
                    return trace_parent
                except Parser.ParserError as error:
                    adapter.info("Failed to retrieve trace parent")
                    if adapter.isEnabledFor(logging.DEBUG):
                        adapter.debug("Failed to retrieve trace parent with error '%s'", error)
                    return default_return_value

            else:
                if adapter.isEnabledFor(logging.DEBUG):
                    adapter.debug("Found transport context while trying to retrieve trace parent")
                try:
                    trace_parent = Parser.get_trace_parent_from_context(transport_trace_id,
                                                                         transport_span_id,
                                                                         transport_sampled_flag)
                except Parser.ParserError as error:
                    adapter.info("Failed to retrieve trace parent.")
                    if adapter.isEnabledFor(logging.DEBUG):
                        adapter.debug("Failed to retrieve trace parent with error '%s'", error)
                    return default_return_value
                if adapter.isEnabledFor(logging.DEBUG):
                    adapter.debug("Successfully retrieved trace parent from transport context.")
                return trace_parent
        except Parser.ParserError as error:
            adapter.info("Failed to retrieve trace parent")
            if adapter.isEnabledFor(logging.DEBUG):
                adapter.debug("Failed to retrieve trace parent with error '%s'", error)
            return default_return_value
    elif key == TRACE_STATE_KEY:
        return_value = default_return_value
        try:
            creation_trace_id, creation_span_id, creation_sampled_flag, creation_trace_state = \
                carrier._message.get_creation_trace_context()
        except PubSubPlusClientError as error:
            adapter.warning(f"Failed to retrieve creation context as a part of retrieving the trace state, with " \
                           f"error {error}.")
            return return_value
        try:
            if Parser.context_is_not_found(creation_trace_id, creation_span_id, creation_sampled_flag,
                                            creation_trace_state):
                # If we get NOT_FOUND, it's because the creation context hasn't been set yet. If so,
                # we can't retrieve a trace state from a creation context that doesn't exist. Also, no
                # transport context should exist without the creation context, so we can assume in this case
                # that there is no transport context either and return immediately
                adapter.info("Did not find creation context as a part of trying to retrieve trace state, so trace " \
                             "state cannot be retrieved.")
                return return_value
        except Parser.ParserError as error:
            adapter.info("Failed to retrieve trace state")
            if adapter.isEnabledFor(logging.DEBUG):
                adapter.debug("Failed to retrieve trace state from creation context due to error '%s'", error)
            return default_return_value
        if creation_trace_state is None:
            creation_trace_state = ""
        if not Parser.is_trace_state_valid(creation_trace_state):
            # Trace state is invalid, so operation fails early
            adapter.info("Failed to retrieve trace state.")
            if adapter.isEnabledFor(logging.DEBUG):
                adapter.debug("Failed to retrieve trace state because '%s' could not be parsed.", creation_trace_state)
            return return_value
        return_value += creation_trace_state

        try:
            transport_trace_id, transport_span_id, transport_sampled_flag, transport_trace_state = \
                carrier._message.get_transport_trace_context()
        except PubSubPlusClientError as error:
            adapter.warning(f"Failed to retrieve transport context as a part of retrieving the trace state, with " \
                           f"error {error}.")
            # Even though we previously found the creation context trace state, we return the default value here since
            # there was an error. We don't want to return the creation context trace state because that might lead the
            # application to believe that the operation was successful and that there simply wasn't a transport
            # context trace state.
            return default_return_value
        try:
            if Parser.context_is_not_found(transport_trace_id, transport_span_id, transport_sampled_flag,
                                            transport_trace_state):
                if adapter.isEnabledFor(logging.DEBUG):
                    adapter.debug("Did not find transport context when trying to retrieve trace state")
                # We can return whatever has been formatted because if either of the IDs is not found, then the
                # transport context was not set, so there is no transport trace state to retrieve, and whatever was
                # already formatted is the only information available.
                return return_value
        except Parser.ParserError as error:
            adapter.info("Failed to retrieve trace state from transport context.")
            if adapter.isEnabledFor(logging.DEBUG):
                adapter.debug("Failed to retrieve trace state from transport context due to error '%s'", error)
            return default_return_value
        if transport_trace_state is None:
            transport_trace_state = ""
        if not Parser.is_trace_state_valid(transport_trace_state):
            adapter.info("Failed to retrieve trace state")
            if adapter.isEnabledFor(logging.DEBUG):
                adapter.debug("'%s' '%s' '%s'", FAILED_TO_GET_KEY, TRACE_STATE_KEY, REASON_PARSING_FAILED)
            # If parsing failed, we can't add to the trace state, so just return
            return default_return_value
        # If the transport trace state is valid, prepend it to the return value
        if return_value != default_return_value and transport_trace_state != "":
            return Parser.concatenate_trace_states(return_value, transport_trace_state)
        return return_value + transport_trace_state

    elif key == BAGGAGE_KEY:
        try:
            baggage = carrier._message.get_baggage()
        except PubSubPlusClientError as error:
            adapter.warning(f"An error was encountered while trying to retrieve baggage from the carrier: {error}")
            return default_return_value
        if baggage is None:
            if adapter.isEnabledFor(logging.DEBUG):
                adapter.debug("Did not find baggage in carrier")
            return default_return_value
        if adapter.isEnabledFor(logging.DEBUG):
            adapter.debug("Successfully found baggage '%s' in carrier.", baggage)
        return baggage
    else:
        adapter.warning(f"{FAILED_TO_GET_KEY} {key} {REASON_UNKNOWN_KEY}")
        return default_return_value
