# import files_control
# from files_control import read_data, save_data
from tools import read_data, save_data
#from tools.files_control import read_data, save_data
# from random import randint

action = input("action: ")

if action == "s":
    save_data(["test", "itStep", "Dimas"])

if action == "r":
    l = read_data()
    print(l)

