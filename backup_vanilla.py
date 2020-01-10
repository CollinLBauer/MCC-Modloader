import os
import shutil
import json


def backup_file(filepath, force=False):
  # uses copyfile to back up file with the .original tag amended
  # tbh I prefer a folder attempt to tags, but the project's brand new so whatever.
  backfile = filepath + ".original"
  if not force and os.path.exists(backfile):
    return
  
  shutil.copyfile(filepath, backfile)


def backup_originals(directory, gui=False):
  #TODO
  '''
  print("Backing up files...", end="")
  for each file in directory:
    if file ends in ".map":
      send it to backup_file()
      if gui=False:
        print(".", end="", dumpbuffer)
  print("Done.")
  '''

  print("Not yet implemented!")
  pass


def main():
  with open("settings.json", "r") as settings:
    dir = json.loads(settings.read())["directory"]

  if not os.path.exists(dir):
    print("Map directory not found!\nPlease change the directoy in settings.json")
    return
  
  print("""This program will backup all vanilla map files.
WARNING: This utility assumes all currently active .map files are vanilla.

Continue? y/n: """,
  end="")

  answer = ""
  while answer != "Y" and answer != "N":
    answer = input().upper()
  if answer == "Y":
    backup_originals(dir)


main()