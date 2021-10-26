import json

with open('C:/Users/ryanw/Documents/char_classes.json') as json_file:
    data = json.load(json_file)

print("name".ljust(15), "str".ljust(5), "int".ljust(5), "wis".ljust(5), "dex".ljust(5), "con".ljust(5))
for name, values in data.items():
    print(name.ljust(15), "{:6}{:6}{:6}{:6}{:6}".format(\
            *map(str, [values['str'], values['int'], values['wis'], values['dex'], values['con']])))