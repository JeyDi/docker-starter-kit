#!/bin/bash
# for f in keys/*.pub; do
#     echo "adding user with auth key: ${f}"
#     ansible-playbook -i inventory.ini -l "pbg" playbooks/add_user_standard.yml
# done
ansible-playbook -i inventory.ini -l "pbg" playbooks/add_user_standard.yml
