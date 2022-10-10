#!/bin/bash
echo "Setup advance python for a specific user..."
ansible-playbook -i inventory.ini ../playbooks/setup_advance_python.yml
# ansible-playbook -i inventory.ini -l "personal_setup" playbook/start_config.yml
# ansible-playbook -i inventory.ini playbook/start_config.yml --tags "docker"
echo "finish..."


