import os
import sys
from pathlib import Path
import shutil 
import json
from cmd_specific_actions import *

with open("settings.json", "r") as settings:
    dir = json.loads(settings.read())["directory"]


def main():
    if not os.path.exists(dir):
        print("Map directory not found!\nPlease change the directoy in settings.json")
        return
  
    menu()

main()
