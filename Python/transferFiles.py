# -*- coding: utf-8 -*-
import os
import datetime as dt 
import pathlib
import shutil

# We want files where the modification of each file is between startDate and endDate
start_date = dt.datetime(2019, 6, 1).timestamp()
end_date = dt.datetime.now().timestamp()

folder_source = pathlib.Path(r'C:\Users\utilisateur\Documents\Source')
folder_destination = pathlib.Path(r'C:\Users\utilisateur\Documents\Destination')


def copy_file(file):
    if folder_destination.exists() :
        shutil.copy2(file, folder_destination)
    else : 
        raise AttributeError("The folder destination doesn't exist :", folder_destination)

def get_files():
    if folder_source.exists() :
        files = pathlib.Path(folder_source).glob("*.docx")
        for file in files:
            modification_date = os.path.getctime(file)
            if modification_date > start_date and modification_date < end_date :
                copy_file(file)
    else : 
        raise AttributeError("The folder source doesn't exist :", folder_source)


def main():
    get_files()

if __name__ == "__main__":
    main()