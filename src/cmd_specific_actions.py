import os
import sys
from pathlib import Path
import shutil 
import json

def menu():
    print("\nHalo: The Master Chief Collection Modloader")
    choice = input("""
    A: Enter Vanilla/Original Mode
    B: Enter Modded Mode
    C: Show Modlist
    D: Help
    E: Quit/Exit
    Please enter your choice: """)

    if choice.upper()=="A":
        vanilla()
    elif choice.upper()== "B":
        modded()
    elif choice.upper()== "C":
        modlist()
    elif choice.upper()=="D":
        help()
    elif choice.upper()=="E":
        sys.exit       
    else:
        print("You must only select either A,B,C,D, or E.")
        print("Please try again\n")
        menu()
        
def vanilla():
  for subdir, dirs, files in os.walk(dir):
    for filename in files:
        file = subdir + os.sep + filename
        base, ext = os.path.splitext(file)
        if ext == ".original":
            shutil.move(os.path.join(dir, file),os.path.join(dir, base))
            shutil.copyfile(os.path.join(dir, base), os.path.join(dir, base+'.original'))
  print("Halo MCC Ready to play without mods")
  menu()
  
def modded():
    for subdir, dirs, files in os.walk(dir):
        for filename in files:
            file = subdir + os.sep + filename
            base, ext = os.path.splitext(file)
            if ext == ".mod":
                shutil.move(os.path.join(dir, file),os.path.join(dir, base))
                shutil.copyfile(os.path.join(dir, base), os.path.join(dir, base+'.mod'))
    print("Halo MCC Ready to play with mods")
    menu()
  
def modlist(dir):
    #print("Mods:")
    modl=[]
    for subdir, dirs, files in os.walk(dir):
        for filename in files:
            file = subdir + os.sep + filename
            base, ext = os.path.splitext(file)
            if ext == ".mod":
                modl.append(filename)
    return modl
    menu()
  
def help():
    print("""
Choosing A will change Halo MCC into Vanilla mode. This allows the user to play online multiplayer and without any mod enabled.
Choosing B will change Halo MCC into Modded mode. This allows the user to play with mods, but may prevent the user from playing online multiplayer.
Choosing C will show the list of modded files that you have availible.
Choosing D will display this message.
Choosing E will exit this program.
To add a mod, make a copy of the original file and add ".original" to the file extension (e.g. file.map -> file.map.original).
Then add ".mod" to the file extension of the "mod" version of the file (e.g. file.map -> file.map.mod).
Both files should be in the same location as the original file.
Some(Few) mods do not require this modloader because they are allowed in online multiplayer.
If you need further help, or wish to contribute then please visit the Github page at https://github.com/ib4519894/MCC-Modloader
    """)
    menu()

# uses copyfile to back up file with the .original tag amended
# I recommend eventually swapping this method for a folder-based approach.
def backup_file(filepath, force=False):
  
    backfile = filepath + ".original"
    if not force and os.path.exists(backfile):
        return
    shutil.copyfile(filepath, backfile)

# backs up all .map files in directory as .map.original
def backup_originals(directory, gui=False):
    print("Not yet implemented!")
    pass
"""
    # pseudocode
    print("Backing up files...", end="")
    for each file in directory:
        if file ends in ".map":
            send it to backup_file()
            if gui=False:
                print(".", end="", dumpbuffer)
    print("Done.")
"""

# checks if directory is valid, then asks user
#  if they wish to back up their maps
def backup_prompt():
    if not verify_path():
        return

    print("""This program will backup all vanilla map files.
WARNING: This utility assumes all currently active .map files are vanilla.

Continue? y/n: """, end="")

    answer = ""
    while answer != "Y" and answer != "N":
        answer = input().upper()
    if answer == "Y":
        backup_originals(dir)

# checks the integrity of the filepath.
# If the path does not exist, retun false.
# Note that the path could theoretically point to any
#  arbitrary folder, but this is unlikely.
def verify_path():
    with open("settings.json", "r") as settings:
        dir = json.loads(settings.read())["directory"]
    if not os.path.exists(dir):
        print("Map directory not found!\nPlease change the directoy in settings.json")
        return False
    return True
