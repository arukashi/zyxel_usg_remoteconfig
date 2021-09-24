# zyxel_usg_remoteconfig

# Synopsis
Simple script for configuring Zyxel USG devices remotely over SSH. Created with a little help of https://github.com/ArcliteF22

# Requirements
* Python 3.9
* Netmiko module for Python

# Description

Three parameters that are mandatory for running this script:

* `--user` - username for admin account
* `--routerlist` - path to file containing list of target devices, IP addresses or FQDN. 
* `--conf` - path to file containing list of commands in config mode

Script expecting same username and password on all of the devices you want to configure, so you'd enter password just once.

There is no need for "configure terminal" in `--conf` file, because script enters config mode anyway.

# Usage example
`[username@host ~]$ python3.9 zyxelremoteconf.py --user sshadmin --routerlist routers.txt --conf zyxelconf.txt  `
