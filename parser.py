import yaml

path=".workenv.yml"


def parse_value(name):
    stream = open(path, 'r')
    config = yaml.safe_load(stream)
    workenv_config = config[name]
    print(workenv_config)


