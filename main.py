import typer
import os
import time
from parser import parse_value

def run_bin(bin: str, args: str):
    os.system(f"{bin} {args}")
    
def wmctrl(args):
    run_bin("wmctrl", args)

def go_to_desktop(desktop):
    wmctrl(f"-s {desktop}")

def set_desktop_number(number: int):
    wmctrl(f"-n {number}")

def main(workenv_name: str):
    workenv = parse_value(workenv_name)
    for workenv_command in workenv.commands:
        go_to_desktop(workenv_command.desktop)
        run_bin(workenv_command.command, "")
        time.sleep(2)

if __name__ == "__main__":
    typer.run(main)
