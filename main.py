from Helper import validate_user_rights
from components.User import User


@validate_user_rights(level="admin")
def print_hi(user: User):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {user.name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    jan_admin = User("Jan", 1, 0)

    print_hi(jan_admin)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
