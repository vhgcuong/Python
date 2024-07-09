import os
import shutil
import argparse


def move_folders(src, dic):
    if os.path.isdir(src) is False or os.path.isdir(dic) is False:
        raise ("Something wrong")
    for sub_folder in os.listdir(src):
        old_path = os.path.join(src, sub_folder)
        shutil.move(old_path, dic)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Move all folders in other folders"""
    )

    parser.add_argument('--src_path', type=str, required=True)
    parser.add_argument('--dic_path', type=str, required=True)
    args = parser.parse_args()

    move_folders(args.src_path, args.dic_path)
