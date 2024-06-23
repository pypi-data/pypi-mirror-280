import logging
from typing import Optional

from cachetools import cached, TTLCache

from tools_commons.singleton import Singleton
from ..mongo import mongo_utils
from ..session_provider import session
from ..vertical.vertical_config import *


class VerticalConfigStore(Singleton):

    def __init__(self):
        mongo_utils.mongo_connect(session.settings)
        self.logger = logging.getLogger(__name__)

    def save(self,
             partner: int,
             vertical: str,
             display_vertical: Optional[str] = None,
             additional: Optional[dict] = None):
        return VerticalConfig(partner=partner,
                              vertical=vertical,
                              display_vertical=display_vertical,
                              additional=additional).save()

    def bulk_save(self, bulk_data: list):
        config_list = []
        for data in bulk_data:
            config = {}
            if "partner" in data.keys() and data["partner"] is not None:
                config["partner"] = data["partner"]
            else:
                continue

            if "vertical" in data.keys() and data["vertical"] is not None:
                config["vertical"] = data["vertical"]
            else:
                continue

            config["display_vertical"] = None
            if "display_vertical" in data.keys():
                config["display_vertical"] = data["display_vertical"]

            config["additional"] = None
            if "additional" in data.keys():
                config["additional"] = data["additional"]

            config_list.append(self.save(int(config["partner"]),
                                         config["vertical"],
                                         display_vertical=config["display_vertical"],
                                         additional=config["additional"]))

        return config_list

    @cached(cache=TTLCache(maxsize=2048, ttl=60))
    def find(self, partner: int):
        try:
            return VerticalConfig.objects.get(partner=partner)
        except DoesNotExist:
            return None

    @cached(cache=TTLCache(maxsize=2048, ttl=60))
    def bulk_find(self, partner_list: tuple):
        return [self.find(int(partner)) for partner in partner_list]

    def update(self, partner: int,
               vertical: Optional[str] = None,
               display_vertical: Optional[str] = None,
               additional: Optional[dict] = None):
        partner_document = self.find(partner)
        if not partner_document:
            return None

        if vertical is None:
            vertical = partner_document["vertical"]
        if display_vertical is None:
            display_vertical = partner_document["display_vertical"]
        if additional is None:
            additional = partner_document["additional"]

        return partner_document.update(vertical=vertical, display_vertical=display_vertical, additional=additional)

    def bulk_update(self, bulk_data: list):
        updated_config_list = []

        for data in bulk_data:
            config = {}
            if "partner" in data.keys() and data["partner"] is not None:
                config["partner"] = data["partner"]
            else:
                continue

            config["vertical"] = None
            if "vertical" in data.keys():
                config["vertical"] = data["vertical"]

            config["display_vertical"] = None
            if "display_vertical" in data.keys():
                config["display_vertical"] = data["display_vertical"]

            config["additional"] = None
            if "additional" in data.keys():
                config["additional"] = data["additional"]

            updated_config_list.append(self.update(int(config["partner"]),
                                                   config["vertical"],
                                                   display_vertical=config["display_vertical"],
                                                   additional=config["additional"]))

        return updated_config_list

    def remove(self, partner: int):
        partner_document = self.find(partner)
        if partner_document:
            partner_document.delete()

    def bulk_remove(self, partner_list: list):
        for partner in partner_list:
            self.remove(partner)


vertical_store = VerticalConfigStore()