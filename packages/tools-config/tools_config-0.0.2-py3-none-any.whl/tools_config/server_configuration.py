import collections
import logging
from mongoengine import *

# The serverConfiguration provider - it looks up the server properties like kafka config from the mongo service registry
# This is client-side service locator
# Currently support kafka_config for a tier

# This utility can be and should be moved out of visual when this is used anywhere else
# and other service locator function is added

DEFAULT = "DEFAULT"
DEFAULT_CONTENT_TYPE = "image"
DEFAULT_MODULE = "LISTENING"  # visual
GLOBAL_PARTNER = 0

INPUT_FEEDS_TYPE = "input_feeds"
OUTPUT_FEEDS_TYPE = "output_feeds"

SEEING_KAFKA_TIER_TYPE = "SEEING_KAFKA"

# Server Categories
KAFKA_FEED_SERVER_CATEGORY = "KAFKA_FEED_SERVER_CONFIG"
ELASTIC_SEARCH = "ELASTIC_SEARCH"
ELASTICSEARCH_SERVER = "ELASTICSEARCH_SERVER"
CLASSIFICATION_SERVER_CATEGORY = "CLASSIFICATION"
MONGO = "MONGO"
MQTT = "MQTT"
REDIS = "REDIS"
INFLUX = "INFLUX"

# Server Types
ES_COMMUNITY = "COMMUNITY"
ES_COMMUNITY_SERVER_TYPE_MAP = {
    "user": "COMMUNITY_USER",
    "topic": "COMMUNITY_TOPIC",
    "message": "COMMUNITY_MESSAGE"
}

# Additional field
INTERNAL_K8_HOST = "k8sHost"
INTERNAL_K8_PORT = "k8sPort"
# Declaring namedtuple()
# Output case-class dto
KafkaConfig = collections.namedtuple(
    "KafkaConfig",
    [
        "input_topic_names",
        "input_kafka_brokers",
        "output_topic_names",
        "output_kafka_brokers",
    ],
)

ESReadConfig = collections.namedtuple(
    "ESReadConfig", (
        "ip",
        "port",
        "read_indexes"
    )
)


class ClassificationEngineConfig(Document):
    """
    The classification engine config is global and unique per engine_id
    This holds metadata regarding engine - for engine request processors as well as config managers

    Do not change any string literal  variables
    """

    engine_id = StringField(required=True, db_field="engineId")
    engine_type = StringField(required=True, db_field="engineType")
    content_type = StringField(required=True, db_field="contentType")
    module = StringField(required=True, db_field="module")
    submit_to_classifier_in_sync = BooleanField(required=True, db_field="submitToClassifierInSync")

    meta = {"collection": "classificationEngineConfig", "strict": False, 'db_alias': 'spr-global'}


class SeeingProvisioningConfig(DynamicDocument):
    """
        SeeingProvisioningConfig for partnerIds.
    """
    meta = {"collection": "seeingProvisioningConfig", "strict": False, 'db_alias': 'spr-global'}


class TierConfiguration(Document):
    """
    The tier is a logical grouping of partner ids
    The additional map has the tier metadata - like kafka topic names for the tier.

    Do not change any string literal  variables
    """

    name = StringField(required=True, db_field="name")
    type = StringField(required=True, db_field="type")
    partner_ids = SortedListField(LongField(required=True, db_field="partnerIds"))
    additional = DictField(db_field="additional")

    meta = {"collection": "tierConfiguration", "strict": False, 'db_alias': 'spr-global'}


class InternalServerConfiguration(Document):
    server_category = StringField(required=True, db_field="serverCategory")
    server_type = StringField(required=True, db_field="serverType")
    ip = StringField(db_field="ip")
    port = LongField(db_field="port")
    name = StringField(required=True, db_field="name")

    additional = DictField(db_field="additional")

    meta = {"collection": "internalServerConfiguration", "strict": False, 'db_alias': 'spr-global'}


