import os 
import sys

path = "/home/oem/Downloads/"
dir = os.listdir( path )

for file in dir:
    print(file)

if os.path.isdir("/downloads/"):
     print("current dic")
    
