---
sidebar_position: 1
---

# Overview

Monitors are the core components that track and analyze your metrics. This section covers the different types of monitors available and how to configure them effectively. Monitors should implement the `process` method, which is used to process the data from the data source and call alert service if the data is not as expected.

All monitors should inherit from the `Monitor` class, which is the base class for all monitors. You could implement your own monitor by inheriting from the `Monitor` class and implementing the `process` method, then register your class with the `register_monitor` decorator as such:

```python
from bs_monitoring.monitors import Monitor, register_monitor
from bs_monitoring.alert_services import AlertService, alert
from bs_monitoring.common.utils import MonitoringServiceError
from typing import Any

class CustomMonitorError(MonitoringServiceError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


@register_monitor
class CustomMonitor(Monitor):
    def __init__(self, alert_service: AlertService, db_name: str | None = None, config: Any = None):
        super().__init__(alert_service, db_name, config)
        ...

    @alert(
        message="Custom monitor failed to process data.",
    )
    async def process(self, data: dict[str, list[dict[str, Any]]]) -> None:
        ...
        raise CustomMonitorError("Custom monitor failed to process data.")
```

This custom monitor will be registered as `Custom` and can be used in the configuration file like this:

```yaml
Monitors:
  - type: "Custom"
```

The `process` method is the main method that will be called by the pipeline. It will receive the data from the data source and then process it. If the data is not as expected, the `alert_service` will be called to send an alert. The `alert` decorator is used to send an alert if the `process` method raises an exception that inherits from `MonitoringServiceError`.

## Supported Monitors

- [DataQuantity](/docs/monitors/data_quantity)
- [DataScheme](/docs/monitors/data_scheme)
