########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

__author__ = 'idanmo'


import requests
import json


class NodesApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def get_node_instance(self, node_id,
                          get_state_and_runtime_properties=True):

        resource_path = '/nodes/{0}'.format(node_id)

        query_params = {
            'state_and_runtime_properties':
            str(get_state_and_runtime_properties).lower()
        }

        url = self.api_client.resource_url(resource_path)

        response = requests.get(url,
                                params=query_params)

        self.api_client.raise_if_not(200, response, url)

        return response.json()

    def update_node_instance(self, node_id, state_version,
                             runtime_properties=None, state=None):

        resource_path = '/nodes/{0}'.format(node_id)
        url = self.api_client.resource_url(resource_path)
        data = {
            'state_version': state_version
        }
        if state:
            data['state'] = state
        if runtime_properties:
            data['runtime_info'] = runtime_properties

        response = requests.patch(url,
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(data))

        self.api_client.raise_if_not(200, response, url)

        return response.json()
