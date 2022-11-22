#!/usr/bin/env python
from subprocess import call, check_output
from rich.progress import track
from time import sleep
import argparse

import re
console = Console()

def hello():

    options = get_arguments()
    current_mac = get_current_mac(options.interface)

    console.print(Panel(f'''
    1. Help is [red]python3 main.py --hello[/red]
    2. How it should look like [red]python3 main.py -i INTERFACE -m NEW_MAC[/red]
       2.1 For example [red]python3 main.py -i eth0 -m 00:11:22:33:44:55[/red]
    3. Check result [red]ifconfig[/red]
    4. Your current MAC address is [red]{current_mac}[/red]
    ''', title='[white]Change MAC address'), justify='center')
=======


    # change_mac(options.inteface, options.new_mac)

def get_current_mac(interface):
    ifconfig_result  = check_output(['ifconfig', interface])
    mac_adress_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if mac_adress_result:
       return mac_adress_result.group(0)
    else:
        return 'Coudn\'t read interface' # change it


def get_arguments():
    parser = argparse.ArgumentParser(
        prog='MacAddress',
        description='The programm will got changed you MAC Address.',
        epilog='Check it in "ifconfig"')
    parser.add_argument('-i',  '--interface',
                        help='Interface to change its MAC address')
    parser.add_argument('-m', '--mac', help='New MAC address')
    options, arguments = parser.parse_args(), parser.parse_args()

    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    elif not options.mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')

    return options


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC adress for {interface} to {new_mac}')
    call(['ifconfig', interface, 'down'])
    call(['ifconfig', interface, 'hw', 'ether', new_mac])
    call(['ifconfig', interface, 'up'])
    call(['ifconfig'])



options, argument = get_arguments(), get_arguments()

change_mac(options.interface, options.mac)

if '__name__' == '__main__':
    get_arguments()

