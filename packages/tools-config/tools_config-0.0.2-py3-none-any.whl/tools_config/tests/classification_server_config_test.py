import unittest

from ..server_configuration import ServerConfiguration
from ..server_configuration import ServerConfigurationProvider
from ..session_provider import session


class ClassificationServerConfigTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.server_configuration_provider = ServerConfigurationProvider(session.settings)

        server_category = "CLASSIFICATION"
        port = 80
        additional = dict()

        # add 0-en
        name = "dummy_test_1a"
        partner_id = 0
        server_type = "test_dummy_1"
        lang = "en"
        ip = "test_dummy_1a@sprinklr.com"
        ServerConfiguration(
            name=name,
            client_id=-1,
            partner_id=partner_id,
            server_type=server_type,
            server_category=server_category,
            lang=lang,
            ip=ip,
            port=port,
            additional=additional
        ).save()

        # add different partnerID, 999-en
        name = "dummy_test_1b"
        partner_id = 999
        server_type = "test_dummy_1"
        lang = "en"
        ip = "test_dummy_1b@sprinklr.com"
        ServerConfiguration(
            name=name,
            client_id=-1,
            partner_id=partner_id,
            server_type=server_type,
            server_category=server_category,
            lang=lang,
            ip=ip,
            port=port,
            additional=additional
        ).save()

        # add multilingual config, default fallback
        name = "dummy_test_1c"
        partner_id = 0
        server_type = "test_dummy_1"
        ip = "test_dummy_1c@sprinklr.com"
        ServerConfiguration(
            name=name,
            client_id=-1,
            partner_id=partner_id,
            server_type=server_type,
            server_category=server_category,
            lang=None,
            ip=ip,
            port=port,
            additional=additional
        ).save()

        # add different language, 0-ja
        name = "dummy_test_1d"
        partner_id = 0
        server_type = "test_dummy_1"
        lang = "ja"
        ip = "test_dummy_1d@sprinklr.com"
        ServerConfiguration(
            name=name,
            client_id=-1,
            partner_id=partner_id,
            server_type=server_type,
            server_category=server_category,
            lang=lang,
            ip=ip,
            port=port,
            additional=additional
        ).save()

        # non-moderation service of only one config
        name = "dummy_test_2"
        partner_id = 0
        server_type = "test_dummy_2"
        ip = "test_dummy_2@sprinklr.com"
        ServerConfiguration(
            name=name,
            client_id=-1,
            partner_id=partner_id,
            server_type=server_type,
            server_category=server_category,
            lang=None,
            ip=ip,
            port=port,
            additional=additional
        ).save()

        ServerConfiguration(
            name="random",
            client_id=-1,
            partner_id=-1,
            server_type="KAFKA_FEED_SERVER_CONFIG",
            server_category="KAFKA_FEED_SERVER_CONFIG",
            kafka_cluster_id="kafka_cluster_id",
            lang=None,
            ip=ip,
            port=port,
            additional=additional
        ).save()

    def test_kafka_feed_config_fetch(self):
        config = self.server_configuration_provider.kafka_feed_config(kafka_cluster_id="kafka_cluster_id")
        print(config)
        assert config is not None

    # initial mongo fetch maybe of list, test filtering
    def test_services(self):
        server_category = "CLASSIFICATION"

        # fetch 0-en
        server_type = "test_dummy_1"
        partner_id = 0
        lng = "en"
        name = "dummy_test_1a"
        ip = "test_dummy_1a@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id,
                                                                                                lng)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id == partner_id
        assert classification_config.name == name
        assert classification_config.lang == lng
        assert classification_config.ip == ip

        # fetch 999-en
        server_type = "test_dummy_1"
        partner_id = 999
        lng = "en"
        name = "dummy_test_1b"
        ip = "test_dummy_1b@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id,
                                                                                                lng)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id == partner_id
        assert classification_config.name == name
        assert classification_config.lang == lng
        assert classification_config.ip == ip

        # partner specific config not present, fallback to global partner config
        server_type = "test_dummy_1"
        partner_id = 30
        name = "dummy_test_1a"
        ip = "test_dummy_1a@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id,
                                                                                                lng)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id != partner_id
        assert classification_config.partner_id == 0
        assert classification_config.name == name
        assert classification_config.lang is not None
        assert classification_config.ip == ip

        # fetch multilingual config, should return lang as None
        server_type = "test_dummy_1"
        partner_id = 0
        name = "dummy_test_1c"
        ip = "test_dummy_1c@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id == partner_id
        assert classification_config.name == name
        assert classification_config.lang is None
        assert classification_config.ip == ip

        # fetch specific 'ja' language
        server_type = "test_dummy_1"
        partner_id = 0
        lng = "ja"
        name = "dummy_test_1d"
        ip = "test_dummy_1d@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id,
                                                                                                lng)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id == partner_id
        assert classification_config.name == name
        assert classification_config.lang == lng
        assert classification_config.ip == ip

        # fetch config of non-moderation-like service when language is specified
        server_type = "test_dummy_2"
        partner_id = 0
        lng = "en"
        name = "dummy_test_2"
        ip = "test_dummy_2@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id,
                                                                                                lng)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id == partner_id
        assert classification_config.name == name
        assert classification_config.lang is None
        assert classification_config.ip == ip

        # fetch config if language is not specified, fallback to the only existing config again
        server_type = "test_dummy_2"
        partner_id = 0
        name = "dummy_test_2"
        ip = "test_dummy_2@sprinklr.com"
        classification_config = self.server_configuration_provider.classification_server_config(server_type,
                                                                                                partner_id)
        assert isinstance(classification_config, ServerConfiguration)
        assert classification_config.server_type == server_type
        assert classification_config.server_category == server_category
        assert classification_config.partner_id == partner_id
        assert classification_config.name == name
        assert classification_config.lang is None
        assert classification_config.ip == ip

    def tearDown(self):
        ServerConfiguration.objects(server_type="test_dummy_1", partner_id=0, name="dummy_test_1a").delete()
        ServerConfiguration.objects(server_type="test_dummy_1", partner_id=999, name="dummy_test_1b").delete()
        ServerConfiguration.objects(server_type="test_dummy_1", partner_id=0, name="dummy_test_1c").delete()
        ServerConfiguration.objects(server_type="test_dummy_1", partner_id=0, name="dummy_test_1d").delete()
        ServerConfiguration.objects(server_type="test_dummy_2", partner_id=0, name="dummy_test_2").delete()
        super().tearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2)
