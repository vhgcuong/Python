import os
import re
import shutil
import argparse
from datetime import datetime


def convert_string_to_date(date_string):
    try:
        date_object = datetime.strptime(date_string, "%d_%m_%Y").date()
        return date_object
    except ValueError:
        return None


def move_files(path):
    with os.scandir(path) as itr:
        for entry in itr:
            file_name = entry.name
            pattern = r"\d{4}-\d{2}-\d{2}"
            match = re.search(pattern, file_name)
            if match:
                date_time = match.group()
                path_new = f"{os.path.join(path, date_time)}"
                if os.path.isdir(path_new) is False:
                    os.mkdir(path=path_new)
                shutil.move(entry.path, f"{os.path.join(path, date_time)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""The path to the directory
                containing the folders to be rename
                ex: 17_04_2024 ---> 2024_04_17"""
    )

    parser.add_argument('--path', type=str, required=True)
    args = parser.parse_args()

    move_files(args.path)
