from src.Helper import validate_user_rights
from src.components.User import User


@validate_user_rights(level="admin")
def print_hi(user: User):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {user.name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    jan_admin = User(name="Jan",
                     user_id=1,
                     admin_level="admin")

    print_hi(jan_admin)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
