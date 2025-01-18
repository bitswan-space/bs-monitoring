---
sidebar_position: 3
---

# OpsGenie

OpsGenie is a monitoring tool that allows you to send alerts to a channel. 

To use OpsGenie, you need to create an API key in the OpsGenie dashboard. You can find the API key in the OpsGenie dashboard. Then you can use the `OpsGenieAlertService` class to send alerts to the OpsGenie channel.

```python
from bs_monitoring.alert_services import AlertService, register_alert_service

@register_alert_service
class OpsGenieAlertService(AlertService):
    ...
```

## Configuration

This alert service requires the following configuration:

```yaml
AlertServices:
  - type: "OpsGenie"
    config:
      api_key: ${OPSGENIE_API_KEY}
```
