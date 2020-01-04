import os
import sys
from pathlib import Path
import shutil 
import json

with open("settings.json", "r") as settings:
  dir = json.loads(settings.read())["directory"]


def backup_original():
  print("Not yet implemented.")
  pass


def main():
  '''
  if not os.path.exists(dir):
    print("Map directory not found!\nPlease change the directoy in settings.json")
    return
    '''
  
  print("""This program will backup all vanilla map files.
WARNING: This utility assumes all currently active .map files are vanilla.
Any currently backed up map files will be lost.

Are you sure you want to continue? y/n: """,
  end="")

  answer = ""
  while answer != "Y" and answer != "N":
    answer = input().upper()
  if answer == "Y":
    backup_original()


main()