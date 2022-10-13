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

def extract_ips(filename):
    ips = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if is_ip(word):
                    ips.append(word)
    return ips

def gen_hostfile(ips, outname):
    with open(outname, "w+") as ofile:
        for ip in ips:
            line = f"{ip} slots=20 max_slots=20\n"
            ofile.write(line)

def main():
    filename = "ugh.txt"
    outname = "hostfile"
    ips = extract_ips(filename)
    gen_hostfile(ips, outname)
    print(ips)


if __name__ == "__main__":
    main()