class ServerConfiguration(DynamicDocument):
    """
    Generic server configuration object - this represents service location
    Maps service discovery query filter with its configs

    Do not change any string literal variables
    """

    partner_id = LongField(required=True, db_field="partnerId")
    client_id = LongField(required=True, db_field="clientId")
    server_category = StringField(required=True, db_field="serverCategory")
    server_type = StringField(required=True, db_field="serverType")
    name = StringField(required=True, db_field="name")
    ip = StringField(db_field="ip")
    port = LongField(db_field="port")
    lang = StringField(db_field="lang", default=None)
    source_type = StringField(db_field="sourceType", default=None)
    url = StringField(db_field="url")
    db_name = StringField(db_field="dbName")
    kafka_topic_name = StringField(db_field="kafkaTopicName")
    feed_name = StringField(db_field="feedName")
    topic_name = StringField(db_field="topicName")

    kafka_cluster_id = StringField(db_field="kafkaClusterId")
    bootstrap_servers = StringField(db_field="bootstrapServers")
    brokers = StringField(db_field="brokers")

    producer_config_map_json = StringField(
        db_field="producerConfigMapJson"
    )
    consumer_config_map_json = StringField(
        db_field="consumerConfigMapJson"
    )

    # For mongo config
    tls = BooleanField(db_field="tlsEnabled", default=False, required=False)
    auth = BooleanField(db_field="authEnabled", default=False, required=False)
    user = StringField(db_field="user", required=False)
    password = StringField(db_field="password", required=False)

    additional = DictField(db_field="additional")

    meta = {"collection": "serverConfiguration", "strict": False, 'db_alias': 'spr-global'}


class ESTimeShardInfo(DynamicDocument):
    """
        ES shard info for time shard indexes
        esTimeShardInfo is actually in dmongo for partner.
        Current implementation only works for global level es repos with partner = 0
        #TODO: Handle time sharded info  at partner mongo
    """

    meta = {"collection": "eSTimeShardInfo", "strict": False, 'db_alias': 'spr-global'}


class ESTimeShardVersionInfo(DynamicDocument):
    """
        ES shard info for time shard indexes
    """

    meta = {"collection": "eSTimeShardVersionInfo", "strict": False, 'db_alias': 'spr-global'}


class ESCommunityConfig(DynamicDocument):
    server_type = StringField(required=True, db_field="serverType")
    partner_id = LongField(required=True, db_field="partnerId")
    name = StringField(required=True, db_field="name")
    server_category = StringField(required=True, db_field="serverCategory")
    deleted = BooleanField(required=True, default=True, db_field="deleted")
    index_name = StringField(required=True, db_field="indexName")
    meta = {"collection": "serverConfiguration", "strict": False, 'db_alias': ES_COMMUNITY}


class PartnerLevelConfigBean(DynamicDocument):
    config = DictField(required=True, db_field="config")
    meta = {"collection": "partnerLevelConfigBean", "strict": False, 'db_alias': 'spr-global'}


class VoiceTTSASRConfiguration(DynamicDocument):
    configurations = DictField(required=True, db_field="configurations")
    partner_id = DictField(required=True, db_field="partnerId")
    meta = {
        "collection": "voiceTTSASRConfiguration",
        "strict": False,
        "db_alias": "spr-global",
    }


class ConfigurationProvider:
    def __init__(self, settings):
        from .mongo import mongo_utils
        mongo_utils.mongo_connect(settings)

    def get_classification_engine_config(self, engine_id):
        try:
            classification_config = ClassificationEngineConfig.objects.get(engine_id=engine_id)
        except DoesNotExist:
            logging.exception(
                "Error while fetching classification engine configuration for engine : {}".format(str(engine_id)))
            return None
        return classification_config

    def get_seeing_provisioning_config(self, partner_ids):
        seeing_provisioning_configs = SeeingProvisioningConfig.objects(partnerId__in=partner_ids)
        return seeing_provisioning_configs

    def get_all_seeing_provisioning_configs(self):
        return SeeingProvisioningConfig.objects()


