"""
the use of this script is to make connection with mongo servers

"""
import logging
import time
import os
import requests
import asyncio
from copy import deepcopy

from pymongo import MongoClient
import mongoengine as me
from mongoengine import fields
from tools_frameworks.cache_refresh.abcs import CacheRefreshable
from tools_frameworks.cache_refresh.api import cache_api

logger = logging.getLogger(__name__)

#Read about all fields here: https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html
default_tls_conf = {
    "tls": False,
    "tlsCAFile": None,
    "tlsCertificateKeyFile": None,
    "tlsCertificateKeyFilePassword": None
}

MONGO_SERVER_CATEGORY = "MONGO"


def mongo_connect(settings):
    """Connect mongoengine to mongo db. This connection is reused everywhere"""

    persistence_config = getattr(
        settings, "PERSISTENCE_CONFIG", getattr(settings, "persistenceConfig")
    )
    missing_conf_msg = "Missing Mongo Server Config!"
    if not persistence_config:
        logger.error(missing_conf_msg)
        raise Exception(missing_conf_msg)

    logger.error("Got config Persistence config: \n" + str(persistence_config))

    mongo_conf = persistence_config.get(
        "mongo_server_config", persistence_config.get("mongoServerConfig")
    )
    if not mongo_conf:
        logger.error(missing_conf_msg)
        raise Exception(missing_conf_msg)

    if not isinstance(mongo_conf, list):
        __connect(mongo_conf)
    else:
        for conf in mongo_conf:
            __connect(conf)
class MongoRefresh(CacheRefreshable):
    """
    It monitors any change in IP configuration and updates Mongo connection via cache refresh
    """
    def __init__(self, key, *args, **kwargs):
        """
        :param key: key to identify the mongo IP in `serverConfiguration` collection
        """
        cache_key = f"{str(key)}"
        super().__init__(cache_key)
        self.key = key
        self.config = kwargs.get("config", {})
        self.event_loop = asyncio.new_event_loop()

    def destroy_cache(self, properties: dict):
        pass

    def rebuild_cache(self, properties: dict):
        try:
            logging.error("Mongo cache refresh rebuilding cache")
            asyncio.set_event_loop(self.event_loop)
            mongo_conf = deepcopy(self.config)

            mongo_db_name, mongo_host, mongo_port, db_alias, tls_conf = mongo_params_helper(mongo_conf)
            logging.info(f"Rebuild_cache with db={mongo_db_name}, host={mongo_host}, port={mongo_port}, alias={db_alias}")

            try:
                me.connect(db=mongo_db_name, host=mongo_host, port=mongo_port, alias=db_alias, **tls_conf)
                logging.error(f"Re-connected to new IP")
            except Exception as exc:
                logger.warning("Error refreshing mongo cache, will retry in 1 sec: %r", exc)
                time.sleep(1)
                me.connect(db=mongo_db_name, host=mongo_host, port=mongo_port, **tls_conf)
            else:
                logger.info("Mongo IP cache refreshed...")
            logging.warning(f"Cache refreshed successfully for {str(self.key)}")
        except Exception as e:
            logging.exception(f"Error in refreshing cache for {str(self.key)} {str(e)}")


def mongo_params_helper(mongo_conf):
    auth_conf = get_auth_conf()
    if not mongo_conf.__contains__("host"):
        mongo_conf, auth_conf = get_mongo_config(mongo_conf)
    mongo_host = mongo_conf["host"]
    mongo_db_name = mongo_conf["name"]
    mongo_port = mongo_conf["port"]
    tls_conf = __parse_tls_fields(mongo_conf)
    tls_conf.update(auth_conf)
    logger.info(
        "Attempting to connect to %s at %s:%s", mongo_db_name, mongo_host, mongo_port
    )

    db_alias = mongo_conf.get('alias', me.DEFAULT_CONNECTION_NAME)
    return mongo_db_name, mongo_host, mongo_port, db_alias, tls_conf

def __connect(mongo_conf):
    # global auth config

    mongo_db_name, mongo_host, mongo_port, db_alias, tls_conf = mongo_params_helper(mongo_conf)
    try:
        me.connect(db=mongo_db_name, host=mongo_host, port=mongo_port, alias=db_alias, **tls_conf)
        logging.info(f"Inside connect db={mongo_db_name}, host={mongo_host}, port={mongo_port}, alias={db_alias}")
    except Exception as exc:
        logger.warning("Error connecting to mongo, will retry in 1 sec: %r", exc)
        time.sleep(1)
        me.connect(db=mongo_db_name, host=mongo_host, port=mongo_port, **tls_conf)
    else:
        if mongo_conf.__contains__("key"):
            mongo_refreshable = MongoRefresh(key=mongo_conf["key"], config=mongo_conf)
            cache_api.watch(mongo_refreshable)
            logging.error(f"Cache api watching {mongo_conf['key']}")
        logger.error("Connected...")


