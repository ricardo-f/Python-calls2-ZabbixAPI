from pyzabbix import ZabbixAPI
import configparser

def connect():
    config = configparser.ConfigParser()
    config.read("config.ini")

    user = config.get('zabbix', 'user')
    password = config.get('zabbix', 'password')
    server = config.get('zabbix', 'server')

    zapi = ZabbixAPI(server)
    # Issues with certificate can be skipped with the commented line below
    # zapi.session.verify = False
    zapi.login(user, password)

    return zapi
