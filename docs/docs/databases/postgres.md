---
sidebar_position: 2
---

# Postgres Database

This module implements a database that stores data in a PostgreSQL database. It can be configured as such:

```python
@register_database
class PostgresDatabase(Database):
    ...
```

## Configuration

```yaml
Database:
  type: "Postgres"
  name: "postgres_db"
  config:
    host: "localhost"
    port: 5432
    user: "postgres"
    password: ${POSTGRES_PASSWORD}
    database: ${POSTGRES_DB}
```

This will create a database that will be used to store data in the `postgres_db` database. Fields in `config` section are required and must be passed in the configuration file. These are used to connect to the database.

The `name` field is used to identify the database in the configuration file and then other components can reference this database by its name.

```yaml
Monitors:
    - type: "Custom"
      db_name: "postgres_db"
      config:
        ...
```
