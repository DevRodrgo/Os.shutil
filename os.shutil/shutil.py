#!usr/bin/python

import os 
import sys
import shutil
import base64
import /home/oem/Downloads/portifolio/PortifolioRodrigo.io/encrypted.py

def system(self, argv, base64Decode):
    self.start(sys.version)
    self.execute(sys.stdin)
    if self.start:
        exit()
    elif self.execute:
        base64Decode(system)
    sys.argv(sys.path)


dir = input("Enter dic name:")

path = "dir"
dir = os.listdir( path )
for file in dir:
    print(file)

answer = input("do u want continue?")

if answer == "yes":
    print("we are starting") 
    exit()

if os.path.isdir("dir"):
     print("current dic")
else:
    print("isnt dic")

try:
    shutil.rmtree(dir)

except OSError as e:
    print("Error: %e - %e." % (e.filename, e.strerror))

