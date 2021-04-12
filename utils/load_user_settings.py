"""
Module for loading user settings and returning them in a dictionary
"""


def return_user_settings() -> dict:
    with open("user_settings.txt", "r") as file:
        data = file.readline().strip().split(',')
    result = {"theme": data[0], "background": data[1]}
    return result

