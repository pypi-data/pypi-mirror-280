import unittest

from ..server_configuration import ServerConfiguration
from ..server_configuration import ServerConfigurationProvider
from ..session_provider import session

import logging
class ServerConfigTest(unittest.TestCase):

    def setUp(self):
        self.serverConfigStore = ServerConfigurationProvider(session.settings)
        ServerConfiguration(
            client_id=-1,
            name="test_dummy",
            server_type="dummy_test",
            partner_id=2606,
            server_category="MONGO"
        ).save()

    def tearDown(self):
        ServerConfiguration.objects(server_type="dummy_test", partner_id=2606).delete()

    def test_mongo_server_config(self):

        server_config = self.serverConfigStore.mongodb_server_config(server_type="dummy_test", partner_id=2606)
        assert isinstance(server_config, ServerConfiguration)
        assert server_config.server_type == "dummy_test"



