#!/bin/bash
for f in keys/authorized/*.pub; do
    echo "adding user with auth key: ${f}"
    ansible-playbook -i inventory.ini -l "personal_setup" new-user-standard.yml    
done

