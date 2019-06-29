import re


def process_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line[-1] == '-':
                print(lines[i-2])
                print(lines[i-1])
                print(lines[i])
                print(lines[i+1])
                print(lines[i+2])
                print()