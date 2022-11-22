from random import randint
#


def gen_mac_char():
    return hex((randint(0, 16))).split('x')[1]


def gen_mac_pair():
    return ''.join([gen_mac_char(), gen_mac_char()])


def gen_last_half_mac(stem):
    return ':'.join([stem, gen_mac_pair(), gen_mac_pair(), gen_mac_pair()])


print(gen_last_half_mac('00:60:2f'))
