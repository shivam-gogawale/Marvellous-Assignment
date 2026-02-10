# 1. Design automation script which accept directory name and display checksum of all files.

# Usage: DirectoryChecksum.py "Demo"
# Demo is name of directory.

import sys
import os
import hashlib


def CheckSum(File):
    Fobj = open(File,"rb")

    hObj = hashlib.md5()

    buffer = Fobj.read(1024)

    while len(buffer) > 0:
        hObj.update(buffer)
        buffer = Fobj.read(1024)

    Fobj.close()

    return hObj.hexdigest()

def GetCheckSum(DirtName):
    border = "-"*50
    if not os.path.exists(DirtName):
        print("This Directory is not present")
        return

    if not os.path.isdir(DirtName):
        print("This is not directory")
        return

    fObj = open("consoleQ1.log","w")

    fObj.write(border + "\n")
    fObj.write("------------Assignment 32 Question 1--------------\n")
    fObj.write(border + "\n")
    fObj.write('\n\n\n')

    for Folder,SubFolder,Files in os.walk(DirtName):
        for File in Files:
            FileName= os.path.join(Folder,File)
            ret = CheckSum(FileName)
            fObj.write(f"Check sum of {File} is {ret} \n")

    fObj.write('\n\n\n')
    fObj.write(border + "\n")
    fObj.write("---------End Assignment 32 Question 1-------------\n")
    fObj.write(border + "\n")

    print("Fetch Successfully checksum")
    fObj.close()

def main():
    if len(sys.argv) < 2:
        print("Enter Directory Name")
    else:
        GetCheckSum(sys.argv[1])

if __name__ == "__main__":
    main()