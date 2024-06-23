import unittest

from ..server_configuration import InternalServerConfiguration
from ..server_configuration import InternalServerConfigStore
from ..session_provider import session


#please remove 'db_alias': 'spr-global' field in InternalServerConfiguration document to run test
class ServerConfigTest(unittest.TestCase):
    def setUp(self):
        self.serverConfigStore = InternalServerConfigStore(session.settings)

    def test_add_server_config(self):
        assert isinstance(self.serverConfigStore.add_server_configuration('xyz', 'kafka',
                                                                        'qa', '0.0.0.0',
                                                                        100), InternalServerConfiguration)

    def test_get_config_byname(self):
        name = 'xyz'
        server_config = self.serverConfigStore.get_server_configuration_by_name(name)
        assert isinstance(server_config, InternalServerConfiguration)

