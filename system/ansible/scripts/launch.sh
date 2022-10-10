#!/bin/bash
# use --ask-pass if you want to ask password auth
echo "launching starting configuration: start_config.yml"
ansible-galaxy collection install community.general
ansible-playbook -i inventory.ini -l "pbg"  playbooks/start_config.yml --ask-pass
# ansible-playbook -i inventory.ini -l "gpu2" playbooks/start_config_internal.yml --tags "gitlab" --ask-pass
# ansible-playbook -i inventory.ini playbooks/start_config_internal.yml --tags "users" --ask-pass
echo "finish..."


