import apizabbix
import json

api = apizabbix.connect()

host = api.host.get(
    output={'name': 'name'},
    selectTriggers={
    'name': 'description'
    }
)

data=[]

for host in host:
    triggers=host['triggers']
    for trigger in triggers:
        data.append({"name": host['name'],  "description": trigger['description']})

x = data
y = json.dumps(x)

print(y)

api.user.logout()