class ServerConfigurationProvider:
    """
    This actually should be a contract and there should be one implementation for SprinklrServiceConfigurationProvider
    TODO: rethink service discovery contract altogether for asgard

    This is a service locator logic - implements service specific config -> kafka_config() for kafka cluster
    """

    def __init__(self, settings):
        from tools_config.mongo import mongo_utils
        self.settings = settings
        mongo_utils.mongo_connect(settings)

    @staticmethod
    def kafka_feed_config(kafka_cluster_id):
        kafka_feed_configs = ServerConfiguration.objects(
            server_category="KAFKA_FEED_SERVER_CONFIG",
            server_type="KAFKA_FEED_SERVER_CONFIG",
            kafka_cluster_id=kafka_cluster_id
        )
        if not kafka_feed_configs or not len(kafka_feed_configs):
            raise AttributeError("kafka feed config not found")

        return kafka_feed_configs[0]

    @staticmethod
    def kafka_config_multiple_sources(engine_id, tier, sources: list = None):
        if sources is None or len(sources) == 0:
            sources = ["NA"]

        input_feeds = dict()
        output_feeds = dict()
        input_kafka_brokers = None
        output_kafka_brokers = None
        for source in sources:
            kafka_config: KafkaConfig = ServerConfigurationProvider.kafka_config(engine_id, tier, source)
            input_feeds[source] = kafka_config.input_topic_names
            output_feeds[source] = kafka_config.output_topic_names
            # assuming single cluster
            input_kafka_brokers = kafka_config.input_kafka_brokers
            output_kafka_brokers = kafka_config.output_kafka_brokers
        return KafkaConfig(
            input_feeds, input_kafka_brokers, output_feeds, output_kafka_brokers
        )

    @staticmethod
    def kafka_config(engine_id, tier, source=None):
        """
        Discovers kafka cluster details for the tier (and the engine of the container):
        1. Load tier config to find the kafka topic names
        2. Load kafka_feed_config from server configuration to find the kafka cluster id
        3. Load kafka_feed_server_config from server configuration to find the broker ip for the cluster id
        - assumes there will be unique broker list for the give cluster id

        :param engine_id: engine_id of the deployment
        :param tier: the tier
        :param source: the source of message, required to pick different kafka queues based on source information
        :return: named tuple of KafkaConfig - containing input and output feeds' details
        """

        def get_classification_config(engine_id):
            classification_config = ClassificationEngineConfig.objects.get(
                engine_id=engine_id
            )
            assert classification_config is not None, (
                    "Classification Config for " + engine_id + " is not present"
            )
            return classification_config

        def get_supported_module(engine_id):
            classification_config = get_classification_config(engine_id)
            return classification_config.module or DEFAULT_MODULE

        def get_supported_content(engine_id):
            classification_config = get_classification_config(engine_id)
            return classification_config.content_type or DEFAULT_CONTENT_TYPE

        def get_feed_names(module, feed_type, source_type=None):
            if module is None:
                return "%s_%s" % (source_type, feed_type)
            elif source_type is None:
                return "%s_%s" % (module, feed_type)
            else:
                return "%s_%s_%s" % (module, source_type, feed_type)

        def get_input_feeds_with_fallback(module, source_type):

            # 1st level - Search for feeds with module and source type
            feed_field = get_feed_names(module, INPUT_FEEDS_TYPE, source_type)
            if feed_field in additional:
                return additional.get(feed_field).split(",")

            # 2nd level fallback - Search for feeds with source type
            feed_field = get_feed_names(None, INPUT_FEEDS_TYPE, source_type)
            if feed_field in additional:
                return additional.get(feed_field).split(",")

            # 3rd level fallback - Search for feeds with only module type
            feed_field = get_feed_names(module, INPUT_FEEDS_TYPE, None)
            if feed_field in additional:
                return additional.get(feed_field).split(",")

        def get_output_feeds_with_fallback(module, source_type):

            # 1st level - Search for feeds with source type
            feed_field = get_feed_names(None, OUTPUT_FEEDS_TYPE, source_type)
            if feed_field in additional:
                return additional.get(feed_field).split(",")

            # 2nd level fallback - Search for feeds with module and source type
            feed_field = get_feed_names(module, OUTPUT_FEEDS_TYPE, source_type)
            if feed_field in additional:
                return additional.get(feed_field).split(",")

            # 3rd level fallback - Search for feeds with only module type
            feed_field = get_feed_names(module, OUTPUT_FEEDS_TYPE, None)
            if feed_field in additional:
                return additional.get(feed_field).split(",")


        tier_config = TierConfiguration.objects.get(
            name=tier, type=("%s" % SEEING_KAFKA_TIER_TYPE)
        )
        additional = tier_config.additional
        engine_module = get_supported_module(engine_id)

        input_feeds = get_input_feeds_with_fallback(engine_module, source_type=source)
        output_feeds = get_output_feeds_with_fallback(engine_module, source_type=source)

        feed_list = []
        feed_list.extend(input_feeds)
        feed_list.extend(output_feeds)

        kafka_feed_configs = ServerConfiguration.objects.filter(
            Q(feed_name__in=feed_list) | Q(kafka_topic_name__in=feed_list)
        )
        cluster_ids = set(map(lambda x: x.kafka_cluster_id, kafka_feed_configs))

        kafka_server_configs = ServerConfiguration.objects(
            server_category=("%s" % KAFKA_FEED_SERVER_CATEGORY),
            kafka_cluster_id__in=list(cluster_ids),
        )
        cluster_id_brokers = {}
        for conf in kafka_server_configs:
            cluster_id = conf.kafka_cluster_id
            cluster_id_brokers[cluster_id] = conf.brokers


        input_kafka_brokers = None
        output_kafka_brokers = None
        for config in kafka_feed_configs:
            cluster_id = config.kafka_cluster_id
            feed = config.feed_name or config.kafka_topic_name
            # overriding input_kafka_brokers & output_kafka_brokers - assuming there will be only one unique cluster id
            if feed in input_feeds:
                input_kafka_brokers = cluster_id_brokers[cluster_id]
            elif feed in output_feeds:
                output_kafka_brokers = cluster_id_brokers[cluster_id]
            else:
                raise ValueError("unexpected topic feed name: " + feed)
        if len(input_feeds) <= 0 or len(output_feeds) <= 0:
            raise RuntimeError(
                "input_feeds and output_feeds must exists for tier: " + str(tier_config)
            )
        if input_kafka_brokers is None or output_kafka_brokers is None:
            raise RuntimeError(
                "unable to find kafka server config for brokers for feeds: "
                + str(feed_list)
            )
        return KafkaConfig(
            input_feeds, input_kafka_brokers, output_feeds, output_kafka_brokers
        )

    @classmethod
    def es_config_helper(cls, server_type, config, current_sharding_version,
                         time_sharded=False, use_host_server_config=False):
        if time_sharded:
            # Only handle partner_id=0 for now
            read_indexes = [record._data.get('shardIndexName') for record in
                            ESTimeShardInfo.objects(esServerType=server_type,
                                                    shardingVersion=current_sharding_version)]
        else:
            read_indexes = [config._data.get('readIndexName') or config._data.get('index_name')]
        cluster_name = config._data.get('clusterName')
        if config._data.get('hostPortCsv') and not use_host_server_config:
            host_port = config._data.get('hostPortCsv').split(",")[0]
            return ESReadConfig(ip=host_port.split(":")[0], port=host_port.split(":")[1], read_indexes=read_indexes)
        else:
            config = ServerConfiguration.objects(serverCategory=ELASTICSEARCH_SERVER, clusterName=cluster_name).first()
            host_port = config._data.get('hostPortCsv').split(",")[0]
            return ESReadConfig(ip=host_port.split(":")[0], port=host_port.split(":")[1], read_indexes=read_indexes)

    # noinspection PyProtectedMember
    @staticmethod
    def es_config(server_type, partner_id=0, time_sharded=False, use_host_server_config=False) -> ESReadConfig:
        current_sharding_version = DEFAULT
        shard_version_info = ESTimeShardVersionInfo.objects(esServerType=server_type, partnerId=partner_id)
        if shard_version_info:
            current_sharding_version = shard_version_info.first()._data.get('currentShardingVersion')

        config = ServerConfiguration.objects(serverCategory=ELASTIC_SEARCH, serverType=server_type,
                                             partnerId=partner_id, shardVersion=current_sharding_version).first()

        return ServerConfigurationProvider.es_config_helper(
            server_type=server_type,
            config=config,
            current_sharding_version=current_sharding_version,
            time_sharded=time_sharded,
            use_host_server_config=use_host_server_config
        )

    @staticmethod
    def es_community_config(es_server_type, partner_id=0, time_sharded=False, use_host_server_config=False):
        from tools_config.mongo import mongo_utils
        config = ServerConfiguration.objects(server_type=ES_COMMUNITY, partner_id=partner_id).first()
        url = config._data.get("url")
        url = url.split(",")[0]
        mongo_conf = {
            "name": config._data.get("dbName") or config._data.get("db_name"),
            "host": url.split(":")[0],
            "port": int(url.split(":")[1]),
            "alias": ES_COMMUNITY
        }
        mongo_utils.connect(mongo_conf)
        es_server_type = ES_COMMUNITY_SERVER_TYPE_MAP.get(es_server_type, es_server_type)
        config = ESCommunityConfig.objects(
            server_type=es_server_type,
            deleted=False).first()
        logging.info("ES community config: {}".format(config._data))
        return ServerConfigurationProvider.es_config_helper(
            server_type=es_server_type,
            config=config,
            current_sharding_version=DEFAULT,
            time_sharded=time_sharded,
            use_host_server_config=use_host_server_config
        )

    @staticmethod
    def classification_server_config(engine_id, partner_id, lng=None):
        try:
            # using '.objects' instead of '.objects.get' returns 'mongoengine.QuerySet' since mapping is no longer unique
            classification_configs = ServerConfiguration.objects(
                server_category=("%s" % CLASSIFICATION_SERVER_CATEGORY),
                server_type=engine_id,
                partner_id=partner_id
            )
            # fallback to global config if partner specific config not present
            if not classification_configs:
                classification_configs = ServerConfiguration.objects(
                    server_category=("%s" % CLASSIFICATION_SERVER_CATEGORY),
                    server_type=engine_id,
                    partner_id=GLOBAL_PARTNER
                )

            # fallback to partner agnostic engines if partner specific config not present
            if not classification_configs or not len(classification_configs):
                classification_configs = ServerConfiguration.objects(
                    server_category=("%s" % CLASSIFICATION_SERVER_CATEGORY),
                    server_type=engine_id
                )

            classification_config = None
            for configuration in classification_configs:
                if not configuration.lang:
                    classification_config = configuration
                if configuration.lang == lng:
                    classification_config = configuration
                    break

            if classification_config:
                if INTERNAL_K8_HOST in classification_config.additional.keys():
                    classification_config.ip = classification_config.additional[INTERNAL_K8_HOST]
                if INTERNAL_K8_PORT in classification_config.additional.keys():
                    classification_config.port = int(classification_config.additional[INTERNAL_K8_PORT])
        except DoesNotExist:
            logging.exception("Error while fetching classification server configuration")
            return None
        return classification_config

    @staticmethod
    def mqtt_server_config(server_type, partner_id):
        try:
            mqtt_config = ServerConfiguration.objects.get(
                server_category=("%s" % MQTT),
                server_type=server_type,
                partner_id=partner_id
            )
        except DoesNotExist:
            logging.exception("Error while fetching mqtt server configuration")
            return None
        return mqtt_config

    @staticmethod
    def redis_server_config(server_type, partner_id, **kwargs):
        try:
            redis_config = ServerConfiguration.objects.get(
                server_category=REDIS,
                partner_id=partner_id,
                server_type=server_type,
                **kwargs
            )
            redis_config = redis_config.to_mongo().to_dict()
        except DoesNotExist:
            logging.exception("Error while fetching redis server configuration")
            return None
        return redis_config

    @staticmethod
    def influxdb_server_config(server_type, **kwargs):
        try:
            influxdb_config = ServerConfiguration.objects.get(
                server_category=INFLUX,
                server_type=server_type,
                **kwargs
            )
            influxdb_config = influxdb_config.to_mongo().to_dict()
        except DoesNotExist:
            logging.exception("Error while fetching Influx server configuration")
            return None
        return influxdb_config

    @staticmethod
    def mongodb_server_config(server_type, partner_id):
        try:
            mongo_config = ServerConfiguration.objects.get(
                server_category=("%s" % MONGO),
                server_type=server_type,
                partner_id=partner_id
            )
        except DoesNotExist:
            logging.exception("Error while fetching mongo server configuration")
            return None
        return mongo_config

    @staticmethod
    def classification_server_configs():
        return ServerConfiguration.objects()
    
    @staticmethod
    def voice_server_configs():
        voice_configs = PartnerLevelConfigBean.objects(config__module="VOICE_TTS_CONFIG")
        return voice_configs

    @staticmethod
    def tts_asr_server_configurations():
        tts_asr_server_configurations = VoiceTTSASRConfiguration.objects()
        return tts_asr_server_configurations


class InternalServerConfigStore:

    def __init__(self, settings):
        from tools_config.mongo import mongo_utils
        mongo_utils.mongo_connect(settings)

    @staticmethod
    def add_server_configuration(name: str, server_category: str, server_type: str, ip: str, port: int):
        return InternalServerConfiguration(name=name,
                                           server_category=server_category,
                                           server_type=server_type,
                                           ip=ip,
                                           port=port).save()

    @staticmethod
    def get_server_configuration_by_name(name):
        try:
            return InternalServerConfiguration.objects.get(name=name)
        except DoesNotExist:
            return None
