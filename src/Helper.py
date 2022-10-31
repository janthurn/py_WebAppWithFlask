import functools

from src.Constants import USER_LEVEL
from src.components.User import User


def validate_user_rights(level: str = "guest"):
    def validate_wrapper(func):
        # keeps the original function alive in the namespace
        @functools.wraps(func)
        def validate_function(user: User):
            level_value = User.convert_user_lvl_to_value(level)
            if user.admin_level_value >= level_value:
                return func(user)
            else:
                print(f"User: {user.name} does not have the necessary rights")

        return validate_function

    return validate_wrapper
