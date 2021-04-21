"""
Module for loading user settings and returning them in a dictionary
"""


def return_user_settings() -> dict:
    try:
        with open("user_settings.txt", "r") as file:
            data = file.readline().strip().split(',')
        result = {"theme": data[0], "background": data[1]}
        return result
    except FileNotFoundError:
        f = open("user_settings.txt", "w")
        f.write("light,classic")
        f.close()
        return {"theme": 'light', "background": 'classic'}


def write_user_settings(settings: dict):
    f = open("user_settings.txt", "w")
    f.write(f"{settings['theme']},{settings['background']}")
    f.close()
    return {"theme": 'light', "background": 'classic'}


