# -*- coding: utf-8 -*-

"""
这个模块的可以让你对 Account / Character 和 WTF 配置文件的模板进行排列组合, 然后一键将你的
配置文件应用到你的客户端中的 WTF 目录下.
"""

import typing as T
import dataclasses
from pathlib_mate import Path
from functools import cached_property

from jinja2 import Template
from wow_acc.api import Account, Character

from ..logger import logger
from ..utils import group_by


@dataclasses.dataclass
class Client:
    r"""
    代表着一个具体魔兽世界客户端. 你必须要制定这个客户端的目录. 然后就可以用各种 method 来
    获取对应的 WTF 配置文件的绝对路径了.

    :param dir: 客户端目录, 根据此目录可以定位其他的目录. 例如 "C:\Program Files\World of Warcraft"
    :param locale: 客户端语种, 例如 enUS, zhCN, zhTW 等.
    """

    dir: Path = dataclasses.field()
    locale: str = dataclasses.field()

    @property
    def dir_wtf(self) -> Path:
        return self.dir / "WTF"

    @property
    def client_config(self) -> Path:
        r"""
        This file stores client level user interface configuration.

        Example: ``C:\...\WTF\Config.wtf``
        """
        return self.dir_wtf / "Config.wtf"

    def _get_acc_dir(self, account: "Account") -> Path:
        r"""
        Example: ``C:\...\WTF\Account\MYACCOUNT``
        """
        return self.dir_wtf / "Account" / account.wtf_account_name

    def get_account_config_cache_wtf(
        self,
        account: "Account",
    ) -> Path:
        r"""
        This file stores account level user interface configuration.

        Example: ``C:\...\WTF\Account\MYACCOUNT\config-cache.wtf``
        """
        return self._get_acc_dir(account) / "config-cache.wtf"

    def get_account_bindings_cache_wtf(
        self,
        account: "Account",
    ) -> Path:  # pragma: no cover
        r"""
        This file stores account level key bindings.

        Example: ``C:\...\WTF\Account\MYACCOUNT\bindings-cache.wtf``
        """
        return self._get_acc_dir(account) / "bindings-cache.wtf"

    def get_account_macros_cache_txt(
        self,
        account: "Account",
    ) -> Path:  # pragma: no cover
        r"""
        This file stores account level macro configurations.

        Example: ``C:\...\WTF\Account\MYACCOUNT\macros-cache.txt``
        """
        return self._get_acc_dir(account) / "macros-cache.txt"

    def get_account_saved_variables(
        self,
        account: "Account",
        file: str,
    ) -> Path:
        r"""
        This file stores per AddOn account level saved variables.

        Example: ``C:\...\WTF\Account\MYACCOUNT\SavedVariables\AtlasLoot.lua``
        """
        return self._get_acc_dir(account) / "SavedVariables" / file

    def _get_char_dir(self, character: "Character") -> Path:
        r"""
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\``
        """
        return (
            self._get_acc_dir(character.account)
            / character.realm_name
            / character.titled_character_name
        )

    def get_character_config_cache_wtf(
        self,
        character: "Character",
    ) -> Path:
        r"""
        This file stores character level user interface configuration.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\config-cache.wtf``
        """
        return self._get_char_dir(character) / "config-cache.wtf"

    def get_character_chat_cache_txt(
        self,
        character: "Character",
    ) -> Path:
        r"""
        This file stores character level chat cache configuration.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\chat-cache.txt``
        """
        return self._get_char_dir(character) / "chat-cache.txt"

    def get_character_bindings_cache_wtf(
        self,
        character: "Character",
    ) -> Path:
        r"""
        This file stores character level key bindings.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\bindings-cache.wtf``
        """
        return self._get_char_dir(character) / "config-cache.wtf"

    def get_character_layout_local_txt(
        self,
        character: "Character",
    ) -> Path:
        r"""
        This file stores character level UI layout configurations.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\layout-local.txt``
        """
        return self._get_char_dir(character) / "layout-local.txt"

    def get_character_addons_txt(
        self,
        character: "Character",
    ) -> Path:
        r"""
        This file stores character level UI AddOns enable / disable configurations.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\AddOns.txt``
        """
        return self._get_char_dir(character) / "AddOns.txt"

    def get_character_macros_cache_txt(
        self,
        character: "Character",
    ) -> Path:  # pragma: no cover
        r"""
        This file stores character level macro configurations.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\macros-cache.txt``
        """
        return self._get_char_dir(character) / "macros-cache.txt"

    def get_character_saved_variables(
        self,
        character: "Character",
        file: str,
    ) -> Path:
        r"""
        This file stores per AddOn character level saved variables.

        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\SavedVariables\tlasLoot.lua``
        """
        return self._get_char_dir(character) / "SavedVariables" / file


