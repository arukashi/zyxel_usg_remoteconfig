# zyxel_usg_remoteconfig

# Synopsis
Simple script for configuring Zyxel USG devices remotely over SSH. 

# Requirements
* Python 3.9
* Netmiko module for Python

# Description

Three parameters are mandatory for running this script:

* `--user` - username for admin account
* `--routerlist` - path to file containing list of target devices, IP addresses or FQDN. 
* `--conf` - path to file contining list of commands in config mode

Script expecting same username and password on all of the devices you want to configure. 

# Usage example
`[username@host ~]$ python3.9 zyxelremoteconf.py --user sshadmin --routerlist routers.txt --conf zyxelconf.txt  `
