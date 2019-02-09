from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F
from nornir_utilities import nornir_set_creds, std_print
from nornir.plugins.tasks.text import template_file


def test_task(task):
    result = task.host["template_config"] = task.run(task=template_file,
                                            template="router.j2", path="")
    return result


def main():
    norn = InitNornir(config_file="nornir.yaml")
    f = F(groups__contains="juniper")
    norn = norn.filter(f)
    result = norn.run(test_task, num_workers=1)
    std_print(result)


if __name__ == "__main__":
    main()
