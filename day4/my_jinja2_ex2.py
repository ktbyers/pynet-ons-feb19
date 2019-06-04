
import jinja2
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

nxos1 = {
    'interface' = 'Ethernet2/1',
    'ip_address' = '10.1.1.1',
    'mask' = '/24',
}


nxos2 = {
    'interface' = 'Ethernet2/1',
    'ip_address' = '10.2.1.1',
    'mask' = '/24',
}

print()
for j2_vars in (nxos1, nxos2):
    template_file = "my_jinja2_ex2.j2"
    template = env.get_template(template_file)
    output = template.render(**j2_vars)
    print("-" * 10)
    print(j2_vars["host"])
    print("-" * 10)
    print(output.lstrip())
print()

