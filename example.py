from src import ShibaConnection

import json

cx = ShibaConnection(host='localhost', port=3308, user='root', password='duoc')
cx.create_database('hola2')
cx.use_database('hola2')

table = cx.create_table('users')
table.increments('id')
table.string('name', 20)
table.integer('age')
table.text('languages')
table.text('settings')
table.build()
print (table)

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