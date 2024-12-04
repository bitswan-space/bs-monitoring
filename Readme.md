# Bitswan Data Monitoring Library

## Overview

Bitswan is a Python library for building data monitoring pipelines. It enables you to:
- Monitor periodic data sources
- Validate data quality
- Send alerts when issues are detected
- Configure everything through YAML files

## Quick Start

1. Install the library:
```bash
pip install bitswan-monitoring
```

2. Create a config file (`config.yaml`):
```yaml
DataSource:
  type: "Elastic"
  config:
    url: "http://elasticsearch:9200"
    indices: ["my-index"]

AlertService:
  type: "Discord"
  config:
    webhook_url: "${DISCORD_WEBHOOK_URL}"

Monitors:
  - type: "DataQuantity"
    config:
      threshold: 100
```

3. Create your monitoring service:
```python
from bs_monitoring.pipeline import Pipeline
from bs_monitoring.common.configs.base import read_config

def main():
    config = read_config()
    pipeline = Pipeline.construct(config)
    pipeline.run()

if __name__ == "__main__":
    main()
```

## Core Components

### Pipeline
The main orchestrator that connects all components:
- Manages data collection
- Runs monitors
- Handles alerts
- Controls the monitoring lifecycle

### Data Sources
Fetch data from various sources. Create custom sources by inheriting from `DataSource`:
```python
@register_data_source
class MyDataSource(DataSource):
    api_key = ConfigField(str)
    
    async def produce(self) -> dict[str, list[dict]]:
        return {"source": [{"data": "value"}]}
```

### Monitors
Validate your data by inheriting from `Monitor` and implementing validation logic with the `@alert` decorator for automatic error notifications.

### Alert Services
Handle notifications when issues are detected by implementing custom alert services that inherit from `AlertService`.

## Configuration

Use YAML files to configure your monitoring service and environment variables with `${VAR_NAME}` syntax:
```yaml
DataSource:
  type: "MySource"
  config:
    api_key: "${API_KEY}"

AlertService:
  type: "Discord"
  config:
    webhook_url: "${WEBHOOK_URL}"

Monitors:
  - type: "DataQuantity"
    config:
      threshold: 0.95
```

## Best Practices

1. **Error Handling**: Use `MonitoringServiceError` for alertable errors
2. **Async Support**: Implement async methods for better performance
3. **Configuration**: Use `ConfigField` for all configurable parameters
4. **Alerts**: Use the `@alert` decorator for automatic error notifications
5. **Database**: Only request database access when needed

For detailed documentation, visit our [Documentation](link-to-your-documentation).
