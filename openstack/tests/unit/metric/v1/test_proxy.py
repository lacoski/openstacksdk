# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.metric.v1 import _proxy
from openstack.tests.unit import test_proxy_base


class TestMetricProxy(test_proxy_base.TestProxyBase):
    def setUp(self):
        super(TestMetricProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_capabilities_list(self):
        self.verify_list('openstack.metric.v1.capabilities.Capabilities.list',
                         self.proxy.list_capabilities)