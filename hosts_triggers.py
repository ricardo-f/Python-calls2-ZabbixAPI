import apizabbix

api = apizabbix.connect()

host = api.host.get(
    output='extend',
    selectTriggers={
    'name': 'description'
    }
)

from pprint import pprint
pprint(host)

api.user.logout()
