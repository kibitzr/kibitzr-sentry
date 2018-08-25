"""
Send errors from Kibitzr checks to Sentry.

To setup this extension add following configuration to kibitzr-creds.yml:

```
sentry:
    dsn: "https://123:456@sentry.io/789"
    level: error
```

Note quotes aroung URL, they are required to disambiguate
YAML parser from parsing collon symbol as key-value mapping.
"""
import logging

from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

from kibitzr.conf import settings


logger = logging.getLogger(__name__)


LOG_LEVEL_CODES = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARN': logging.WARNING,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET,
}


def setup_sentry_handler(sentry_dsn, level=logging.ERROR):
    """
    Setup Sentry logging handler.
    https://docs.sentry.io/clients/python/integrations/logging/
    """
    handler = SentryHandler(sentry_dsn)
    handler.setLevel(level)
    setup_logging(handler)


def on_before_start(*_args, **_kwargs):
    """Function to be called from Kibitzr using entrypoints"""
    sentry_dsn = settings().creds.get('sentry', {}).get('dsn')
    if sentry_dsn:
        level_name = settings().creds['sentry'].get('level', '').upper()
        level = None
        if level_name:
            level = LOG_LEVEL_CODES.get(level_name)
            if level is None:
                logger.warning(
                    "Unknown sentry.level: %s. "
                    "Choose one of the existing levels: %s",
                    level_name,
                    ', '.join(sorted(LOG_LEVEL_CODES)),
                )
        setup_sentry_handler(sentry_dsn, level=level)
