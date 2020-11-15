import typer
import os


def run_bin(bin: str, args: str):
    os.system(f"{bin} {args}")

def wmctrl(args):
    run_bin("wmctrl", args)

def go_to_desktop(desktop):
    wmctrl(f"-s {desktop}")

def set_desktop_number(number: int):
    wmctrl(f"-n {number}")

def main(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
