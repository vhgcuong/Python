import os
import shutil
import argparse


def move_folders(src, dst):
    if not os.path.isdir(src):
        raise ValueError(f"Source path '{src}' is not a valid directory.")
    if not os.path.isdir(dst):
        raise ValueError(f"Destination path '{dst}' is not a valid directory.")

    for sub_folder in os.listdir(src):
        old_path = os.path.join(src, sub_folder)
        new_path = os.path.join(dst, sub_folder)
        shutil.move(old_path, new_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move all folders from the source directory to the destination directory.")
    parser.add_argument('--src_path', type=str, required=True, help="Source directory path.")
    parser.add_argument('--dst_path', type=str, required=True, help="Destination directory path.")

    args = parser.parse_args()

    move_folders(args.src_path, args.dst_path)
