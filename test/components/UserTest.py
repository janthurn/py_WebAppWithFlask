
import unittest
from unittest import mock
from src.components.User import User


class UserTest(unittest.TestCase):

    def test_init(self):

        user = User("name", 1234, 0)
        self.assertEqual("name", user._name)
        self.assertEqual(1234, user._user_id)
        self.assertEqual(0, user._admin_level)

        user = User("name", 1234, "Admin")
        self.assertEqual("name", user._name)
        self.assertEqual(1234, user._user_id)
        self.assertEqual(2, user._admin_level)

    def test_get_readable_admin_level(self):

        user = User("name", 1234, 0)
        self.assertEqual("Regular user", user.get_readable_admin_level())

        user = User("name", 1234, 1)
        self.assertEqual("Premium user", user.get_readable_admin_level())

        user = User("name", 1234, 2)
        self.assertEqual("Admin user", user.get_readable_admin_level())

        user = User("name", 1234, 100)

        self.assertEqual("Owner", user.get_readable_admin_level())

    def test_properties(self):

        user = User("name", 1234, 100)

        with mock.patch.object(user, "get_readable_admin_level", return_value="master" ) as mock_get_readable:
            self.assertEqual("master", user.admin_level)
            self.assertEqual(1234, user.user_id)
            self.assertEqual("name", user.name)
            self.assertEqual(100, user.admin_level_value)

            mock_get_readable.assert_called_once()

    def test_convert_user_lvl_to_value(self):

        user = User("name", 1234, 100)

        self.assertEqual(0, user.convert_user_lvl_to_value("Regular user"))
        self.assertEqual(1, user.convert_user_lvl_to_value("Premium user"))
        self.assertEqual(2, user.convert_user_lvl_to_value("Admin user"))
        self.assertEqual(100, user.convert_user_lvl_to_value("Owner"))
        self.assertEqual(0, user.convert_user_lvl_to_value("JoeSchmo"))
