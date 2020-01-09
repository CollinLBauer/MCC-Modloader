import sys
import hashlib

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


# This is mostly for testing.
def main():
  print(check_if_modded(sys.argv[1]))

main()