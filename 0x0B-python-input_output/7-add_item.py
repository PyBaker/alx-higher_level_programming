#!/usr/bin/python3
""" Module ./7-add_item.py
    Adds all arguments to a Python list and saves them to a file
"""


def main():
    """ This will add list of args to json file in JSON format """
    import argparse

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    parser = argparse.ArgumentParser()
    parser.add_argument('forjson', nargs='+')
    args = parser.parse_args()
    # vars will turn Namespace to dict so i'll use the list of args
    data_from_args = vars(args)['forjson']

    try:
        loaded_data = load_from_json_file("add_item.json")
        save_to_json_file(loaded_data + data_from_args, "add_item.json")
    except FileNotFoundError:
        save_to_json_file(data_from_args, "add_item.json")

if __name__ == "__main__":
    main()
