import apizabbix
import json

api = apizabbix.connect()

host = api.host.get(
    output={'name': 'name'},
    selectTriggers={
    'name': 'description'
    }
)

raw_output = host
parsed_to_json = json.dumps(raw_output)

print(parsed_to_json)

api.user.logout()
