#!/usr/bin/env python

from subprocess import SubprocessError, call
from rich.progress import track
from time import sleep
import argparse


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
