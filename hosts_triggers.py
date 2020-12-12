import apizabbix

api = apizabbix.connect()

host = api.host.get(
    output={'name': 'name'},
    selectTriggers={
    'name': 'description'
    }
)

from pprint import pprint
pprint(host)

api.user.logout()
