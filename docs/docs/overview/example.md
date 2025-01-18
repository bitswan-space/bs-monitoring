---
sidebar_position: 5
---

# Example

This section will showcase a simple example with predefined modules on how to create a simple monitoring pipeline that runs every 24 hours and checks if the data quantity for predefined Elasticsearch indices is greater than 0.

```python
# main.py
from dotenv import load_dotenv
from bs_monitoring.pipeline import Pipeline

from bs_monitoring.common.configs.base import read_config


def main():
    load_dotenv()
    arguments = read_config()

    pipeline = Pipeline.construct(arguments)
    pipeline.run()


if __name__ == "__main__":
    main()
```


```yaml
# config.yaml
Interval: 86400 # 24 hours

AlertService:
  type: "Discord"
  config:
    webhook_url: ${DISCORD_WEBHOOK_URL}

DataSource:
  type: "Elastic"
  config:
    url: ${ELASTIC_URL}
    indices:
      - index-1
      - index-2
      - index-3
    history_length: 1
    basic_auth:
      - ${ES_USER}
      - ${ES_PASS}

Monitors:
  - type: DataQuantity
```

This configuration will create a monitoring pipeline that will run every 24 hours and check if the data quantity for the indices `index-1`, `index-2`, and `index-3` is greater than 0. If not, it will send a message to the Discord channel specified in the `AlertService` configuration. 

The `DataSource` is configured to use the `Elastic` data source, with the `url` being passed as an environment variable. The `indices` field is a list of indices to check, in this case, it will check the indices `index-1`, `index-2`, and `index-3`. The `history_length` field is the number of days to look back at when checking the data quantity.

The `AlertService` is configured to use the `Discord` alert service, with the `webhook_url` being passed as an environment variable.

The `Monitors` field is a list of monitors to run. In this case, we have a `DataQuantity` monitor that will check if the data quantity for the indices is greater than 0.

To run this example, you can use the following command:

```bash
python main.py --config config.yaml
```
