---
sidebar_position: 3
---

# SQLite

This module implements a database that stores data in a SQLite database. It can be configured as such:

```python
@register_database
class SQLiteDatabase(Database):
    ...
```

## Configuration

```yaml
Database:
  type: "SQLite"
  name: "sqlite_db"
  config:
    path: "/path/to/sqlite/database.db"
```

This will create a database that will be used to store data in the `sqlite_db` database. Fields in `config` section are required and must be passed in the configuration file. These are used to connect to the database.

The `name` field is used to identify the database in the configuration file and then other components can reference this database by its name.

```yaml
Monitors:
    - type: "Custom"
      db_name: "sqlite_db"
```
