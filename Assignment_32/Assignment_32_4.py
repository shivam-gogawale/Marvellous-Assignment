# 4. Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory. Display execution time required for the script.

# Usage: Directory DusplicateRemoval.py "Demo"
# Demo is name of directory

import sys
import os
import hashlib
import time 


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

    fObj = open("LogQ4.txt","w")

    fObj.write(border + "\n")
    fObj.write("------------Assignment 32 Question 4--------------\n")
    fObj.write(border + "\n")
    fObj.write('\n\n\n')

    start_time = time.time()
    fObj.write(f'start time {start_time} \n')

    for Folder,SubFolder,Files in os.walk(DirtName):
        for File in Files:
            FileName= os.path.join(Folder,File)
            ret = CheckSum(FileName)

            if ret in files_Obj:
                files_Obj[ret].append(FileName)
            else:
                files_Obj[ret]= [FileName]


    dup = list(filter(lambda x: len(x) > 1,files_Obj.values()))

    count = 0
    for i in dup:
        for name in i:
            count += 1
            if count > 1:
                fObj.write(f"Deleted file name is {name} \n")
                os.remove(name)
        count = 0    

    end_time = time.time()
    fObj.write(f'End time {end_time} \n')

    fObj.write(f"Total time require to execute this script is {end_time - start_time}")

    fObj.write('\n\n\n')
    fObj.write(border + "\n")
    fObj.write("---------End Assignment 32 Question 4-------------\n")
    fObj.write(border + "\n")

    print("Delete duplicate files Successfully")
    fObj.close()


def main():
    if len(sys.argv) < 2:
        print("Enter Directory Name")
    else:
        GetCheckSum(sys.argv[1])

if __name__ == "__main__":
    main()