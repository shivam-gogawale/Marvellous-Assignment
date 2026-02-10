# 1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage: DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search

import os
import sys
import CheckIsDirectoy

def GetSearchFile(dirName,ExtName):
    if CheckIsDirectoy.IsDirectory(dirName) == False:
        return

    fObj = open("LogfileQ1.log",'w')

    border = "-"*60
    fObj.write(border + '\n')
    fObj.write('---------------Start Assignment 31 Question 1---------------\n')
    fObj.write(border + '\n')

    for FolderName,subFolder,FileName in os.walk(dirName):
        for File in FileName:
            if File.endswith(ExtName):
                print(File)
                fObj.write(f'File with extension {ExtName} is {File} \n')

    fObj.write(border + '\n')
    fObj.write('----------------End Assignment 31 Question 1----------------\n')
    fObj.write(border + '\n')

    fObj.close()

def main():

    if len(sys.argv) < 3:
        print("Enter Directory name and file extension")
    
    GetSearchFile(sys.argv[1],sys.argv[2])



if __name__ == "__main__":
    main()