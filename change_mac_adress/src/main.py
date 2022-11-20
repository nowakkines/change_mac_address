#!/usr/bin/env python

from subprocess import SubprocessError, call
from rich.progress import track
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich import print
import argparse
console = Console()

def hello():
    console.print(Panel('''
    Help --> python3 main.py [red]--hello[/red]
    How it should look like --> python3 main.py -i [red]INTERFACE[/red] -m [red]NEW_MAC[/red]
    For example --> [blue]python3 main.py -i eth0 -m 00:11:22:33:44:55[/blue]
    Check result --> [red]ifconfig
    ''', title='[white]Change MAC address'), justify='center')

    process()


def process():
    options, argument = get_arguments(), get_arguments()
    change_mac(options.interface, options.mac)


def get_arguments():
    parser = argparse.ArgumentParser(
        prog='MacAddress',
        description='The programm will got changed you MAC Address.',
        epilog='HOW IT SHOULD LOOK LIKE --> python3 main.py -i eth0 -m 00:11:22:33:44:55')
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


if __name__ == '__main__':
    hello()
