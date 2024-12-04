---
title: Bitswan Data Monitoring Library
description: Documentation for building and configuring data monitoring pipelines
---

# Bitswan Data Monitoring Library Documentation

## Table of Contents
- [Overview](#overview)
- [Core Components](#core-components)
- [Getting Started](#getting-started)
- [Creating Custom Components](#creating-custom-components)
- [Configuration Reference](#configuration-reference)
- [Best Practices](#best-practices)
- [Lifecycle Management](#lifecycle-management)

## Overview <a name="overview"></a>
Bitswan is a Python library for building data monitoring pipelines. It provides a flexible framework to monitor data sources, validate data quality, and send alerts when issues are detected. The library is built around composable components that can be easily extended and configured using YAML files.

## Core Components <a name="core-components"></a>

### Pipeline Component
The Pipeline is the main orchestrator that connects all components. It manages:
- Data collection from sources
- Data validation through monitors
- Alert dispatching
- Lifecycle management

### Data Sources Component
Data sources are responsible for fetching data. The library comes with:
- ElasticSearch data source
- Extensible base class for custom sources

### Monitors Component
Monitors validate data quality. Built-in monitors include:
- Data Quantity Monitor (checks for data presence)
- Data Schema Monitor (validates data structure)

### Alert Services Component
Alert services handle notifications. Supported services:
- Discord (webhook-based)
- OpsGenie

### Databases Component
Optional database connections for monitors:
- PostgreSQL
- SQLite

## Getting Started <a name="getting-started"></a>

### Basic Setup

1. Install the package:
```language-bash
pip install bitswan-monitoring
```

2. Create a configuration file (`config.yaml`):
```language-yaml
DataSource:
  type: "Elastic"
  config:
    url: "http://elasticsearch:9200"
    indices: ["my-index"]
    basic_auth: ["user", "pass"]

AlertService:
  type: "Discord"
  config:
    webhook_url: "${DISCORD_WEBHOOK_URL}"

Monitors:
  - type: "DataQuantity"
  - type: "DataScheme"
    config:
      file: "schema.yaml"

Interval: 3600  # Run every hour
```

3. Create a simple monitoring service:
```language-python
from bs_monitoring.pipeline import Pipeline
from bs_monitoring.common.configs.base import read_config

def main():
    config = read_config()  # Reads from --config argument
    pipeline = Pipeline.construct(config)
    pipeline.run()

if __name__ == "__main__":
    main()
```

4. Run the service:
```language-bash
python service.py --config config.yaml
```

## Creating Custom Components <a name="creating-custom-components"></a>

### Custom Data Source Implementation

```language-python
from bs_monitoring.data_sources import DataSource, register_data_source
from bs_monitoring.common.utils import ConfigField

@register_data_source
class MyDataSource(DataSource):
    # Define configuration fields
    api_key = ConfigField(str)
    url = ConfigField(str)

    def __init__(self, alert_service, config):
        super().__init__(config)
        self.alert_service = alert_service

    async def produce(self) -> dict[str, list[dict[str, Any]]]:
        # Implement data fetching logic
        data = {
            "my-source": [{"field": "value"}]
        }
        return data
```

### Custom Monitor Implementation

```language-python
from bs_monitoring.monitors import Monitor, register_monitor
from bs_monitoring.alert_services import alert
from bs_monitoring.common.utils import ConfigField

@register_monitor
class MyMonitor(Monitor):
    threshold = ConfigField(float, default=0.9)

    def __init__(self, alert_service, db_name=None, config=None):
        super().__init__(alert_service, db_name, config)

    @alert(message="Data quality issue detected")
    async def process(self, data: dict[str, Any]) -> None:
        # Implement validation logic
        for source, records in data.items():
            if not self._validate(records):
                raise MonitoringServiceError(f"Validation failed for {source}")
```

### Custom Alert Service Implementation

```language-python
from bs_monitoring.alert_services import AlertService, register_alert_service
from bs_monitoring.common.utils import ConfigField

@register_alert_service
class MyAlertService(AlertService):
    api_token = ConfigField(str)
    
    def __init__(self, config):
        super().__init__(config)

    def send_alert(self, message: str, description: str | None = None):
        # Implement alert sending logic
        pass
```

## Configuration Reference <a name="configuration-reference"></a>

### Environment Variables Configuration
Use environment variables in your config:
```language-yaml
DataSource:
  type: "MySource"
  config:
    api_key: "${API_KEY}"
```

### Database Configuration Example
```language-yaml
Databases:
  - type: "Postgres"
    name: "metrics_db"
    config:
      host: "localhost"
      port: 5432
      user: "${DB_USER}"
      password: "${DB_PASS}"
      database: "metrics"
```

### Monitor with Database Configuration
```language-yaml
Monitors:
  - type: "MyMonitor"
    db_name: "metrics_db"  # References database name
    config:
      threshold: 0.95
```

## Best Practices <a name="best-practices"></a>

### 1. Error Handling
- Use `MonitoringServiceError` for expected errors that should trigger alerts
- Implement proper error context in custom components

### 2. Async Support
- All data processing methods should be async-compatible
- Use `async/await` patterns consistently

### 3. Configuration Management
- Use `ConfigField` for all configurable parameters
- Implement proper type hints and defaults

### 4. Alert Implementation
- Use the `@alert` decorator to automatically handle error notifications
- Provide meaningful alert messages and contexts

### 5. Database Usage
- Only request database access if your monitor needs it
- Implement proper connection management

## Lifecycle Management <a name="lifecycle-management"></a>

### Pipeline Lifecycle Features
The pipeline handles:
- Graceful shutdown on SIGTERM/SIGINT
- Resource cleanup
- Continuous execution with configurable intervals
- Component initialization and dependency injection

### Component Lifecycle
Each component (DataSource, Monitor, AlertService) follows a consistent lifecycle:
1. Configuration parsing
2. Initialization
3. Runtime execution
4. Cleanup

This library provides a robust foundation for building data monitoring services while remaining flexible enough to accommodate custom requirements through its extensible component system.

