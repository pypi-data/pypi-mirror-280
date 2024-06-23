import asyncio
import os
import unittest

from .. import session_provider
from ..async_index import AsgardIndex
from ..settings import Settings


def run_coroutine(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


class AsgardIndexTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        resources_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")
        self.intuition_session = session_provider.session
        self.settings = Settings(os.path.join(resources_path, "default_settings.yaml"))

    def tearDown(self):
        super().tearDown()

    def test_get_index_path(self):
        indexes = {
            "engine_type": "text",
            "engine_id": "messageType",
            "language": "en",
            "vertical": "default",
            "partner_id": "978",
            "model_name": "messageType",
            "model_type": "default",
            "stage": "DEPLOYED"
        }
        asgard_index = AsgardIndex(indexes=indexes, base_path=self.settings.base_path, fs=self.intuition_session.fs)
        self.assertEqual(
            run_coroutine(asgard_index.get_index_path("model", "output", base_path=asgard_index.base_path)),
            asgard_index.base_path + "model/output/engine_type=text/engine_id=messageType/language=en/vertical=default/partner_id=978/model_name=messageType/model_type=default/stage=DEPLOYED/version=0"
        )

    def test_get_index_path_without_version(self):
        indexes = {
            "engine_type": "text",
            "engine_id": "messageType",
            "language": "en",
            "vertical": "default",
            "partner_id": "978",
            "model_name": "messageType",
            "model_type": "default",
            "stage": "DEPLOYED"
        }
        asgard_index = AsgardIndex(indexes=indexes, base_path=self.settings.base_path, fs=self.intuition_session.fs)
        self.assertEqual(
            run_coroutine(asgard_index.get_index_path_without_version("model", "output", base_path=asgard_index.base_path)),
            asgard_index.base_path + "model/output/engine_type=text/engine_id=messageType/language=en/vertical=default/partner_id=978/model_name=messageType/model_type=default/stage=DEPLOYED"
        )

    def test_compulsion(self):
        indexes = {
            "engine_type": "text",
            "language": "en",
            "vertical": "default",
            "partner_id": "978",
            "model_name": "messageType",
            "model_type": "default",
            "stage": "DEPLOYED"
        }
        with self.assertRaises(ValueError):
            AsgardIndex(indexes=indexes, base_path=self.settings.base_path, fs=self.intuition_session.fs)


if __name__ == "__main__":
    unittest.main(verbosity=2)
