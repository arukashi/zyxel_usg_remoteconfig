from netmiko import ConnectHandler
from getpass import getpass
import argparse

# Pass the arguments block. All parameters are mandatory
parser = argparse.ArgumentParser()
parser.add_argument('--user', type=str, required=True, help="admin user name")
parser.add_argument('--routerlist', type=str, required=True, help="path to router list file")
parser.add_argument('--conf', type=str, required=True, help="path to config file")
args = parser.parse_args()

print("Input user password")
sshuser_pass = getpass()

with open(args.routerlist) as f:
    for router in f:
        # check if line in routers_file commented
        if router.startswith("#"):
            continue
        rout = router.rstrip('\n')
        print('You are now connecting to', rout)
        device1 = {
            "device_type": "cisco_ios",
            "host": rout,
            "username": args.user,
            "password": sshuser_pass,
        }

        try:
            net_connect = ConnectHandler(**device1)
        except:
            print("Cannot connect to", rout, "SSH Server")
            continue

        net_connect.enable()
        # в файле с инструкциями не указываем configure terminal, метод ниже является тем же conf t
        net_connect.config_mode()

        with open(args.conf) as config_file:
            for cfgline in config_file:
                if cfgline.startswith("#"):
                    continue
                print(cfgline, end='')
                net_connect.send_command_timing(cfgline)

        # for some reason instruction below does not working, that's why it has been commented
        # net_connect.exit_config_mode()

        net_connect.disconnect()

        if not router:
            break
