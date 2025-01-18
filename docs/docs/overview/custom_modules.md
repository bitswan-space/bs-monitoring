---
sidebar_position: 4
---

# Custom Modules

As showcased in the [Configuration](/overview/configuration) section, you can configure a `CustomMonitor` that uses a `Sqlite` database. This is a custom monitor that you can implement yourself, you can find more information about the `Monitor` interface in the [Monitors](/monitors/introduction) section.

You can also implement your own `DataSource`, `AlertService`, and `Database` modules. This page will showcase how to implement your own modules and how to register them in the library. 

BS Monitoring is designed to be easily extended with new components that fit nicely into the existing architecture. This library provides multiple decorators that you can use to implement your own modules. Namely:
- `register_database`
- `register_datasource`
- `register_alertservice`
- `register_monitor`

You can import these decorators from the `bs_monitoring.{database, datasource, alertservice, monitor}.base` modules and use them as such:

```python
from bs_monitoring.monitors.base import register_monitor
from bs_monitoring.common.utils import ConfigField


@register_monitor
class CustomMonitor(Monitor):
    foo = ConfigField(str)
```

Note the use of the `ConfigField` class, this is a helper class that you can use to define the configuration fields for your module. This class will automatically register the field in the configuration schema and will also provide a way to set the field from the configuration file.

Modules are called by stripping the `Database`, `DataSource`, `AlertService`, and `Monitor` suffix from the class name and using the remaining string to look up the module in the `DATABASES`, `DATASOURCES`, `ALERTSERVICES`, and `MONITORS` dictionaries.

For example, if you have a module called `CustomMonitor`, you can call it by using the string `Custom` in the configuration file.

```yaml
Monitors:
  - type: Custom
    config:
      foo: bar
```

