#!/usr/bin/python3
import re


regex = re.compile(r"compute-(\d+).*\s*((?:\d+\.?){4})")
with open("input.txt", 'r') as f:
    nodes = {int(node): ip for node, ip in re.findall(regex, f.read())}


with open("src/hosts", 'w') as f:
    f.write("127.0.0.1    localhost localhost.localdomain localhost4 localhost4.localdomain4\n")
    f.write("::1          localhost localhost.localdomain localhost6 localhost6.localdomain6\n")
    f.write("10.25.32.50  head\n")
    f.writelines(f"{nodes[i+1]:<12} compute-{i+1:02}\n" for i in range(len(nodes)))

with open("src/hostfile", 'w') as f:
    f.writelines(f"{nodes[i+1]:<12} slots=20 max_slots=20\n" for i in range(len(nodes)))
