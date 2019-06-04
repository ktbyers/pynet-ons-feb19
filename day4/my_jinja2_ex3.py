from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

ipv4_enable = True
ipv6_enable = False

vrf_var = {
    'vrf_name': 'blue',
    'rd_number': '100:1',
    'ipv4_enable': True,
    'ipv6_enable': True,
}

print()
template_file = "my_jinja2_ex3.j2"
template = env.get_template(template_file)
cfg = template.render(**vrf_var)
print(cfg)
print()

