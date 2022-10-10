# JeyDi Ansible and Server Configurations

My personal Ansible collection of playbook and roles.

We are using this collection also with PythonBiellaGroup to manage our servers and machines.

See also the Ansible documentation page here or on Notion.

If you want to test a single machine connection do:
`ansible all -m ping -i ./inventory.ini -u root --ask-pass`

Remember to install Ansible following the official guide:
- https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Thanks to: Andrea Melloncelli (Vanlog) @Akirocode for the support

## Folder organization
The file: `inventory.ini` contains all the servers and machines that you want to manage

Inside the `inventory.ini` files there are different server groups that you can use.

**Attention**: the `inventory.ini` file use the `~/.ssh/config` file on your machine so please be sure to have a correct configuration file.

In the folder: `playbooks` you will find all the starting point of the ansible `roles`

In the `scripts` folder you can find all the scripts to launch Ansible playbooks with roles

The file: `start_config_internal.yml` and ``start_config_swisscom.yml` inside the folder `playbooks` contains the starting point for all the configuration, inside this file you can find a list of roles and the variable configuration for the user (username and password asked to the user by prompt).

You can find the `scripts`: `launch_internal.sh` and `launch_swisscom.sh` into the `scripts` folder that you can launch to start creating the servers

The folder: `roles` contains all the playbook divided by task
- **base-tools**: basic getting started configuration for the server (tools, packages, ufw, ssh, ... )
- **bashtop**: to configure and install bashtop monitoring service
- **cran-r**: installation of R
- **r-setup**: installation of R
- **docker**: installation of Docker
- **docker_stop**: if you want to stop the docker daemon
- **nodejs**: installation of node js
- **python**: installation of python, pyenv, poetry and all related packages
- **python_advance**: to install pyenv and poetry for a specific user
- **sshd**: to configure sshd config file with security policies
- **fail2ban**: to install and configure a basic fail2ban service in the server
- **users**: to create new users inside the server
- **virtualbox**: to install and configure virtualbox virtualization service in the server
- **zsh**: to install and configure zsh


## Setup


First of all it's important to configure your `~/.ssh/config` file.

All the playbook and roles here in his project it's made using the custom ~/.ssh/config file.

It's also **very important** to modify the `inventory.ini` file correctly if you want to use your credentials

When you have setup everything try to look the scripts in the `scripts` folder (for example: `launch_internal.sh`)

And then the respective ansible playbook inside the `playbooks` folder (for example: `start_config_internal.yml`)

If you want to personalize the installation of ansible you can follow this examples

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
`ansible-playbook -i inventory.ini start_config.yml -u aiteam --key-file "~/.ssh/aiteam" --tags "docker"`

If you want to launch a specific playbook with specific roles and configurations 
`ansible-playbook -i inventory.ini start_config.yml --tags "docker"`

## Normal Usage

If you want to use this project on your new machine you can look the playbook: `start_config.yml` that contains the getting started configuration.

Before launch everything please check the connections with the ping

If everything it's working and after your modification you can launch everything by launching the sh script: `./scripts/launch` 


## Considerations

If you have problems with permissions on ssh keys or if you want some help with ssh keys, please refer to this github gist:
- https://gist.github.com/grenade/6318301

If you have some problems regarding ssh password with this message: `Ansible: To use the 'ssh' connection type with passwords, you must install the sshpass program"` you have to install **sshpass tool**, look those link and examples:
- https://stackoverflow.com/questions/42835626/ansible-to-use-the-ssh-connection-type-with-passwords-you-must-install-the-s
- https://gist.github.com/arunoda/7790979


## References

References:
- https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-automate-initial-server-setup-on-ubuntu-18-04
- https://www.jitsejan.com/creating-ansible-deployment-for-ubuntu-vps
- https://github.com/jitsejan/vps-provision
- https://github.com/craighurley/ansible-personal-vps