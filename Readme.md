# Bitswan Data Monitoring and Analysis Library

## Overview

This library provides easy abstraction over defining monitoring services for periodical data sources. It is designed to be used in a microservice architecture where each service is responsible for monitoring a specific data source. The library provides a simple interface to define the pipeline of data collection, validation and alerting. The library is designed to be extensible and can be easily integrated with any data source, enabling the user to define custom data collection and validation logic, which then can be configured using `yaml` files, which are the main configuration object for this library.

## Components

Firstly, the library uses `yaml` files to define the structure of the whole service. The configuration file defines all the components of the service. The format of the file is as follows:

```yaml
Databases:
  - type: "Postgres"
    name: "test"
    config:
      key: value

AlertService:
  type: "type"
  config:
    key: value

DataSource:
  type: "type"
  config:
    key: value

Monitors:
  - type: "type"
    db_name: "test"
    config:
      key: value
  - type: "type"
    config:
      key: value
```

The values provided in the configuration file are used to construct the components of the service. All the components define configurable attributes via class attributes of type `ConfigFiel(type, default=default_value)`, such as `api_key = ConfigField(str | None, default=None)` which defines an attribute `api_key` of type `str` with default value `None`. Then, in the configuration file, the attribute can be set as `api_key: "value"` inside the `config` subpart. The configuration file also supports the use of environment variables, which are then expanded.
You can use environment variables in the configuration file by using the following syntax: `${ENV_VAR_NAME}`. The library will then expand the environment variable to its value.

Main component of this library is `Pipeline`. It's an object encapsulating all of the parts: data collection, validation, alerting, database, etc. The pipeline is always constructed from a configuration file, which is a `yaml` file. The configuration file defines the pipeline and its components. The configuration file is then used to construct the components of the pipeline.
The pipeline is then the controlling component of the whole runtime. Whole service could be defined as simply as:

```python
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

This code will read the configuration file from the path provided in the environment variable `CONFIG_PATH`, construct the pipeline and run it. The pipeline will then collect the data from the history, validate it and send alerts if necessary.

## Data Collection

All data collection is done by the `DataSource` object. The `DataSource` object is responsible for collecting the data from the data source. The data source can be anything, such as an API, a database, a file, etc. The `DataSource` object is reponsible for collecting the data from the history, which is then passed to all of the `Monitor` objects. You can write your own `DataSource` object by inheriting from the `DataSource` class and implementing the `produce` method, which should return the data from the history of type `dict[str, list[dict[str, Any]]]`.
If you want to have a configurable attribute, you can specify it in the `DataSource` class as a class attribute of type `ConfigField`. The attribute can then be set in the configuration file under the `config` subpart. To then make the new `DataSource` object available in the configuration file, you need to register it in the `DataSource` registry. You can do this by decorating the class with `register_data_source` decorator.

## Alerting

Whole point of this library is to provide easy alerting in-case something goes wrong, that's where `AlertService` component comes in. The `AlertService` object is responsible for sending alerts. The alerts can be sent via email, slack, etc. To define your own `AlertService` inhertit from the `AlertService` class and implement the `send_alert` method. In the public API, there is also `alert` decorator available, which can be used to decorate the `Monitor` methods. The decorator will then send an alert if the decorated method raises an exception. For configuration, same rules apply as for the `DataSource` object, but registering the class can be done via `register_alert_service` decorator.

## Data Monitoring


