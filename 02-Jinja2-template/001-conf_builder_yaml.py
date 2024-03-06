import yaml
from jinja2 import Environment, FileSystemLoader

config = yaml.full_load(open('./data.yml'))

env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('cisco_template_yaml.j2')

result = template.render(config)
print(result)

with open(r'./result.yml','w') as file:
    file.write(result)