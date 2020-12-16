import apizabbix

api = apizabbix.connect()

host = api.host.get(
    output={'name': 'name'},
    selectTriggers={
    'name': 'description'
    }
)

for host in host:
    triggers=host['triggers']
    for trigger in triggers:
        print('Name:' + host['name'] + 'Alarme: ' + trigger['description'])

api.user.logout()
