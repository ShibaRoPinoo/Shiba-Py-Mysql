# Shiba-Py-Mysql

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/ShibaRoPinoo/Shiba-Py-Mysql/blob/main/LICENSE)

Shiba-Py-Mysql is a lightweight Python library that provides a convenient interface for interacting with MySQL databases using the `pymysql` library. It simplifies common database administration tasks such as creating databases, selecting databases, creating tables, and performing basic CRUD operations.

## Features

- Easy database creation and selection.
- Table creation with support for different column types.
- Retrieving data from tables with support for JSON fields.

## Installation

You can install Shiba-Py-Mysql using pip:

```shell
pip install shiba-mysql
```

```python

import shiba as s

# Create a connection to the MySQL database
connection = s.ShibaConnection(host='localhost', port=3306, user='myuser', password='mypassword')

# Create a new database
connection.create_database('my_database')

# Select the database
connection.use_database('my_database')

# Create a table
table_builder = connection.create_table('users')
table_builder.increments('id')
table_builder.string('name', 20)
table_builder.integer('age')
table_builder.text('languages')
table_builder.text('settings')
table_builder.build()
```

```python
# Insert data into the table
data_single = {
    "name": "John",
    "age": 30,
    "languages": json.dumps(["Python", "JavaScript", "Java"]),
    "settings": json.dumps({"theme": "dark", "notifications": True})
}

data_list = [
    {
        "name": "Alice",
        "age": 25,
        "languages": json.dumps(["Python", "C++"]),
        "settings": json.dumps({"theme": "light", "notifications": False})
    },
    {
        "name": "Bob",
        "age": 35,
        "languages": json.dumps(["JavaScript", "TypeScript"]),
        "settings": json.dumps({"theme": "dark", "notifications": True})
    }
]

cx.table('users').insert(data_single)
cx.table('users').insert(data_list)

x = cx.table("users").get()
for e in x:
    for k, v in e.items():
        if k == "languages":
            languages = json.loads(v)
            languages_str = ", ".join(languages)
            print(f"Languages: {languages_str}")
        elif k == "settings":
            settings_str = json.loads(v)
            print(f"Settings\n  Theme: {settings_str['theme']}\n  Notifications: {settings_str['notifications']}")
        else:
            print(f"{k}: {str(v)}")
```

## LICENSE

This project is under the [MIT License](https://github.com/ShibaRoPinoo/Shiba-Py-Mysql/blob/main/LICENSE).