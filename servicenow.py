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
    def __init__(self):
        self.base_uri = 'https://dev17199.service-now.com/'
        self.user = 'apiuser'
        self.password = '9a9j0D%V'

    def get_table_schema(self, table_name):
        uri = self.base_uri + 'api/now/v1/table/sys_dictionary?name=' + table_name
        print uri
        headers = {'accept' : 'application/json'}
        r = requests.get(uri, headers=headers, auth=HTTPBasicAuth(self.user, self.password))

        if r.status_code != requests.codes.ok:
            raise Exception('Ticket query failed with error ' + str(r.status_code))


        print json.dumps(json.loads(r.text), indent=4)
        return json.loads(r.text)


if __name__ == '__main__':
    snow = ServiceNowAPI()
    result = snow.get_table_schema('cmdb_ci_hardware')

    
