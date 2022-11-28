from subprocess import check_output
from rich.console import Console
from rich.panel import Panel
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
    4. Your current MAC address is [blue]{current_mac}[/blue]
    ''', title='[white]Change MAC address'), justify='center')


def get_current_mac(interface):
    ifconfig_result = check_output(['ifconfig', interface])
    mac_adress_result = re.search(
        r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if mac_adress_result:
        return mac_adress_result.group(0)
    else:
        return 'COULDN\'T READ INTERFACE'


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',  '--interface',
                        help='Interface to change its MAC address')
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    hello()