from pprint import pprint
import yaml
f = open("yaml_ex1.yml")
output = yaml.load(f)
pprint(output)
