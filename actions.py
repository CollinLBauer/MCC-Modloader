import os
import sys
from pathlib import Path
import shutil 

#Utilities file, used by gui to perform correct actions

def vanilla(dir):
  for subdir, dirs, files in os.walk(dir):
    for filename in files:
        file = subdir + os.sep + filename
        base, ext = os.path.splitext(file)
        if ext == ".original":
            shutil.move(os.path.join(dir, file),os.path.join(dir, base))
            shutil.copyfile(os.path.join(dir, base), os.path.join(dir, base+'.original'))
  print("Halo MCC Ready to play without mods")
  return False


def modded(dir):
  for subdir, dirs, files in os.walk(dir):
    for filename in files:
      file = subdir + os.sep + filename
      base, ext = os.path.splitext(file)
      if ext == ".mod":
        shutil.move(os.path.join(dir, file),os.path.join(dir, base))
        shutil.copyfile(os.path.join(dir, base), os.path.join(dir, base+'.mod'))
  print("Halo MCC Ready to play with mods")
  return True


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

#def launch(modded,steam):
#    if(shouldlaunch.get()):
#      window.destroy()
#      if(modded)
#        if(steam)
#          #subprocess.call([])
#      else:
#        if(steam)
#          #subprocess.call([])

