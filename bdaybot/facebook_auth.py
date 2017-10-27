import getpass


def login():
    test_login = "botbday@gmail.com"
    test_password = "12345679"
    login = input("Provide your login: ")
    password = getpass.getpass("Provide your password:")

    if login and password:
        return {"login": login, "password": password}
    else:
        return {"login": test_login, "password": test_password}
