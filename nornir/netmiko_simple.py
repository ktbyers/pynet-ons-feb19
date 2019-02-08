from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
# from nornir.plugins.functions.text import print_result
from nornir_utilities import nornir_set_creds, std_print


def main():

    # Initialize Nornir object using hosts.yaml/groups.yaml/defaults.yaml
    norn = InitNornir(config_file="nornir.yaml")
    nornir_set_creds(norn)
    result = norn.run(
        netmiko_send_command,
        num_workers=20,
        command_string="show ip arp",
        # use_textfsm=True,
    )
    std_print(result)


if __name__ == "__main__":
    main()
