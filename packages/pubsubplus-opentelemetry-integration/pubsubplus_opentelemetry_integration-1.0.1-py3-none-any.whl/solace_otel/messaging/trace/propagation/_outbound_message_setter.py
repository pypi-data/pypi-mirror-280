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
This module contains the OutboundMessageSetter class which can be used in tandem with the
:py:class`OutboundMessageCarrier<solace_otel.messaging.trace.propagation.OutboundMessageCarrier>`
class to configure context data on a Solace message.
"""

import logging.config
from opentelemetry.propagators import textmap

from solace_otel.messaging.trace.propagation._logging import SolaceLoggingAdapter, \
                                                             SOLACE_OPEN_TELEMETRY_LOGGER

from solace_otel.messaging.trace.propagation._outbound_message_carrier import OutboundMessageCarrier

logger = logging.getLogger(SOLACE_OPEN_TELEMETRY_LOGGER)

class OutboundMessageSetter(textmap.Setter):
    """
    This class implements a Setter that enables injecting propagated fields into a Solace message carrier.
    """

    def __init__(self):
        super().__init__()
        self._id_info = f"[OutboundMessageSetter ID Info: {str(hex(id(self)))}]"
        self._adapter = SolaceLoggingAdapter(logger, {'id_info': self._id_info})

    def set(self, carrier: 'OutboundMessageCarrier', key: str, value: str):
        """
        Function that can set a value into a Solace message carrier

        Args:
            carrier: A Solace message carrier which contains values that are used to construt a Context.
            key: The key of a field in carrier.
            value: The value for a field in carrier.
        """

        if not isinstance(carrier, OutboundMessageCarrier):
            self._adapter.warning("The application attempted to set a key/value pair on a " \
                                  "non-OutboundMessageCarrier object.")
            return

        carrier.set(key, value)
