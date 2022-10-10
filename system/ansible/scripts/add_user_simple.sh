#!/bin/bash
for f in keys/authorized/*.pub; do
    echo "adding user with auth key: ${f}"
    ansible-playbook -i inventory.ini -l "gpu2" playbooks/new_user_standard.yml
done

