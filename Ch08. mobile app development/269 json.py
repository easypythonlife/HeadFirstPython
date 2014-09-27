import json
names = ['John', ['Johny', 'Jack'], 'Michael', ['Mike', 'Mikey', 'Mick']]
print(names)

to_transfer = json.dumps(names)
print(to_transfer)

from_transfer = json.loads(to_transfer)
print(from_transfer)
