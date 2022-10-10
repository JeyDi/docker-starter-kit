#!/bin/bash
echo "Add zsh shell to a specific user"
ansible-playbook -i inventory.ini ../playbooks/add_zsh_user.yml
# ansible-playbook -i inventory.ini -l "personal_setup" playbook/start_config.yml
# ansible-playbook -i inventory.ini playbook/start_config.yml --tags "docker"
echo "finish..."


