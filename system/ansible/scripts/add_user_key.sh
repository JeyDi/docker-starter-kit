#!/bin/bash
echo "add to the user the auth key"
ansible-playbook -i inventory.ini -l "gpu2" playbooks/add_user_key.yml --ask-pass

