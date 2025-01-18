---
sidebar_position: 2
---

# Elastic Data Source

The `Elastic` data source is a data source that consumes messages from Elasticsearch. It is implemented as a custom data source, more information about how to implement a custom data source can be found in the [Custom Modules](/overview/custom_modules) section.

```python
@register_datasource
class ElasticDataSource(DataSource):
    ...
```

## Configuration

The `Elastic` data source is configured like this:

```yaml
DataSource:
  type: "Elastic"
  config:
    url: "http://localhost:9200"
    indices:
      - "index-1"
      - "index-2"
    history_length: 2
    basic_auth:
      - ${ES_USER}
      - ${ES_PASS}
```

History Length is the number of days that will be used to query Elasticsearch. This is useful for monitoring data over time, for example if you want to monitor the number of documents in a index over the last 2 days, you can set the history length to 2.

Indices is a list of indices that will be used to query Elasticsearch. This is useful for monitoring multiple indices.

Basic Auth is a list of username and password that will be used to authenticate with Elasticsearch. This is useful for authenticating with Elasticsearch using username and password.

Api Key is a string that will be used to authenticate with Elasticsearch. This is useful for authenticating with Elasticsearch using an API key.
