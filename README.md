# Python untuk yaml dan Jinja2

### &#x1F680; 01-yaml

#### Begin :

    ❯ cd 01-yaml

    ❯ python -m venv venv

    ❯ source venv/bin/activate

    # install packages

    ❯ pip install pyyaml

    ❯ pip install Jinja2


#### Code :

001-write-yaml.py :

    import yaml

    dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
    {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

    with open(r'./store_file.yaml', 'w') as file:
        yaml.dump(dict_file, file)
        print("Done")


#### Folder and file structure :

    ❯ tree -L 3 -I 'venv'

        ├── 001-conf_builder_yaml.py
        ├── data.yml
        └── templates
            └── cisco_template_yaml.j2


#### Run :

    ❯ python3 001-write-yaml.py


#### Result : 

    ❯ cat store_file.yaml

        - sports:
            - soccer
            - football
            - basketball
            - cricket
            - hockey
            - table tennis
        - countries:
            - Pakistan
            - USA
            - India
            - China
            - Germany
            - France
            - Spain

---


### &#x1F680; 02-Jinja2-template

#### Begin :

    ❯ cd 02-Jinja2-template

    ❯ python -m venv venv

    ❯ source venv/bin/activate

    # install packages

    ❯ pip install pyyaml

    ❯ pip install Jinja2

#### Code :

001-conf_builder_yaml :

    import yaml
    from jinja2 import Environment, FileSystemLoader

    config = yaml.full_load(open('./data.yml'))

    env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('cisco_template_yaml.j2')

    result = template.render(config)
    print(result)

    with open(r'./result.yml','w') as file:
        file.write(result)

#### Run :





---

#### Notes:

    ❯ pip list

        Package    Version
        ---------- -------
        Jinja2     3.1.3
        MarkupSafe 2.1.5
        pip        22.0.4
        PyYAML     6.0.1
        setuptools 58.1.0