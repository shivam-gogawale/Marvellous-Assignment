
import os

def IsDirectory(dirName):
    Ret = True

    if os.path.exists(dirName) == False:
        print("Please Enter valid directory")
        Ret = False
        return 
   
    if os.path.isdir(dirName) == False:
        print("It is not directory")
        Ret = False
        return
    
    return Ret
