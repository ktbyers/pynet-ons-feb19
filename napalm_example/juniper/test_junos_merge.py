#!/usr/bin/env python
from __future__ import print_function
from getpass import getpass
from pprint import pprint as pp
from napalm_base import get_network_driver

ip_addr = 'srx1.twb-tech.com'
username = 'pyclass'
password = getpass()
optional_args = {}

driver = get_network_driver('junos')
device = driver(ip_addr, username, password, optional_args=optional_args)

def hit_enter():
    try:
        raw_input("Hit enter to continue: ")
    except NameError:
        input("Hit enter to continue: ")

print()
print(">>>Test device open")
device.open()

print()
print(">>>Load config change (merge) - no commit")
device.load_merge_candidate(filename='junos-merge.conf')
print(device.compare_config())
hit_enter()

print()
print(">>>Discard config change (merge)")
device.discard_config()
print(device.compare_config())
hit_enter()

print()
print(">>>Load config change (merge) - commit")
device.load_merge_candidate(filename='junos-merge.conf')
print(device.compare_config())
device.commit_config()
hit_enter()

print()
print(">>>Rollback")
device.rollback()
hit_enter()
