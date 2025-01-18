---
sidebar_position: 1
---

# Overview

Data sources are the foundation of BS Monitoring. They represent the various systems, applications, and services that you want to monitor. This section covers all supported data sources and their configuration. 

## Data Source Interface

The `DataSource` interface is the base class for all data sources. It defines the methods that must be implemented by all data sources. This is how a custom data source could be implemented:

```python
from bs_monitoring.data_sources import DataSource, register_data_source
from bs_monitoring.alert_services import AlertService, alert
from typing import Any
from bs_monitoring.common.utils import ConfigField

@register_data_source
class CustomDataSource(DataSource):
    foo: str = ConfigField(str)

    def __init__(self, alert_service: AlertService, config: Any):
        super().__init__(config)
    
    @alert(
        message="Failed to consume messages from Custom Data Source.",
    )
    async def produce(self) -> dict[str, list[dict[str, Any]]]:
        ...
```

This custom data source will be registered as `Custom` and can be used in the configuration file like this:

```yaml
DataSource:
  type: "Custom"
  config:
    foo: bar
```

This will create a data source that will be used to produce data from the `Custom` data source. Note that the `foo` field is required and must be passed in the configuration file, also note that the `produce` method is required and must be implemented.

Important detail is the call to `super().__init__(config)`, this is how the data source is initialized and the configuration is passed to the data source. 

The `alert` decorator is used to define an alert that will be sent if the data source fails to produce data. This is useful for debugging and for alerting the user if the data source is not working as expected. More about this can be found in the [AlertService](/alertservices/introduction) section.

## Supported Data Sources

- [Elastic](/datasources/elastic)

