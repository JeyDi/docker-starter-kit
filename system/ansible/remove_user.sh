# Old method
# for f in keys/revoked/*.pub; do
#     ansible pbg_root -i inventory.yml -u root -m authorized_key -a "user=root state=absent key={{ lookup('keys/', '${f}') }}"
# done

# New method with playbook
ansible-playbook -i inventory.ini -l "pbg" playbooks/remove_user.yml