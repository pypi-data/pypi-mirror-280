import logging
import os


empty = object()
logger = logging.getLogger(__name__)


class Settings:
    """
    # Arguments
        file_path:  loads settings as a dict from a .yaml file
        kwargs:     can override with kwargs
    """

    def __init__(self, file_path=None, **template_args):
        if file_path:
            self.__load_config(file_path, **template_args)
        else:
            filename = os.path.join(
                os.path.dirname(__file__), "default_settings.yaml"
            )
            self.__load_config(filename, **template_args)

    def load(self, filepath):
        self.__load_config(filepath)

    def __load_config(self, filepath, **template_args):
        self.__update_self(Settings.__get_config(filepath, **template_args))

    def __update_self(self, config):
        self.__dict__.update(config)

    def __getattribute__(self, name: str):
        return object.__getattribute__(self, name)

    @staticmethod
    def __get_config(filepath, **template_args):
        from tools_fs.utils.yaml_loader import load_yaml
        return load_yaml(filepath, **template_args)
