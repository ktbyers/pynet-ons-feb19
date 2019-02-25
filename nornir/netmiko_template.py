from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F
from nornir_utilities import nornir_set_creds, std_print
from nornir.plugins.tasks.text import template_file

import ipdb

def test_task(task):
    ipdb.set_trace()
    group_name = task.host.groups[0]  
    group = task.nornir.inventory.groups[group_name]
    result = task.host["template_config"] = task.run(task=template_file,
                                            template="router.j2", path="", group=group)
    return result


def main():
    norn = InitNornir(config_file="nornir.yaml")
    ipdb.set_trace()
    f = F(groups__contains="juniper")
    norn = norn.filter(f)
    result = norn.run(test_task, num_workers=1)
    std_print(result)


if __name__ == "__main__":
    main()
