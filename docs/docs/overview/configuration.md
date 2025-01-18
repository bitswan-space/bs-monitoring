---
sidebar_position: 3
---

# Configuration

As previously mentioned, BS Monitoring is configured via a yaml file. This file is used to construct the monitoring pipeline.
The configuration file is provided as a command line argument to the python script, as such:

```bash
python <your-script>.py --config config.yaml
```

In your script, you can then use function `bs_monitoring.common.configs.base.read_config()` to read the configuration file and properly parse it and pass it to create the monitoring pipeline.

```python
from bs_monitoring.common.configs.base import read_config
from bs_monitoring.pipeline import Pipeline


args = read_config()
pipeline = Pipeline.construct(args)
pipeline.run()
```

This configuration file is a yaml file that contains the configuration for each of the components in the monitoring pipeline. Each
pipeline requires a `DataSource`, one or more `Monitor`s and an `AlertService` to be configured. Optionally, a `Database` can be configured to store persistent data.

The following is an example configuration file, you can notice that environment variables are used to pass the configuration for the `DataSource` and `AlertService` with the special `${...}` format.

```yaml
Interval: 86400 # 1 day

AlertService:
  type: "Opsgenie"
  config:
    api_key: ${OPSGENIE_API_KEY}

Database:
  type: "Sqlite"
  name: "custom_monitor_db"
  config:
    path: "bs-monitoring.db"

DataSource:
  type: "Elastic"
  config:
    url: "http://localhost:9200"
    indices:
      - "bs-de-registry"
    history_length: 2
    basic_auth:
      - ${ES_USER}
      - ${ES_PASS}

Monitors:
  - type: DataQuantity
  - type: DataScheme
    config:
      file: data-scheme.yaml
  - type: Custom
    db_name: "custom_monitor_db"
    config:
      foo: bar
```

In this example, we have a `DataSource` that is configured to use Elasticsearch, with a history length of 2. We have two `Monitor`s, one is a `DataQuantity` monitor and the other is a `DataScheme` monitor.
We also have a `Custom` monitor that is configured to use a `Sqlite` database with the name `custom_monitor_db`. `Custom` is a custom monitor that you can implement yourself, you can find more information about how to implement a custom monitor in the [Custom Modules](/docs/overview/custom_modules) section.

The `AlertService` is configured to use the `Opsgenie` alert service, with the `api_key` being passed as an environment variable.

The `Database` is configured to use a `Sqlite` database with the name `custom_monitor_db` and the path to the database file is `bs-monitoring.db`.

With the `Interval` field, we set the interval at which the monitoring pipeline will be run. In this case, it will be run every 24 hours.