@dataclasses.dataclass
class BaseMapping:
    """
    Mapping 是一个 Account / Character 和一个 WTF 配置文件模板的组合.
    """

    file: Path = dataclasses.field()

    @cached_property
    def tpl(self) -> Template:
        """
        Jinja template 对象. 它会被缓存下来以便复用.
        """
        return Template(self.file.read_text(encoding="utf-8"))


@dataclasses.dataclass
class AccLvlMapping(BaseMapping):
    """
    ``Account`` 和一个 WTF 配置文件模板的组合.

    :param acc: `wow_acc.api.Account <https://wow-acc.readthedocs.io/en/latest/wow_acc/model.html#wow_acc.model.Account>`_ 对象.
    :param file: WTF 配置文件模板的绝对路径.
    """

    acc: Account = dataclasses.field()
    file: Path = dataclasses.field()

    @classmethod
    def make_many(
        cls,
        accounts: T.Iterable[Account],
        file: T.Union[Path, T.Iterable[Path]],
    ):
        """
        生成多个 ``Account`` 和 WTF 配置文件模板的组合. 让你写更少的代码.

        :param accounts: Account 对象集合.
        :param file: 单个文件或是多个文件的集合.
        """
        if isinstance(file, Path):
            return [cls(acc=acc, file=file) for acc in accounts]
        else:
            lst = list()
            for acc in accounts:
                for f in file:
                    lst.append(cls(acc=acc, file=f))
            return lst


@dataclasses.dataclass
class CharLvlMapping(BaseMapping):
    """
    ``Character`` 和一个 WTF 配置文件模板的组合.

    :param char: `wow_acc.api.Character <https://wow-acc.readthedocs.io/en/latest/wow_acc/model.html#wow_acc.model.Character>`_ 对象.
    :param file: WTF 配置文件模板的绝对路径.
    """

    char: Character = dataclasses.field()
    file: Path = dataclasses.field()

    @classmethod
    def make_many(
        cls,
        characters: T.Iterable[Character],
        file: T.Union[Path, T.List[Path]],
    ):
        """
        生成多个 ``Character`` 和 WTF 配置文件模板的组合. 让你写更少的代码.

        :param characters: Character 对象集合.
        :param file: 单个文件或是多个文件的集合.
        """
        if isinstance(file, Path):
            return [cls(char=char, file=file) for char in characters]
        else:
            lst = list()
            for char in characters:
                for f in file:
                    lst.append(cls(char=char, file=f))
            return lst


def apply(
    path: Path,
    content: str,
    real_run: bool = False,
    verbose: bool = True,
):
    r"""
    Apply a content to a file (Write to the file in ``World of Warcraft\WTF\...``).

    :param path: The file path to write to.
    :param content: The content to write.
    :param real_run: If True, do not write to the file.
    :param verbose: If True, print log.
    """
    if verbose:
        # 使用 file:// URI 使得可以点击打印在 Console 中的输出直接跳转到文件
        logger.info(f"Write to: file://{path}")
    if real_run:
        try:
            path.write_text(content, encoding="utf-8")
        except FileNotFoundError:
            path.parent.mkdir(parents=True)
            path.write_text(content, encoding="utf-8")


