# import files_control

# settings, config_admin config_db

# from files_control import read_data, save_data
# from tools import read_data, save_data
from tools.files_control import read_data, save_data, FILE_NAME
# from random import randint

action = input("action: ")

if action == "s":
    save_data(["test", "itStep", "Dimas"])

if action == "r":
    l = read_data()
    print(l)

