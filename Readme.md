# Data Monitoring and Analysis Service

## Overview

This service is responsible for monitoring and analyzing the data from different data sources. If the data does not conform to the expected format, is not available, there is not enough data, etc., the service will send a notifaction to the configured alerting platform.

The service is implemented in Python and configurable via `.yaml` configuration file together with environment variables. An example of the configuration file is provided in the [configs](configs) directory.

The service is implemented as a set of components, each of which is responsible for a specific task. Custom components can be added by implementing the base class for each component type and adding the component to the matching factory function. The components are:

- [**Data Source**](src/data_sources): Responsible for fetching the data from the source.
- [**Alert Service**](src/alert_services): Responsible for sending alerts to the configured alerting platform.
- [**Data Monitor**](src/data_monitors): Responsible for monitoring the data and sending alerts if the data does not conform to the expected format, is not available, there is not enough data, etc. Uses the decorator `@alert` from [`AlertService`](src/alert_services/base.py#L26) module to send alerts.

## Custom components

To add a custom component, you need to implement the base class for the component type (always specified in `base.py` file) and add the component to the matching factory function. The factory functions are implemented in the `__init__.py` file of each component type. Only difference is the `Monitor` component, which can be registered using the [`@register_monitor`](src/monitors/base.py#L26) decorator, as can be seen [here](src/monitors/data_quantity.py#L20).After implementing the custom component, you can add it to the configuration file and configure it using the environment variables or the configuration file. In case of the `Monitor` component, the type of the monitor to be specified in the configuration file should match the name of the class implementing the monitor, stripped of *Monitor* if the class name ends with it.

## Running the service

The service comes with a prebuilt Docker image, which can be found on [AWS ECR](public.ecr.aws/bitswan/data-flow-monitoring). The service is ran using a cronjob. The cronjob is configured to run the service at 03:00 AM UTC every day. The image expects the configuration file to be mounted at `configs/config.yaml` and the environment variables to be passed to the container. The environment variables are used to substitute the values in the configuration file.