@dataclasses.dataclass
class WtfMapping:
    """
    定义了一个魔兽世界客户端中被管理的所有 WTF 配置文件的设定.

    :param client: :class:`Client` 对象. 有了这个才知道我们要将配置文件写到哪里去.
    :param all_accounts: 所有的 `wow_acc.api.Account <https://wow-acc.readthedocs.io/en/latest/wow_acc/model.html#wow_acc.model.Account>`_ 对象.
        在 render Jinja 模板时会用到.
    :param all_characters: 所有的 `wow_acc.api.Character <https://wow-acc.readthedocs.io/en/latest/wow_acc/model.html#wow_acc.model.Character>`_ 对象.
        在 render Jinja 模板时会用到.
    :param client_config: :meth:`Client.client_config`.
    :param acc_user_interface: :meth:`Client.get_account_config_cache_wtf`.
    :param acc_macros: :meth:`Client.get_account_macros_cache_txt`.
    :param acc_saved_variables: :meth:`Client.get_account_saved_variables`.
    :param char_user_interface: :meth:`Client.get_character_config_cache_wtf`.
    :param char_chat: :meth:`Client.get_character_chat_cache_txt`.
    :param char_keybinding: :meth:`Client.get_character_bindings_cache_wtf`.
    :param char_layout: :meth:`Client.get_character_layout_local_txt`.
    :param char_addons: :meth:`Client.get_character_addons_txt`.
    :param char_macros: :meth:`Client.get_character_macros_cache_txt`.
    :param char_saved_variables: :meth:`Client.get_character_saved_variables`.
    """

    # fmt: off
    client: Client
    all_accounts: T.Iterable[Account]
    all_characters: T.Iterable[Character]

    client_config: Path = dataclasses.field()

    acc_user_interface: T.List[AccLvlMapping] = dataclasses.field(default_factory=list)
    acc_macros: T.List[AccLvlMapping] = dataclasses.field(default_factory=list)
    acc_saved_variables: T.List[AccLvlMapping] = dataclasses.field(default_factory=list)

    char_user_interface: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    char_chat: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    char_keybinding: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    char_layout: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    char_addons: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    char_macros: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    char_saved_variables: T.List[CharLvlMapping] = dataclasses.field(default_factory=list)
    # fmt: on

    @logger.emoji_block(msg="💻{func_name}", emoji="💻")
    def apply_client_config(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.client_config`.
        """
        path_out = self.client.client_config
        tpl = Template(self.client_config.read_text())
        content = tpl.render()
        apply(path_out, content, real_run=real_run)

    def _apply_account_level(
        self,
        mapping_list: T.List[AccLvlMapping],
        getter: T.Callable,
        real_run: bool = False,
    ):
        for account, mappings in group_by(
            mapping_list, get_key=lambda x: x.acc
        ).items():
            for mapping in mappings:
                with logger.nested():
                    logger.ruler(f"start 👤account: {account.wtf_account_name!r}")
                    path_out = getter(mapping.acc)
                    content = mapping.tpl.render(
                        account=mapping.acc,
                        all_accounts=self.all_accounts,
                        all_characters=self.all_characters,
                    )
                    apply(path_out, content, real_run=real_run)
                    logger.ruler(f"end 👤account: {account.wtf_account_name!r}")

    @logger.emoji_block(msg="👤🖼{func_name}", emoji="👤")
    def apply_account_user_interface(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_account_config_cache_wtf`.
        """
        self._apply_account_level(
            mapping_list=self.acc_user_interface,
            getter=self.client.get_account_config_cache_wtf,
            real_run=real_run,
        )

    @logger.emoji_block(msg="👤🎮{func_name}", emoji="👤")
    def apply_account_macros(self, real_run: bool = False):  # pragma: no cover
        """
        将配置文件写入到 :meth:`Client.get_account_macros_cache_txt`.
        """
        self._apply_account_level(
            mapping_list=self.acc_macros,
            getter=self.client.get_account_macros_cache_txt,
            real_run=real_run,
        )

    @logger.emoji_block(msg="👤🔢{func_name}", emoji="👤")
    def apply_account_saved_variables(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_account_saved_variables`.
        """
        for mapping in self.acc_saved_variables:
            path_out = self.client.get_account_saved_variables(
                mapping.acc,
                mapping.file.basename,
            )
            content = mapping.tpl.render(
                account=mapping.acc,
                all_accounts=self.all_accounts,
                all_characters=self.all_characters,
            )
            apply(path_out, content, real_run=real_run)

    def _apply_character_level(
        self,
        mapping_list: T.List[CharLvlMapping],
        getter: T.Callable,
        real_run: bool = False,
    ):
        for account, mappings in group_by(
            mapping_list, get_key=lambda x: x.char.account
        ).items():
            for mapping in mappings:
                with logger.nested():
                    logger.ruler(
                        f"start characters in 👤account: {account.wtf_account_name!r}"
                    )
                    path_out = getter(mapping.char)
                    content = mapping.tpl.render(
                        character=mapping.char,
                        all_accounts=self.all_accounts,
                        all_characters=self.all_characters,
                    )
                    apply(path_out, content, real_run=real_run)
                    logger.ruler(
                        f"end characters in 👤account: {account.wtf_account_name!r}"
                    )

    @logger.emoji_block(msg="🧙🖼{func_name}", emoji="🧙")
    def apply_character_user_interface(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_character_config_cache_wtf`.
        """
        self._apply_character_level(
            mapping_list=self.char_user_interface,
            getter=self.client.get_character_config_cache_wtf,
            real_run=real_run,
        )

    @logger.emoji_block(msg="🧙💬{func_name}", emoji="🧙")
    def apply_character_chat(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_character_chat_cache_txt`.
        """
        self._apply_character_level(
            mapping_list=self.char_chat,
            getter=self.client.get_character_chat_cache_txt,
            real_run=real_run,
        )

    @logger.emoji_block(msg="🧙🎹{func_name}", emoji="🧙")
    def apply_character_keybinding(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_character_bindings_cache_wtf`.
        """
        self._apply_character_level(
            mapping_list=self.char_keybinding,
            getter=self.client.get_character_bindings_cache_wtf,
            real_run=real_run,
        )

    @logger.emoji_block(msg="🧙📐{func_name}", emoji="🧙")
    def apply_character_layout(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_character_layout_local_txt`.
        """
        self._apply_character_level(
            mapping_list=self.char_layout,
            getter=self.client.get_character_layout_local_txt,
            real_run=real_run,
        )

    @logger.emoji_block(msg="🧙🧩{func_name}", emoji="🧙")
    def apply_character_addons(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_character_addons_txt`.
        """
        self._apply_character_level(
            mapping_list=self.char_addons,
            getter=self.client.get_character_addons_txt,
            real_run=real_run,
        )

    @logger.emoji_block(msg="🧙🎮{func_name}", emoji="🧙")
    def apply_character_macros(self, real_run: bool = False):  # pragma: no cover
        """
        将配置文件写入到 :meth:`Client.get_character_macros_cache_txt`.
        """
        self._apply_character_level(
            mapping_list=self.char_macros,
            getter=self.client.get_character_macros_cache_txt,
            real_run=real_run,
        )

    @logger.emoji_block(msg="🧙🔢{func_name}", emoji="🧙")
    def apply_character_saved_variables(self, real_run: bool = False):
        """
        将配置文件写入到 :meth:`Client.get_character_saved_variables`.
        """
        for mapping in self.char_saved_variables:
            path_out = self.client.get_character_saved_variables(
                mapping.char,
                mapping.file.basename,
            )
            content = mapping.tpl.render(
                character=mapping.char,
                all_accounts=self.all_accounts,
                all_characters=self.all_characters,
            )
            apply(path_out, content, real_run=real_run)
