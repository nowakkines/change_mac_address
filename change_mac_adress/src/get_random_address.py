from random import randint
from subprocess import call
import argparse

interface = input('write here >> ')

def gen_mac_char():
    return hex((randint(0, 16))).split('x')[1]

def gen_mac_pair():
    return ''.join([gen_mac_char(), gen_mac_char()])


def gen_last_half_mac(stem):
    return ':'.join([stem, gen_mac_pair(), gen_mac_pair(), gen_mac_pair()])


def get_mac_address():
    new_mac = gen_last_half_mac('00:60:2f')

    change_mac(new_mac, interface)


def change_mac(new_mac, interface):
    call[f'[+] Changing MAC address for {interface} {new_mac}']
    call(['ifconfig', interface, 'down'])
    call(['ifconfig', interface, 'hw', 'ether', new_mac])
    call(['ifconfig', interface, 'up'])


print(gen_last_half_mac('00:60:2f'))
get_mac_address()

#FIXME:
#call[f'[+] Changing MAC address for {interface} {new_mac}']
#TypeError: 'function' object is not subscriptable
