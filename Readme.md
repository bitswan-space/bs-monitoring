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
        # Your data fetching logic here
        return {"source": [{"data": "value"}]}
```

### Monitors
Validate your data. Create custom monitors by inheriting from `Monitor`:
```python
@register_monitor
class MyMonitor(Monitor):
    threshold = ConfigField(float, default=0.9)
    
    @alert(message="Data validation failed")
    async def process(self, data: dict) -> None:
        # Your validation logic here
        if not self._validate(data):
            raise MonitoringServiceError("Validation failed")
```

### Alert Services
Handle notifications when issues are detected:
```python
@register_alert_service
class MyAlertService(AlertService):
    webhook_url = ConfigField(str)
    
    def send_alert(self, message: str, description: str = None):
        # Your alerting logic here
        pass
```

## Configuration

Use YAML files to configure your monitoring service:
```yaml
# Define databases (optional)
Databases:
  - type: "Postgres"
    name: "metrics"
    config:
      host: "${DB_HOST}"
      port: 5432

# Configure your data source
DataSource:
  type: "MySource"
  config:
    api_key: "${API_KEY}"

# Set up alerting
AlertService:
  type: "Discord"
  config:
    webhook_url: "${WEBHOOK_URL}"

# Define monitors
Monitors:
  - type: "DataQuantity"
  - type: "MyMonitor"
    db_name: "metrics"
    config:
      threshold: 0.95

# Set monitoring interval (seconds)
Interval: 3600
```

## Environment Variables

Use environment variables in your config with `${VAR_NAME}` syntax:
```yaml
DataSource:
  config:
    api_key: "${API_KEY}"
```

## Best Practices

1. **Error Handling**: Use `MonitoringServiceError` for alertable errors
2. **Async Support**: Implement async methods for better performance
3. **Configuration**: Use `ConfigField` for all configurable parameters
4. **Alerts**: Use the `@alert` decorator for automatic error notifications
5. **Database**: Only request database access when needed

For detailed documentation, visit our [Documentation](link-to-your-documentation).
