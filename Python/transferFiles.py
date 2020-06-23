# -*- coding: utf-8 -*-
import os
import datetime as dt 
import pathlib
import shutil

# We want files where the modification of each file is between startDate and endDate
startDate = dt.datetime(2019, 6, 1).timestamp()
endDate = dt.datetime.now().timestamp()

folderSource = pathlib.Path(r'C:\Users\utilisateur\Documents\Source')
folderDestination = pathlib.Path(r'C:\Users\utilisateur\Documents\Destination')


def copyFile(file):
    if folderDestination != None : 
        shutil.copy2(file, folderDestination)
    else : 
        raise ValueError("The folder destination should be filled")

def getFiles():
    if folderSource != None:
        files = pathlib.Path(folderSource).glob("*.docx")
        for file in files:
            modificationDate = os.path.getctime(file)
            if modificationDate > startDate and modificationDate < endDate :
                copyFile(file)

    else : 
        raise ValueError("The folder source should be filled")


def main():
    getFiles()

if __name__ == "__main__":
    main()