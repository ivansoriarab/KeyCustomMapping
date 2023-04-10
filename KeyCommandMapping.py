import argparse
import pynput.keyboard as keyboard
import os

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('key')
argument_parser.add_argument('command')

arguments = argument_parser.parse_args()

def on_press(key):
    if not (hasattr(key, "char") and key.char == arguments.key) and not (hasattr(key, "name") and key.name == arguments.key):
        return

    os.system("drutil tray eject")

listener = keyboard.Listener(on_press=on_press)

with listener:
    listener.join()