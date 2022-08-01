import functools

from Constants import USER_LEVEL
from components.User import User


def validate_user_rights(level: str):
    def validate_wrapper(func):
        @functools.wraps(func)
        def validate_function(user: User):
            level_value = User.convert_user_lvl_to_value(level)
            if user.admin_level_value >= level_value:
                return func(user)
            else:
                print(f"User: {user.name} does not have the necessary rights")

        return validate_function

    return validate_wrapper