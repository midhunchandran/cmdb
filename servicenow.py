from os import listdir, mkdir
from os.path import isdir, join
import json
import requests
from requests.auth import HTTPBasicAuth
import re
import datetime
import time
import sys
import logging


class ServiceNowAPI:
    #def __init__(self):
    #    self.base_uri = 'https://instance.service-now.com/'

    def set_base_uri(self, base_uri):
        self.base_uri = base_uri

    def set_auth(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def get_table_schema(self, table_name):
        uri = self.base_uri + 'api/now/v1/table/sys_dictionary?name=' + table_name
        print uri
        headers = {'accept' : 'application/json'}
        r = requests.get(uri, headers=headers, auth=self.auth) #auth=HTTPBasicAuth(self.user, self.password))

        if r.status_code != requests.codes.ok:
            raise Exception('Ticket query failed with error ' + str(r.status_code))


        print json.dumps(json.loads(r.text), indent=4)
        return json.loads(r.text)


if __name__ == '__main__':
    snow = ServiceNowAPI()

    with open('config.json', 'r') as cf:
        config = json.loads(cf.read())
        base_uri = config['instance_uri']
        username = config['username']
        password = config['password']

        snow.set_base_uri(base_uri)
        snow.set_auth(username, password)

    result = snow.get_table_schema('cmdb_ci_hardware')

    