def connect_mongo_client(settings):
    """Connect py mongo client to mongo db. Return the mongo client"""

    persistence_config = getattr(settings, "PERSISTENCE_CONFIG", getattr(settings, "persistenceConfig"))
    missing_conf_msg = "Missing Mongo Server Config!"
    if not persistence_config:
        logger.info(missing_conf_msg)
        raise Exception(missing_conf_msg)

    logger.info("Got config Persistence config: \n" + str(persistence_config))

    mongo_conf = persistence_config.get("mongo_server_config", persistence_config.get("mongoServerConfig"))
    if not mongo_conf:
        logger.info(missing_conf_msg)
        raise Exception(missing_conf_msg)

    if isinstance(mongo_conf, list):
        mongo_client = __connect_mongo_client(mongo_conf[0])
    else:
        mongo_client = __connect_mongo_client(mongo_conf)
    return mongo_client


def __connect_mongo_client(mongo_conf):
    mongo_db_name, mongo_host, mongo_port, _, tls_conf = mongo_params_helper(mongo_conf)
    if "authentication_source" in tls_conf:
        tls_conf.pop("authentication_source")
    try:
        mongo_client = MongoClient(host=mongo_host, port=mongo_port, **tls_conf)
        logger.info(f"Inside connect db={mongo_db_name}, host={mongo_host}, port={mongo_port}")
        return mongo_client
    except Exception as exc:
        logger.warning("Error connecting to mongo, will retry in 1 sec: %r", exc)
        time.sleep(1)
        mongo_client = MongoClient(host=mongo_host, port=mongo_port, **tls_conf)
        return mongo_client


def decrypt_password(encrypted_password, env=os.environ.get("ENV"), decrypt_url=None, retries=2):
    if decrypt_url is None:
        decrypt_url = (
            "http://{}-restricted.sprinklr.com/restricted/v1/encryption/decrypt".format(
                env
            )
        )
    decrypted_pass = requests.put(decrypt_url, data={"input": encrypted_password})
    if decrypted_pass.status_code == 200:
        return decrypted_pass.text.strip('"')
    if decrypted_pass.status_code == 404 and retries > 0:
        return decrypt_password(env, encrypted_password, retries - 1)


def get_mongo_config(prop: dict):
    from tools_config.server_configuration import ServerConfiguration

    mongo_db_name = prop["name"]
    auth_conf = {}
    mongo_conf: ServerConfiguration = ServerConfiguration.objects.get(db_name=mongo_db_name, server_category=MONGO_SERVER_CATEGORY)
    if mongo_conf.auth:
        user = mongo_conf.user
        encrypted_pass = mongo_conf.password
        password = decrypt_password(encrypted_pass)
        auth_conf["username"] = user
        auth_conf["password"] = password
        auth_conf["authentication_source"] = "admin"
    prop["host"] = mongo_conf.url
    prop["port"] = mongo_conf.port
    prop["key"] = mongo_conf.name
    return prop, auth_conf


# TODO: Need to rewrite logic to fetch mongo configs. Create a generic ServiceLocator instance instead
def connect(mongo_conf: dict):
    __connect(mongo_conf)


def get_auth_conf():
    conf = {}
    if "MONGO_USER" in os.environ:
        conf["username"] = os.environ["MONGO_USER"]
    if "MONGO_PASSWORD" in os.environ:
        conf["password"] = os.environ["MONGO_PASSWORD"]
        conf["authentication_source"] = "admin"
    return conf


def __parse_tls_fields(conf: dict) -> dict:
    __tls_conf = default_tls_conf.copy()
    for k,v in conf.items():
        if k in __tls_conf:
            __tls_conf[k] = v
    return __tls_conf


def update_document(document, data_dict):
    def field_value(field, value):

        if field.__class__ in (fields.ListField, fields.SortedListField):
            return [field_value(field.field, item) for item in value]
        if field.__class__ in (
                fields.EmbeddedDocumentField,
                fields.GenericEmbeddedDocumentField,
                fields.ReferenceField,
                fields.GenericReferenceField,
        ):
            return field.document_type(**value)
        else:
            return value

    [
        setattr(document, key, field_value(document._fields[key], value))
        for key, value in data_dict.items()
    ]

    return document
