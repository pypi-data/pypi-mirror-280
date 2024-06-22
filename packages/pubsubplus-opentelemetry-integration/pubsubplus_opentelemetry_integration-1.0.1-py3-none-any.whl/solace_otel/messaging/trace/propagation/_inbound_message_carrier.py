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
This module contains the InboundMessageCarrier class. This class wraps an InboundMessage object and can be used in
tandem with the :py:class:`InboundMessageGetter<solace_otel.messaging.trace.propagation.InboundMessageGetter>' class
to retrieve context data from a received Solace message.
"""

import logging
from typing import Any

from solace.messaging.receiver.inbound_message import InboundMessage

from solace_otel.messaging.trace.propagation._logging import SolaceLoggingAdapter, \
                                                             SOLACE_OPEN_TELEMETRY_LOGGER
from solace_otel.messaging.trace.propagation._common import get

logger = logging.getLogger(SOLACE_OPEN_TELEMETRY_LOGGER)

class InboundMessageCarrier:
    """
    This class represents a Otel carrier and is a Solace message wrapper and enables extracting propagated fields
    from Solace message. It is used in conjunction with InboundMessageGetter.
    """
    def __init__(self, inbound_message: InboundMessage):
        self._message = inbound_message
        self._id_info = f"[InboundMessageCarrier ID Info: {str(hex(id(self)))}]"
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
