#!/bin/bash
for f in keys/authorized/*.pub; do
    echo "adding user with auth key: ${f}"
    ansible-playbook -i inventory.ini -l "personal_setup" new-user-admin.yml --tags "docker"
    # ansible moxoff_hq -i inventory.yml -u root -m authorized_key -a "user=root state=present key={{ lookup('file', '${f}') }}"
done

