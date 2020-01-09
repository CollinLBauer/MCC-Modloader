import os
import sys
from pathlib import Path
import shutil
import hashlib

#Utilities file, used by gui and cmd to perform correct actions

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



BLOCKSIZE = 65536
# Compare SHA256 of current file with original file
# Return true if the same (vanilla)
# Return false if different (modded)
def check_if_modded(filename):
  
  # hash current file
  hasher = hashlib.sha256()
  with open(filename, "rb") as current:
    buf = current.read(BLOCKSIZE)
    while len(buf) > 0:
      hasher.update(buf)
      buf = current.read(BLOCKSIZE)
  curr_hash = hasher.hexdigest()

  # hash original file
  hasher = hashlib.sha256()
  with open(filename + ".original", "rb") as original:
    buf = original.read(BLOCKSIZE)
    while len(buf) > 0:
      hasher.update(buf)
      buf = original.read(BLOCKSIZE)
  orig_hash = hasher.hexdigest()
  
  #print(curr_hash) #debug
  #print(orig_hash) #debug

  # Compare hashes and return result
  for i in range(len(curr_hash)):
    if curr_hash[i] != orig_hash[i]:      
      return False # Files are different
  return True # Files are the same

#def launch(modded,steam):
#    if(shouldlaunch.get()):
#      window.destroy()
#      if(modded)
#        if(steam)
#          #subprocess.call([])
#      else:
#        if(steam)
#          #subprocess.call([])

