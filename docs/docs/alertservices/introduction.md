---
sidebar_position: 1
---

# Overview

Alert services are used to send alerts to the user. They are used to send alerts to the user when a monitor fails.

Alert services are implemented as a class that inherits from the `AlertService` class. This class should implement the `send_alert` method, which is used to send the alert to the user.

```python
from bs_monitoring.alert_services import AlertService, register_alert_service
from bs_monitoring.common.utils import ConfigField


@register_alert_service
class AlertService(AlertService):
    foo = ConfigField(str)

    def __init__(self, config: Any):
        super().__init__(config)

    def send_alert(self, message: str, description: str | None = None):
        ...
```

These alert services are registered with the `register_alert_service` decorator.

Components in the pipeline can use the `alert` decorator to send an alert to the user as such:

```python
@alert(
    message="Custom monitor failed to process data.",
)
async def process(self, data: dict[str, list[dict[str, Any]]]) -> None:
    ...
```

## Supported Alert Services

- [Discord](/docs/alertservices/discord)
- [OpsGenie](/docs/alertservices/opsgenie)
