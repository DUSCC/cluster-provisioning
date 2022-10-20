#!/usr/bin/python3
import os
import json


output = os.popen("openstack server list -f json")
nodes = json.loads(output.read())
hosts_output = []

for node in nodes:
    try:
        ip = node['Networks']['stbl'][0]
    except KeyError:
        continue
    name = '-'.join(f"{substr:>03}" for substr in node['Name'].split('-'))
    hosts_output += [[name, ip]]

hosts_output.sort(key=lambda x: x[0])
name, ip = hosts_output[-1]
output = f"{ip:<12} {name}\n" + "\n".join(f"{ip:<12} {name}" for name, ip in hosts_output[:-1])

with open("src/hosts", 'w') as f:
    f.write("127.0.0.1    localhost localhost.localdomain localhost4 localhost4.localdomain4\n")
    f.write("::1          localhost localhost.localdomain localhost6 localhost6.localdomain6\n")
    f.write(output)

broken_hosts = set()
with open("src/broken_hosts", 'r') as f:
    for line in f.readlines():
        broken_hosts.add(line.strip())

with open("src/bad_ip_hosts", 'r') as f:
    for line in f.readlines():
        broken_hosts.add(line.strip())

with open("src/hostfile", 'w') as f:
    f.writelines(f"{name} slots=20 max_slots=20\n" for name, ip in hosts_output[:-1] if name not in broken_hosts)
