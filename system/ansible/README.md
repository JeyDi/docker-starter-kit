# JeyDi Ansible and Server Configurations

My personal Ansible collection of playbook and roles

References:
- https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-automate-initial-server-setup-on-ubuntu-18-04
- https://www.jitsejan.com/creating-ansible-deployment-for-ubuntu-vps
- https://github.com/jitsejan/vps-provision
- https://github.com/craighurley/ansible-personal-vps

See also the Ansible documentation page here or on Notion.

If you want to test a single machine connection do:
`ansible all -m ping -i ./inventory.ini -u root --ask-pass`

Remember to install Ansible following the official guide:
- https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Thanks to: Andrea Melloncelli (Vanlog) @Akirocode for the support

## Folder organization

The file: `inventory.ini` contains my machine definitions with all the informations.

Inside the `inventory.ini` files there are different server groups that you can use.

**Attention**: the `inventory.ini` file use the `~/.ssh/config` file on your machine so please be sure to have a correct configuration file.

In the folder: `playbooks` you will find all the starting point of the ansible `roles`

The file: `provision-vps.yml` inside the folder `playbooks` contains the starting point for all the configuration, inside this file you can find a list of roles and the variable configuration for the user (username and password asked to the user by prompt)

The folder: `roles` contains all the playbook divided by task
- base: basic getting started configuration for the server (tools, packages, ufw, ssh, ... )
- cran_r: installation of R
- docker: installation of Docker
- docker_stop: if you want to stop the docker daemon
- nodejs: installation of node js
- python: installation of python, pyenv, poetry and all related packages


## Setup

First of all it's important to configure your `~/.ssh/config` file.

All the playbook and roles here in his project it's made using the custom ~/.ssh/config file.

It's also **very important** to modify the `inventory.ini` file correctly if you want to use your credentials

### Setup ssh key

Remember to generate also ssh key for your machine and publish to the user

1. Generate valid stable ssh keys:
```shell
#generate the new key
ssh-keygen -t ed25519 -C "myemail@email.com" -f ~/.ssh/mykey
```

2. Copy the ssh key to the `~/.ssh/<keyname>` file
```shell
#copy the public key to a server
ssh-copy-id -i <path-of-the-pub-key> <username>@<host>
```

3. Remember to set (and check) permissions for your keys in your machine:
```shell

```


### Install ansible in a virtual environment

```sh
python3 -m virtualenv venv
. ./venv/bin/activate
pip install -r requirements-dev.txt
```

### Install the required ansible modules

enter a ansible-* folder depending on the server you want to configure. For example:

```sh
cd ansible-vserver
```

Install external modules (using ansible-galaxy):

```sh
ansible-galaxy install -r requirements.yaml
```

## Common commands

Launch a ping in a machine to test if they are reachable:
- `ansible ai -m ping -i inventory.ini`

If you don't want to use (or you don't have) the `ssh key` file you can use the `--ask-pass` option in shell to ask the user for the password:
- `ansible-playbook ./playbooks/ping.yml -i inventory.ini --ask-pass`

Launch the ping script to test if a single or multiple machine are reachable:
- ./ping.sh

Get a list of all tags in a specific playbook
`ansible-playbook ./playbooks/start_config.yml --list-tags`

`ansible-playbook ./playbooks/start_config.yml --tags dev-applications`

`ansible-playbook ./playbooks/start_config.yml --list-tags | grep -i media`

`ansible-playbook ./playbooks/start_config.yml --tags dev-applications`


## Launch the playbook

To launch one playbook to test (with the new or reinstalled machine)
```shell
ansible-playbook -i inventory.ini playbooks/send_echo.yml
```

If you want to launch a specific playbook with settings:  
`ansible-playbook -i inventory.ini provision-vps.yml -u jeydi --key-file "~/.ssh/jeydit4v" --tags "docker"`

If you want to launch a specific playbook with specific roles and configurations 
`ansible-playbook -i inventory.ini -l "personal_setup" provision-vps.yml --tags "docker"`


## Considerations

If you have problems with permissions on ssh keys or if you want some help with ssh keys, please refer to this github gist:
- https://gist.github.com/grenade/6318301

If you have some problems regarding ssh password with this message: `Ansible: To use the 'ssh' connection type with passwords, you must install the sshpass program"` you have to install **sshpass tool**, look those link and examples:
- https://stackoverflow.com/questions/42835626/ansible-to-use-the-ssh-connection-type-with-passwords-you-must-install-the-s
- https://gist.github.com/arunoda/7790979
