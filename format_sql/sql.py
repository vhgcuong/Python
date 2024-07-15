import os
import argparse
from datetime import datetime


def write_file(content):
    path_file = os.path.join(os.curdir, f"""generate_{datetime.now().strftime('%Y%m%d%H%m%s')}.sql""")
    with open(path_file, 'x') as action:
        for item in content:
            action.writelines(item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument('--path', type=str, required=True, help="Source directory path.")

    args = parser.parse_args()
    path = args.path

    lines = []
    with open(path, 'r+') as f:
        text = f.readlines()
        for line in text:
            rep_line = line.replace('),(', '), \n(')
            lines.append(rep_line)

    write_file(lines)
