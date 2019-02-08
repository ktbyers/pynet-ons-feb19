from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
# from nornir.plugins.functions.text import print_result

from nornir_utilities import nornir_set_creds, std_print


def main():

    # Initialize Nornir object using hosts.yaml/groups.yaml/defaults.yaml
    norn = InitNornir(config_file="./nornir.yaml")
    nornir_set_creds(norn)

    # f = F(groups__contains="juniper")
    # my_devices = norn.filter(f)
    # f = F(groups__contains="arista")
    # f = F(groups__contains="arista") | F(groups__contains="cisco")
    # my_devices = norn.filter(hostname="arista1.lasthop.io")
    # my_devices = norn
    f = F(groups__contains="cisco")
    my_devices = norn.filter(f)

    result = my_devices.run(
        netmiko_send_command,
        num_workers=20,
        command_string="show ip arp",
        # use_textfsm=True,
    )
    std_print(result)


if __name__ == "__main__":
    main()
