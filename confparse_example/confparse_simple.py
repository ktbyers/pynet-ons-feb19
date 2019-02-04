#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse
import ipdb

cisco_file = "cisco_config.txt"

cisco_cfg = CiscoConfParse(cisco_file)
intf_obj = cisco_cfg.find_objects(r"^interf")
print()
ipdb.set_trace()
for intf in intf_obj:
    print(intf.text)
    for child in intf.children:
        print(child.text)
    print()
