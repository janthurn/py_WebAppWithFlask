
import re
from typing import Union, Dict, Optional


class User(object):

    def __init__(self, name: str, user_id: Union[str, int], admin_level: Optional[Union[int, str]]):

        self._name = name
        self._user_id = user_id

        if admin_level is not None and isinstance(admin_level, str):
            self._admin_level = self.convert_user_lvl_to_value(admin_level)
        else:
            self._admin_level = admin_level or 0

    def __repr__(self):
        return f"User(name: {self.name}, user_id: {self.user_id}, level of rights: {self.admin_level})"

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def admin_level_value(self):
        return self._admin_level

    @property
    def admin_level(self):
        return self.get_readable_admin_level()

    def get_readable_admin_level(self):

        if self._admin_level == 0:
            return "Regular user"

        elif self._admin_level == 1:
            return "Premium user"

        elif self._admin_level == 2:
            return "Admin user"

        else:
            return "Owner"

    @staticmethod
    def convert_user_lvl_to_value(level_str: str) -> int:
        """
        determine the corresponding user level integer value
        :param level_str:
        :return:
        """
        level_mapping = {
            0: r'regular',
            1: r'premium',
            2: r'admin',
            100: r'own',
        }

        for lvl_value, name_pattern in level_mapping.items():
            if re.search(name_pattern, level_str, re.IGNORECASE):
                return lvl_value

        return 0


class UserRegistry(object):
    pass
