# 2. Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.

# Usage: Directory Dusplicate.py "Demo"
# Demo is name of directory.

import sys
import os
import hashlib


def CheckSum(File):
    fObj = open(File,'rb')

    hObj = hashlib.md5()

    buffer = fObj.read(1024)

    while len(buffer) > 0:
        hObj.update(buffer)
        buffer = fObj.read(1024)

    fObj.close()
    
    return hObj.hexdigest()

def GetCheckSum(DirtName):
    border = "-"*50
    files_Obj = {}
    if not os.path.exists(DirtName):
        print("This Directory is not present")
        return

    if not os.path.isdir(DirtName):
        print("This is not directory")
        return

    fObj = open("Log.txt","w")

    fObj.write(border + "\n")
    fObj.write("------------Assignment 32 Question 2--------------\n")
    fObj.write(border + "\n")
    fObj.write('\n\n\n')

    for Folder,SubFolder,Files in os.walk(DirtName):
        for File in Files:
            FileName= os.path.join(Folder,File)
            ret = CheckSum(FileName)

            if ret in files_Obj:
                files_Obj[ret].append(FileName)
            else:
                files_Obj[ret]= [FileName]


    dup = list(filter(lambda x: len(x) > 1,files_Obj.values()))

    for i in dup:
        for name in i:
            fObj.write(f'Name of Duplicate file is {name} \n')


    fObj.write('\n\n\n')
    fObj.write(border + "\n")
    fObj.write("---------End Assignment 32 Question 2-------------\n")
    fObj.write(border + "\n")

    print("Fetch duplicate files Successfully")
    fObj.close()

def main():
    if len(sys.argv) < 2:
        print("Enter Directory Name")
    else:
        GetCheckSum(sys.argv[1])

if __name__ == "__main__":
    main()