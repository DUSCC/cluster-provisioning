#!/bin/bash

./generate_hosts.py
ansible-playbook ansible/head-playbook.yaml -i ansible/inventory_hosts