# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Create configuration to deploy Kubernetes resources."""


def GenerateConfig(context):
    """Create a Knative Service."""

    propertiesWithoutTypeProvider = context.properties.copy()
    del propertiesWithoutTypeProvider['typeProvider']
    propertiesWithoutTypeProvider['apiVersion'] = 'serving.knative.dev/v1'
    propertiesWithoutTypeProvider['kind'] = 'Service'
    if 'name' not in propertiesWithoutTypeProvider['metadata']:
        propertiesWithoutTypeProvider['metadata']['name'] = context.env['name']
    resources = [{
        'name': context.env['name'],
        'type': ''.join([context.env['project'], '/', context.properties['typeProvider'], ':',
                         '/apis/serving.knative.dev/v1/namespaces/{namespace}/services/{name}']),
        'properties': propertiesWithoutTypeProvider,
    }]

    return {'resources': resources}
