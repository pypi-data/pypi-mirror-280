"""
Base Intuition session to be used to drive system behavior via settings
    - the underlying fileSystem and
    - deployment controller client configs; e.g., kubernetes client configs
Handles properties for the service deployment
"""
import os

from tools_commons.singleton import Singleton
from tools_fs.session import FileSystemSession
from .settings import Settings


class IntuitionSession(Singleton):
    def __init__(self, settings: Settings):
        """
        :type settings:
            dict of all configurations
        """
        self._settings: Settings = settings
        self._properties: dict = settings.__dict__
        self._fs: FileSystemSession = FileSystemSession(self._properties["fileSystem"])

    @property
    def properties(self):
        return self._properties

    @property
    def settings(self):
        return self._settings

    @property
    def fs(self):
        return self._fs

    @property
    def aws_key(self):
        return self._properties["fileSystem"]["s3.key"]

    @property
    def aws_secret(self):
        return self._properties["fileSystem"]["s3.secret"]

    def property(self, key, default=None):
        return self.properties[key] if key in self.properties else default


if "INTUITION_SETTINGS_PATH" in os.environ:
    intuition_settings_path = os.environ["INTUITION_SETTINGS_PATH"]
else:
    intuition_settings_path = "/mnt1/config/intuition_settings.yaml"

session = IntuitionSession(Settings(intuition_settings_path))
