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
This module enables more ergonomic importing of objects required by the application.
"""

# The following imports allow the application to import these classes directly through the following:
# `from solace_otel.messaging.trace.propagation import OutboundMessageCarrier`
# instead of needing to import it using the full path as follows:
# `from solace_otel.messaging.trace.propagation._outbound_message_carrier import OutboundMessageCarrier`
# The following imports also allow us to add them to the __all__ module attribute, which is explained later.
from ._logging import SOLACE_OPEN_TELEMETRY_LOGGER, \
                      set_solace_open_telemetry_log_level
from ._outbound_message_carrier import OutboundMessageCarrier
from ._inbound_message_carrier import InboundMessageCarrier
from ._outbound_message_setter import OutboundMessageSetter
from ._inbound_message_getter import InboundMessageGetter
from ._outbound_message_getter import OutboundMessageGetter

# This module attribute allows the application to glob import all of the listed classes through the following:
# `from solace_otel.messaging.trace.propagation import *`
# instead of needing to import each of them directly.
__all__ = ["OutboundMessageCarrier",
           "InboundMessageCarrier",
           "OutboundMessageSetter",
           "InboundMessageGetter",
           "OutboundMessageGetter",
           "set_solace_open_telemetry_log_level",
           "SOLACE_OPEN_TELEMETRY_LOGGER"]
