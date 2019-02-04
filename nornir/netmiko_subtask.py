from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir_utilities import nornir_set_creds, std_print


def test_task(task):
    # net_connect = task.host.get_connection("netmiko", task.nornir.config)
    cmd = task.host.get("arp_cmd", "show ip arp")
    result = task.run(netmiko_send_command, command_string=cmd)
    return result


def main():

    # Initialize Nornir object using hosts.yaml/groups.yaml/defaults.yaml
    norn = InitNornir(config_file="/home/kbyers/nornir_inventory/config.yaml")
    nornir_set_creds(norn)
    result = norn.run(test_task, num_workers=20)
    std_print(result)


if __name__ == "__main__":
    main()
