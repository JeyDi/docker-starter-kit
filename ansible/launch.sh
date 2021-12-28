#!/bin/bash
echo "launching provision-vps.yml"
# ansible-playbook -i inventory.ini -l "personal_setup" provision-vps.yml
ansible-playbook -i inventory.ini provision-vps.yml --tags "docker"
echo "finish..."


