import json

origin_file = input()
update_file = input()
users = {}
users_upd = {}
tabl = {origin_file: users,
        update_file: users_upd}

for file, dict_data in tabl.items():
    with open(file, encoding="UTF-8") as file_in:
        records = json.load(file_in)
        for rec in records:
            user = rec.pop('name')
            dict_data[user] = rec

for name, data in users_upd.items():
    if name in users.keys():
        for key, value in data.items():
            if key in users[name].keys() and value > users[name][key]:
                users[name][key] = users_upd[name][key]
            elif key not in users[name].keys():
                users[name][key] = users_upd[name][key]
    else:
        users[name] = users_upd[name]

with open(origin_file, "w", encoding="UTF-8") as file_out:
    json.dump(users, file_out, ensure_ascii=False, indent=2)
