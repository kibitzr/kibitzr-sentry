# kibitzr-sentry

[![PyPI](https://badge.fury.io/py/kibitzr-sentry.svg)](https://pypi.org/project/kibitzr-sentry/)

Send errors from Kibitzr checks to Sentry.

# Installation

```
pip install kibitzr-sentry
```

# Configuration

To setup this extension add following configuration to kibitzr-creds.yml:

```
sentry:
    dsn: "https://123:456@sentry.io/789"
    level: error
```

Note quotes aroung URL, they are required to disambiguate
YAML parser from parsing collon symbol as key-value mapping.
