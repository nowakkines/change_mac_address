#!/usr/bin/env python
from subprocess import call, check_output
from rich.progress import track
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich import print
import argparse
import re


console = Console()


def process():
    options = get_arguments()
    current_mac = get_current_mac(options.interface)
    change_mac(options.interface, options.mac)
    check_mac_adress(current_mac, options)


def get_current_mac(interface):
    ifconfig_result = check_output(['ifconfig', interface])
    mac_adress_result = re.search(
        r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if mac_adress_result:
        return mac_adress_result.group(0)
    else:
        return 'COUDN\'T READ INTERFACE'


def get_arguments():
    parser = argparse.ArgumentParser(
        prog='MacAddress',
        description='The programm will got changed you MAC Address.',
        epilog='HOW IT SHOULD LOOK LIKE --> python3 main.py -i eth0 -m 00:11:22:33:44:55')
    parser.add_argument('-i',  '--interface',
                        help='Interface to change its MAC address')
    parser.add_argument('-m', '--mac', help='New MAC address')

    options = parser.parse_args()

    if not options.interface:
        parser.error(
            '[-] Please specify an interface, use --help for more info.')
    elif not options.mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')

    return options


def check_mac_adress(current_mac, options):
    for _ in track(range(50), description='[green]Processing...'):
            sleep(0.03)
    if current_mac != options.mac:
        print(f'[+] Mac address was successfully changed to {options.mac}')
    else:
        print('[-] MAC address didn\'t get changed.')


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC adress for {interface} to {new_mac}')
    call(['ifconfig', interface, 'down'])
    call(['ifconfig', interface, 'hw', 'ether', new_mac])
    call(['ifconfig', interface, 'up'])


if __name__ == '__main__':
    process()