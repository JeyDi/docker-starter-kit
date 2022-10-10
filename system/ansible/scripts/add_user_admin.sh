#!/bin/bash
for f in keys/authorized/*.pub; do
    echo "adding user with auth key: ${f}"
    ansible-playbook -i inventory.ini -l "pbg_admin" playbooks/new_user_admin.yml
done

