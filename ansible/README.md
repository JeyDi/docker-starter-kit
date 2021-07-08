# My Ansible 

My personal collection of Ansible Playbook to automatically install a personal VPS with all i need.

References:
- https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-automate-initial-server-setup-on-ubuntu-18-04
- https://www.jitsejan.com/creating-ansible-deployment-for-ubuntu-vps
- https://github.com/jitsejan/vps-provision
- https://github.com/craighurley/ansible-personal-vps

See also the Ansible documentation page here or on Notion.

To solve the ssh credential problem remember to set the env variable:
`export ANSIBLE_HOST_KEY_CHECKING=False`

If you want to test a single machine connection do:
`ansible all -m ping -i ./inventory.ini -u root --ask-pass`

## Folder organization

The file: `inventory.ini` contains my machine definitions with all the informations.

Inside the inventory.ini files there are different server groups that you can use.

The file: `provision-vps.yml` contains the starting point for all the configuration, inside this file you can find a list of roles and the variable configuration for the user (username and password asked to the user by prompt)

The folder: `roles` contains all the playbook divided by task
- base: basic getting started configuration for the server (tools, packages, ufw, ssh, ... )
- cran_r: installation of R
- docker: installation of Docker
- docker_stop: if you want to stop the docker daemon
- games: collection of game server to install
- journal_dir:
- nodejs: installation of node js
- python: installation of python, pyenv, poetry and all related packages


## Launch the playbook

To launch all the playbook (with the new or reinstalled machine)
```shell
ansible-playbook -i inventory.ini provision-vps.yml -u root --ask-pass
```
If you want to test the connection to server after the ansible update: `ssh jeydi@server.pythonbiellagroup.it -p 4292 -i ~/.ssh/jeydit4v`

If you want to launch a specific playbook (for example docker):  
`ansible-playbook -i inventory.ini provision-vps.yml -u jeydi --key-file "~/.ssh/jeydit4v.pub" --tags "docker"`

If you want to launch a specific playbook with specific configuration 
`ansible-playbook -i inventory.ini -l "personal_setup" provision-vps.yml --tags "docker"`