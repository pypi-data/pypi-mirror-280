import logging
import os
import re
from collections import OrderedDict, namedtuple

from tools_commons.regex_utils import regex_or, punct_regex, newline_regex, space_regex
from tools_commons.misc_utils import run_co_routine
from tools_fs.async_functions import exists, listdir
from tools_fs.session import FileSystemSession


version_pattern = re.compile("version=(.*)")
logger = logging.getLogger(__name__)

IndexKey = namedtuple("IndexKey", ["key", "default_value"])


class AsgardIndex(object):
    """
    Hides the logic to get add, commit, read path for given base path and indexes
    """

    def __init__(self,
                 indexes=None,
                 base_path: str = None,
                 fs: FileSystemSession = None,
                 **kwargs):
        if indexes:
            self.indexes = self.get_index_domain(**indexes)
        if base_path:
            self.base_path = base_path
        if fs:
            self._fs = fs

    def __call__(self, **kwargs):
        """
        todo remove this
        Not truly a callable
        keeping temporarily for backward compatibility..
        """
        return self.__class__(**kwargs, base_path=self.base_path, fs=self._fs)

    def get_index_path(self,
                       *index_prefix,
                       base_path,
                       version=None,
                       append_version: bool = True) -> str:
        """
        :param base_path:
        :param index_prefix: prefix index beyond the base path
        :param version: if not none look for specific version
        :param append_version: if false don't append version
        :return: index path in fs
        """

        path: str = self.get_index_path_without_version(*index_prefix, base_path=base_path)

        if not append_version:
            return path

        if version is None or version == -1:
            _version = str(self.get_version(path))
        else:
            _version = version
        return os.path.join(path, "version=%s" % _version)

    def get_index_path_without_version(self,
                                       *index_prefix,
                                       base_path) -> str:
        """
        :param base_path:
        :param index_prefix: index beyond the base path
        :return: index path in fs
        """
        if index_prefix:
            path = os.path.join(base_path, *index_prefix)
        else:
            path = base_path
        if self.indexes:
            for key, value in self.indexes.items():
                path = os.path.join(path, key + "=" + str(value))
        logger.error("Index path without version - {}".format(path))
        return path

    def get_version(self, path, increment=False):

        """
        :param path: Moneta File system path excluding version index
        :return:
        """

        try:
            if run_co_routine(exists(session=self._fs, path=path)):
                return max(
                    [
                        int(version_pattern.search(_path).group(1).rstrip("/"))
                        for _path in run_co_routine(listdir(session=self._fs, dir_path=path))
                    ]
                ) + (1 if increment else 0)
        except Exception as e:
            logger.error(
                "Setting latest version to 0, if new index this can be ignored. "
                "If not new index, error encountered while getting version is - {}".format(e)
            )
        return 0

    def ensure_index_path(self, *index):
        path = self.get_index_path_without_version(*index, base_path=self.base_path)
        if run_co_routine(exists(self._fs, path)):
            return True
        return False

    # noinspection PyMethodMayBeStatic
    def get_index_keys(self):
        """
        default_value
        - None corresponds to a compulsory attribute
        - "" corresponds to a skip-able attribute
        :return: list of keys for building path
        """
        return [
            IndexKey(key="engine_type", default_value="default"),
            IndexKey(key="engine_id", default_value=None),
            IndexKey(key="language", default_value=None),
            IndexKey(key="vertical", default_value=None),
            IndexKey(key="partner_id", default_value="default"),
            IndexKey(key="model_name", default_value="default"),
            IndexKey(key="model_type", default_value="default"),
            IndexKey(key="stage", default_value="")
        ]

    def get_index_domain(self, **kwargs) -> OrderedDict:
        """
        defines the ordering/cleanup functions
        This would be like a convention for all asgard indexes
        """

        index_keys = self.get_index_keys()
        indices = OrderedDict()

        for index_key in index_keys:
            value = kwargs.get(index_key.key)
            if value is None and index_key.default_value is None:
                # default_value == None => value needs to come from args
                raise ValueError

            if value is not None:
                indices[index_key.key] = value
            elif "" == index_key.default_value:
                # continue on empty default_value
                continue
            elif index_key.default_value is not None:
                # else set default value
                indices[index_key.key] = index_key.default_value
        return indices

    @staticmethod
    def __cleanup(index) -> str:
        if not isinstance(index, str):
            return index
        to_return = index
        if index:
            to_return = re.sub(regex_or(punct_regex, newline_regex), " ", index)
            to_return = to_return.rstrip()
            to_return = re.sub(space_regex, "_", to_return)
        return to_return
