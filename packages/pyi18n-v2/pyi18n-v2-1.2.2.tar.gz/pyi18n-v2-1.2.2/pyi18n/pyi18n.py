"""
This module provides the PyI18n class, which is the main localization class
for internationalization and localization in Python. It uses a loader to load
translation files and provides a gettext method to retrieve translations for
a specified locale and path.
"""
from collections import defaultdict
from typing import Optional, Union
from operator import getitem
from functools import reduce
from os.path import exists
from os import getcwd

from .loaders import PyI18nBaseLoader
from .loaders import PyI18nYamlLoader


class PyI18n:
    """ Main i18n localization class

    Attributes:
        available_locales (tuple): list of available locales
        load_path (str): path to locales directory
        _loaded_translations (dict): (class attribute) dictionary
                                    of loaded translations

    Examples:
        >>> from pyi18n import PyI18n
        >>> pyi18n = PyI18n(("en", "jp"), "locales/")
        >>> pyi18n.gettext("en", "hello.world")
        'Hello, world!'
        >>> pyi18n.gettext("jp", "hello.world")
        'こんにちは、世界！'
    """

    _loaded_translations: dict = {}

    def __init__(
        self,
        available_locales: tuple,
        load_path: str = 'locales/',
        loader: Optional[PyI18nBaseLoader] = None
    ) -> None:

        """ Initialize i18n class

        Args:
            available_locales (tuple): list of available locales
            load_path (str): path to locales directory

        Return:
            None
        """

        self.available_locales: tuple = available_locales
        self.load_path: str = f"{getcwd()}/{load_path}"
        self.loader: PyI18nBaseLoader = loader or PyI18nYamlLoader(
            self.load_path)

        self.load_path: str = self.loader.get_path() if self.loader.get_path(
        ) != self.load_path else self.load_path

        self.__pyi18n_init()

    def __pyi18n_init(self) -> None:
        """ validator and loader for translations

        Raises:
            ValueError: if locale is not available in self.available_locales
            FileNotFoundError: if translation file is not found

        """

        if not self.available_locales:
            raise ValueError("available locales must be specified")

        if not exists(self.load_path):
            raise FileNotFoundError(f"{self.load_path} directory "
                                    "not found, please create it")

        self._loaded_translations: dict = self.loader.load(
                                            self.available_locales)

    def gettext(self, locale: str, path: str, **kwargs) -> Union[dict, str]:
        """ Get translation for given locale and path

        Args:
            locale (str): locale to get translation for
            path (str): path to translation
            **kwargs (dict): interpolation variables

        Returns:
            Union[dict, str]: translation str, dict or error message

        Raises:
            ValueError: if locale is not in self.available_locales

        """

        if locale not in self.available_locales:
            raise ValueError(f"locale {locale} not specified "
                             "in available locales")

        founded: Union[dict, str] = self.__find(path, locale)

        if len(kwargs) > 0 and isinstance(founded, str):
            try:
                return founded.format_map(defaultdict(str, **kwargs))
            except KeyError:
                return founded
        return founded

    def __find(self, path: str, locale: str) -> Union[dict, str]:
        """ Find translation for given path and locale

        Args:
            path (str): path to translation
            locale (str): locale to get translation for

        Returns:
            Union[dict, str]: translation str, dict or error message

        """
        try:
            return reduce(getitem, path.split('.'),
                          self._loaded_translations[locale])
        except (KeyError, TypeError):
            return f"missing translation for: {locale}.{path}"

    def get_loader(self) -> PyI18nBaseLoader:
        """ Return loader class

        Returns:
            PyI18nBaseLoader: loader class

        """
        return self.loader
