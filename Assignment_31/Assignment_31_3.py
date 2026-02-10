# 3. Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.

# Usage: Directory Copy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.

import os
import sys
import shutil


def MoveFileInFolder(Folder1,Folder2):
    
    if not os.path.exists(Folder1):
        print("Enter valid file path")
        return
    
    if not os.path.isdir(Folder1):
        print("Enter valid directory name")
        return

    if not os.path.isdir(Folder2):
        os.makedirs(Folder2,exist_ok=True)

    fObj = open("LogfileQ3.txt",'w')

    border = "-"*60
    fObj.write(border + '\n')
    fObj.write('---------------------Assignment 32 Question 3---------------\n')
    fObj.write(border + '\n')

    for FolderName,subFolder,FileName in os.walk(Folder1):
        for File in FileName:
           src_path = os.path.join(FolderName,File)
           
           relative = os.path.relpath(src_path,Folder1) 
           
           dis_path = os.path.join(Folder2,relative)

           os.makedirs(os.path.dirname(dis_path),exist_ok=True)

           shutil.copy2(src_path,dis_path)
           fObj.write(f"{File} move in to {dis_path} \n")

    fObj.write(border + '\n')
    fObj.write('----------------End Assignment 32 Question 3----------------\n')
    fObj.write(border + '\n')

    fObj.close()

def main():

    if len(sys.argv) < 3:
        print("Enter Directory name .")
    
    MoveFileInFolder(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()