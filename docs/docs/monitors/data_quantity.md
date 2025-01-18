---
sidebar_position: 1
---

# DataQuantity

This monitor is used to check the quantity of data. It will check if the quantity of data is 0. If it is, it will send an alert.

```python
@register_monitor
class DataQuantityMonitor(Monitor):
    ...
```

## Configuration

This monitor does not require any configuration.

## Usage

This monitor can be used in the configuration file like this:

```yaml
Monitors:
  - type: "DataQuantity"
```
