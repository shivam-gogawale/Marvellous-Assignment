# 4. Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time.
# Usage: DirectoryCopyExt.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp.

import os
import sys
import shutil


def MoveFileInFolder(Folder1,Folder2,ext):
    
    if not os.path.exists(Folder1):
        print("Enter valid file path")
        return
    
    if not os.path.isdir(Folder1):
        print("Enter valid directory name")
        return
     
    if not os.path.isdir(Folder2):
        os.makedirs(Folder2,exist_ok=True)

    fObj = open("LogfileQ4.txt",'w')

    border = "-"*60
    fObj.write(border + '\n')
    fObj.write('---------------------Assignment 32 Question 4---------------\n')
    fObj.write(border + '\n')

    for FolderName,subFolder,FileName in os.walk(Folder1):
        for File in FileName:
            name,FileExt = os.path.splitext(File)
            if(FileExt == ext):
        #    if File.endswith(ext): Alternet way
                src_path = os.path.join(FolderName,File)
                
                relative = os.path.relpath(src_path,Folder1) 
                
                dis_path = os.path.join(Folder2,relative)

                os.makedirs(os.path.dirname(dis_path),exist_ok=True)

                shutil.copy2(src_path,dis_path)
                fObj.write(f"{File} end with {ext} move in to {dis_path} \n")

    fObj.write(border + '\n')
    fObj.write('----------------End Assignment 32 Question 4----------------\n')
    fObj.write(border + '\n')

    fObj.close()

def main():

    if len(sys.argv) < 4:
        print("Enter Directory name .")
    
    MoveFileInFolder(sys.argv[1],sys.argv[2],sys.argv[3])


if __name__ == "__main__":
    main()