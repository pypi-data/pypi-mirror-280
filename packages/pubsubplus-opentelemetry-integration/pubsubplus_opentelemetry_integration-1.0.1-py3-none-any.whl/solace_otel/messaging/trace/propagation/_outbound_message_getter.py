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
This module contains the OutboundMessageGetter class, which can be used in tandem with the
:py:class`OutboundMessageCarrier<solace_otel.messaging.trace.propagation.OutboundMessageCarrier>`
class to retrieve context data from a Solace message.
"""

import logging.config
from typing import Union, List
from opentelemetry.propagators import textmap


from solace_otel.messaging.trace.propagation._logging import SolaceLoggingAdapter, \
                                                             SOLACE_OPEN_TELEMETRY_LOGGER
from solace_otel.messaging.trace.propagation._common import TRACE_PARENT_KEY, \
                                                            TRACE_STATE_KEY, \
                                                            BAGGAGE_KEY

from solace_otel.messaging.trace.propagation._outbound_message_carrier import OutboundMessageCarrier

logger = logging.getLogger(SOLACE_OPEN_TELEMETRY_LOGGER)

class OutboundMessageGetter(textmap.Getter):
    """
    This class implements a Getter that enables extracting propagated fields from a carrier.
    """

    def __init__(self):
        super().__init__()
        self._id_info = "[OutboundMessageGetter ID Info: {str(hex(id(self)))}]"
        self._adapter = SolaceLoggingAdapter(logger, {'id_info': self._id_info})

    def get(self, carrier: 'OutboundMessageCarrier', key: str) -> Union[None, List[str]]:
        """
        Function that can retrieve zero or more values from the carrier. In the case that the value does not exist,
        returns None.

        Args:
            carrier(OutboundMessageCarrier): A Solace message carrier object which can contain values that are used
                to construct a Context.
            key(str): The key of a field in carrier.

        Returns:
            Union[None, List[str]]: First value of the propagation key, or None if the key doesn't exist.
        """
        if not isinstance(carrier, OutboundMessageCarrier):
            self._adapter.warning("The applicaiton attempted to set a key/value pair on a " \
                                  "non-OutboundMessageCarrier object.")
            return None
        return [carrier.get(key)]

    def keys(self, carrier: 'OutboundMessageCarrier') -> List[str]:
        """
        Function that can retrieve 'traceparent', 'tracestate', 'baggage', when they are supported by the underlying
        message.

        Args:
            carrier(OutboundMessageCarrier): A Solace message carrier object which can contain values that are used to
                construct a Context.

        Returns:
            List[str]: The values to the keys 'traceparent', 'tracestate', and 'baggage'.
        """
        return [TRACE_PARENT_KEY, TRACE_STATE_KEY, BAGGAGE_KEY]
