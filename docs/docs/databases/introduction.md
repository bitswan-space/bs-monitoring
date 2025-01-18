---
sidebar_position: 1
---

# Overview

BS Monitoring supports various databases for storing monitoring data. This section covers supported databases and their configuration options. Databases interface is a little bit more complex than other components, all methods are optional and you only need to implement the ones you need for your use case. However, each of the databases should at least implement the `connect`, `close`, `execute` and `commit` methods.

## Supported Databases

- [Postgres](/docs/databases/postgres)
- [SQLite](/docs/databases/sqlite)
