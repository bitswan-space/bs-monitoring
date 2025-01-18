---
sidebar_position: 3
---

# DataScheme

This monitor is used to check the scheme of the data, it uses a yaml file to define the expected scheme of the data. In the background, it uses the `cerberus` library to validate the data.

```python
@register_monitor
class DataSchemeMonitor(Monitor):
    ...
```

## Configuration

This monitor requires a configuration file, the configuration file should be a yaml file that defines the expected scheme of the data.

## Usage

This monitor can be used in the configuration file like this:

```yaml
Monitors:
  - type: "DataScheme"
    file: "path/to/your/scheme.yaml"
```

This schema file should be a yaml file that defines the expected scheme of the data.

```yaml

country:
  type: string
  required: false
  allowed:
    - "DE"
    - "BE"
    - "FR"
    - "UK"
```
