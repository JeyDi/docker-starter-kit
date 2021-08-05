for f in keys/revoked/*.pub; do
    ansible moxoff_hq -i inventory.yml -u root -m authorized_key -a "user=root state=absent key={{ lookup('file', '${f}') }}"
done