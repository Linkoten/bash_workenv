import yaml

# Config file path.
CONFIG_PATH = ".workenv.yml"

# Config file key names.
DESKTOP_NUMBER = "desktop_number"
DEFAULT_DESKTOP = "default_desktop"
COMMANDS = "commands"

def parse_value(name):
    with open(CONFIG_PATH, 'r') as config_file:
        configs = yaml.safe_load(config_file)
    workenv_config = configs[name]

