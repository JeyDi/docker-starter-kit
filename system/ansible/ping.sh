# remember to use --ask-pass if you don't want to set ssh keys in inventory.ini for the host

# launch ping direct 
# ansible pbg_root -m ping -i inventory.ini --ask-pass

# launch the ping with playbook
ansible-playbook -i inventory.ini playbooks/ping.yml --ask-pass

# launch the echo with playbook
ansible-playbook -i inventory.ini playbooks/send_echo.yml --ask-pass