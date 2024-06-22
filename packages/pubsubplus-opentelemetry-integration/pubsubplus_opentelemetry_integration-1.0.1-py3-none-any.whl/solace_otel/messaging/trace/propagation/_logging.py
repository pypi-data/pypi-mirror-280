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
This module contains all logging tooling, required for either internal package objects to log important events, or for
the application to configure the package logging.
"""

import logging.config

SOLACE_OPEN_TELEMETRY_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'solace-open-telemetry-default-formatter': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: [%(filename)s:%(lineno)s] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'NOTSET',
            'formatter': 'solace-open-telemetry-default-formatter',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'solace_otel.messaging.trace.propagation': {
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}

logging.config.dictConfig(SOLACE_OPEN_TELEMETRY_LOGGING_CONFIG)
SOLACE_OPEN_TELEMETRY_LOGGER = "solace_otel.messaging.trace.propagation"

def set_solace_open_telemetry_log_level(log_level: str, logger: str=None):
    """
    This function provides an interface through which the application can configure the log level for a certain logger.
    If no logger is given, all loggers will be configured for the given log level.

    Args:
        logger(str): The logger to configure, defaults to None. If None is passed, all loggers are updated to the
            given log level.
        log_level(str): The log level to configure the given logger(s) to.
            Options are 'ERROR', 'WARNING', 'INFO', and 'DEBUG'.
    """
    loggers = SOLACE_OPEN_TELEMETRY_LOGGING_CONFIG['loggers']
    if logger in loggers:
        loggers.get(logger)['level'] = log_level
    else:
        for lgr in loggers:
            loggers.get(lgr)['level'] = log_level
    logging.config.dictConfig(SOLACE_OPEN_TELEMETRY_LOGGING_CONFIG)

class SolaceLoggingAdapter(logging.LoggerAdapter):
    """
    This class is used as an adapter to the Logger class from the logging module so that custom decorators can be added.
    """
    def process(self, msg, kwargs):
        id_info = kwargs.pop('id_info', self.extra['id_info'])
        return '[%s] %s' % (id_info, msg), kwargs  # pylint: disable=consider-using-f-string
                                                   # We disable consider-using-f-string because
                                                   # this will be used as a part of the
                                                   # logger, and this way will be more performant
