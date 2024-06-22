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
This module contains the OutboundMessageCarrier class, which wraps an OutboundMessage object. This class can be used
in tandem with the :py:class:`OutboundMessageSetter<solace_otel.messaging.trace.propagation.OutboundMessageSetter>`
class or :py:class:`OutboundMessageGetter<solace_otel.mesasging.trace.propagation.OutboundMessageGetter>` class to
retrieve or configure context data on a Solace message, respectively.
"""
from typing import Any
import logging.config

from solace.messaging.publisher.outbound_message import OutboundMessage
from solace.messaging.errors.pubsubplus_client_error import PubSubPlusClientError

from solace_otel.messaging.trace.propagation._logging import SolaceLoggingAdapter, \
                                                             SOLACE_OPEN_TELEMETRY_LOGGER
from solace_otel.messaging.trace.propagation._common import FAILED_TO_SET_KEY, \
                                                            REASON_KEY_INVALID, \
                                                            TRACE_PARENT_KEY, \
                                                            TRACE_STATE_KEY, \
                                                            BAGGAGE_KEY, \
                                                            REASON_VALUE_INVALID, \
                                                            REASON_UNKNOWN_KEY, \
                                                            Parser, \
                                                            get

logger = logging.getLogger(SOLACE_OPEN_TELEMETRY_LOGGER)

class OutboundMessageCarrier:
    """
    This class represents a Otel carrier and is a Solace message wrapper and enables injection of propagated fields
    into Solace message. It is used in conjunction with OutboundMessageSetter.
    """
    def __init__(self, outbound_message: OutboundMessage):
        self._message = outbound_message
        self._id_info = f"[OutboundMessageCarrier ID Info: {str(hex(id(self)))}]"
        self._adapter = SolaceLoggingAdapter(logger, {'id_info': self._id_info})

    def get(self, key) -> Any:
        """
        Retrieves the value of a given key.

        Args:
            key(str): The key to use for value retrieval.

        Returns:
            Any: The value associated with the given key
        """
        return get(self, key, self._adapter)


    def set(self, key: str, value: str):  # pylint: disable=too-many-branches,too-many-statements,too-many-return-statements
        """
        Sets the given key-value pair in the carrier.

        Args:
            key(str): The key to use for indexing.
            value(str): The value to associate with the given key.
        """

        if key is None \
            or key == "" \
            or str.isspace(key):
            self._adapter.warning(f"{FAILED_TO_SET_KEY} {REASON_KEY_INVALID}.")
            return
        if key == TRACE_PARENT_KEY:
            # We need to check if the creation ctx exists because it must not be overwritten,
            # And because it must be set before the transport ctx is set
            try:
                creation_trace_id, creation_span_id, creation_sampled_flag, creation_trace_state = \
                    self._message.get_creation_trace_context()
            except PubSubPlusClientError as error:
                self._adapter.warning(f"The following error was encountered while checking the existence of the " \
                                      f"creation context as a part of setting the trace parent: {error}.")
                return
            if Parser.context_is_not_found(creation_trace_id, creation_span_id,
                                            creation_sampled_flag, creation_trace_state):
                if self._adapter.isEnabledFor(logging.DEBUG):
                    self._adapter.debug("Creation context was not previously set, setting now.")
                # Creation context has not been set yet
                try:
                    creation_trace_id, creation_span_id, creation_sampled_flag = \
                        Parser.get_context_from_trace_parent(value)
                except Parser.ParserError as error:
                    # If we are unable to parse the context, the application gave a bad input
                    self._adapter.warning(f"Failed to set trace parent because the passed value could not be " \
                                          f"parsed with error: {error}.")
                    return
                try:
                    self._message.set_creation_trace_context(creation_trace_id, creation_span_id,
                                                             creation_sampled_flag, "")
                except PubSubPlusClientError as error:
                    self._adapter.warning(f"Failed to set trace parent because the following error was " \
                                          f"encountered: {error}.")
                    return
                # If no error was raised during the operation, we can assume it was successful.
                if self._adapter.isEnabledFor(logging.DEBUG):
                    self._adapter.debug("Successfully set trace parent on creation context.")
                return

            # Creation context has been set already, so we set on the transport context instead.
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Creation context was already set, attempting to set trace parent on " \
                                    "transport context.")
            try:
                transport_trace_id, transport_span_id, transport_sampled_flag = \
                    Parser.get_context_from_trace_parent(value)
            except Parser.ParserError as error:
                # If we are unable to parse the context, the application gave a bad input
                self._adapter.warning(f"Failed to set trace parent because the passed value could not be parsed " \
                                      f"with error: {error}")
                return
            try:
                self._message.set_transport_trace_context(transport_trace_id, transport_span_id,
                                                          transport_sampled_flag, "")
            except PubSubPlusClientError as error:
                self._adapter.warning(f"Failed to set trace parent because the following error was encountered: " \
                                      f"{error}.")
            # If no exception was raised, we can assume the operation was successful
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Successfully set trace parent on transport context.")
        elif key == TRACE_STATE_KEY:
            if not Parser.is_trace_state_valid(value):
                self._adapter.warning(f"{FAILED_TO_SET_KEY} {REASON_VALUE_INVALID}.")
                return
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Attempting to set '%s' as trace state.", value)
            # We need the trace parent info to be set before we can set the trace state, so if the trace parent
            # query fails on a context, the trace state cannot be set on that context. If the trace parent query
            # fails on the creation context, then both the creation context and transport context have not been set
            # and we are unable to set the trace state,
            try:
                creation_trace_id, creation_span_id, creation_sampled_flag, creation_trace_state = \
                    self._message.get_creation_trace_context()
            except PubSubPlusClientError:
                self._adapter.warning("Failed to check creation context as a part of trying to set the trace state.")
                return
            if Parser.context_is_not_found(creation_trace_id, creation_span_id, creation_sampled_flag,
                                            creation_trace_state):
                self._adapter.info("Did not find creation context. Unable to set trace state on context that does " \
                                   "not exist.")
                return
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Successfully retrieved creation context while trying to set trace state.")
            try:
                transport_trace_id, transport_span_id, transport_sampled_flag, transport_trace_state = \
                    self._message.get_transport_trace_context()
            except PubSubPlusClientError as error:
                self._adapter.warning(f"Failed to check transport context while trying to set trace state with " \
                                      f"error: {error}.")
                return
            if Parser.context_is_not_found(transport_trace_id, transport_span_id, transport_sampled_flag,
                                            transport_trace_state):
                if self._adapter.isEnabledFor(logging.DEBUG):
                    self._adapter.debug("Transport context was not found, attempting to set trace state on " \
                                        "creation context.")
                # If the transport context does not exist, then set the trace state on the creation context.
                try:
                    self._message.set_creation_trace_context(creation_trace_id,
                                                             creation_span_id,
                                                             creation_sampled_flag,
                                                             value)
                    # If no exception was raised then we can assume the operation was successful
                    if self._adapter.isEnabledFor(logging.DEBUG):
                        self._adapter.debug("The trace state was set on the creation context without an exception " \
                                            "being raised.")
                    return
                except PubSubPlusClientError as error:
                    self._adapter.warning(f"Failed to set trace state on creation context because the following " \
                                          f"error was encountered: {error}.")
                    return

            # If the transport context exists, then we set the trace state on that context
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Successfully retrieved transport context while trying to set trace state.")
            try:
                self._message.set_transport_trace_context(transport_trace_id,
                                                          transport_span_id,
                                                          transport_sampled_flag,
                                                          value)
                # If no exception was raised, we can assume the operation was successful
                if self._adapter.isEnabledFor(logging.DEBUG):
                    self._adapter.debug("The trace state was set on the transport context without an exception " \
                                        "being raised.")
                return
            except PubSubPlusClientError:
                self._adapter.warning(f"Failed to set the trace state on the transport context because the " \
                                      f"following error was encountered: {error}.")

        elif key == BAGGAGE_KEY:
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Attempting to set baggage on OutboundMessageCarrier.")
                self._adapter.debug("Validating passed baggage key/value pairs '{value}'.")
            if Parser.is_empty(value):
                self._adapter.warning(f"{FAILED_TO_SET_KEY} {REASON_KEY_INVALID}.")
                return
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Passed baggage key/value pairs '{value}' were validated.")
            try:
                self._message.set_baggage(value)
            except PubSubPlusClientError as error:
                self._adapter.warning(f"Failed to set baggage because the following error was encountered: {error}.")
                return
            if self._adapter.isEnabledFor(logging.DEBUG):
                self._adapter.debug("Successfully set baggage.")
        else:
            self._adapter.warning(f"{FAILED_TO_SET_KEY} {REASON_UNKNOWN_KEY}")
            return
