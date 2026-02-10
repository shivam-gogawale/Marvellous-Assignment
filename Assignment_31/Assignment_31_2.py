# 2. Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extenntion.
# Usage: DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with.doc

import os
import sys
import CheckIsDirectoy

def ChangesFileExt(dirName,Ext1,Ext2):
    if CheckIsDirectoy.IsDirectory(dirName) == False:
        return

    fObj = open("LogfileQ2.txt",'w')

    border = "-"*60
    fObj.write(border + '\n')
    fObj.write('---------------------Assignment 32 Question 2---------------\n')
    fObj.write(border + '\n')

    for FolderName,subFolder,FileName in os.walk(dirName):
        for File in FileName:
            if File.endswith(Ext1):
                oldPath = os.path.join(FolderName, File)
                newFile = File.replace(Ext1, Ext2)
                newPath = os.path.join(FolderName, newFile)

                os.rename(oldPath, newPath)

                fObj.write(f"{oldPath} renamed to {newPath}\n")

    fObj.write(border + '\n')
    fObj.write('--------------------Assignment 32 Question 2----------------\n')
    fObj.write(border + '\n')

    fObj.close()

def main():

    if len(sys.argv) < 4:
        print("Enter Directory name and file extension")
    
    ChangesFileExt(sys.argv[1],sys.argv[2], sys.argv[3])



if __name__ == "__main__":
    main()