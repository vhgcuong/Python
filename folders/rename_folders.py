import os
import argparse
from datetime import datetime


def convert_string_to_date(date_string):
    try:
        date_object = datetime.strptime(date_string, "%d_%m_%Y").date()
        return date_object
    except ValueError:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""The path to the directory
                containing the folders to be rename
                ex: 17_04_2024 ---> 2024_04_17"""
    )

    parser.add_argument('--path', type=str, required=True)
    args = parser.parse_args()

    with os.scandir(path=args.path) as itr:
        for entry in itr:
            if entry.is_dir():
                date_object = convert_string_to_date(entry.name)
                if date_object is None:
                    continue
                lst = entry.path.split('/')
                lst[-1] = date_object.strftime("%Y_%m_%d")
                os.rename(entry.path, '/'.join(lst))
