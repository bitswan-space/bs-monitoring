---
sidebar_position: 2
---

# Discord

Discord is a messaging platform that allows you to send alerts to a channel. 

To use Discord, you need to create a webhook in the Discord server. You can find the webhook URL in the Discord server settings. Then you can use the `DiscordAlertService` class to send alerts to the Discord channel.

```python
from bs_monitoring.alert_services import AlertService, register_alert_service

@register_alert_service
class DiscordAlertService(AlertService):
    ...
```

## Configuration

This alert service requires the following configuration:

```yaml
AlertServices:
  - type: "Discord"
    config:
      webhook_url: ${DISCORD_WEBHOOK_URL}
```



