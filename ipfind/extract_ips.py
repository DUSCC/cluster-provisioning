#!/usr/bin/python3

import re

def is_ip(word):
    if word.count(".") == 3:
        fields = word.split(".")
        for field in fields:
            if not field.isnumeric():
                return False
        return True
    return False

def main():
    filename = "ugh.txt"
    ips = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if is_ip(word):
                    ips.append(word)
    print(ips)


if __name__ == "__main__":
    main()