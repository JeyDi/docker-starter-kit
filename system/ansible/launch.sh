#!/bin/bash
echo "launching provision-vps.yml"
ansible-playbook -i inventory.ini start_config.yml --ask-pass
# ansible-playbook -i inventory.ini -l "personal_setup" playbook/start_config.yml
# ansible-playbook -i inventory.ini playbook/start_config.yml --tags "docker"
echo "finish..."


