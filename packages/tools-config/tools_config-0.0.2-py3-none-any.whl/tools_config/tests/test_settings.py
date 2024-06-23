import unittest

from . import default_settings_file
from ..settings import Settings


class SettingsTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_settings(self):
        settings = Settings(default_settings_file)
        valid_settings = settings.__dict__
        true_settings = {'PERSISTENCE_CONFIG':
                             {'mongo_server_config':
                                  {'name': 'SPR_GLOBAL',
                                   'url': '172.16.0.12',
                                   'host': '172.16.0.12',
                                   'port': 27017
                                   }
                              },
                         'base_path': 's3://spr-asgard/temp/',
                         'fileSystem':
                             {'s3.key': None,
                              's3.secret': None
                              }
                         }
        self.assertEqual(valid_settings, true_settings)


if __name__ == '__main__':
    unittest.main(verbosity=2)
