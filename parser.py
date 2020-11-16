import yaml
from pydantic import BaseModel
from typing import List

# Config file path.
CONFIG_PATH = ".workenv.yml"

# Config file key names.
DESKTOP_NUMBER = "desktop_number"
DEFAULT_DESKTOP = "default_desktop"
COMMANDS = "commands"

class WorkenvCommand(BaseModel):
    command: str
    desktop: int

class Workenv(BaseModel):
    desktop_number: int
    default_desktop: int
    commands: List[WorkenvCommand]

def parse_value(name):
    with open(CONFIG_PATH, 'r') as config_file:
        configs = yaml.safe_load(config_file)
    workenv_config = configs[name]
    commands = []
    for desktop, command in workenv_config[COMMANDS]:
        commands.append(WorkenvCommand(command = command, desktop = desktop))
    return Workenv(desktop_number = workenv_config[DESKTOP_NUMBER], default_desktop = workenv_config[DEFAULT_DESKTOP], commands = commands)
