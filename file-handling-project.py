from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("\nPlease tell your file name- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("\nwhat you want to write in this file- ")
                fs.write(data)
 
            print(f"\nFILE CREATED SUCCESSFULLY")

        else:
            print("This file already exists")
    
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("\nWhich file do you want to read- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("\nFile readed successfully")

        else:
            print("\nThe file does not exist")

    except Exception as err:
        print(f"\nAn error occured as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("\nWhich file do you want to update- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("\nPress 1 for changing the name of your file- ")
            print("Press 2 for overwriting the data of your file- ")
            print("Press 3 for appending some content in your file- ")
        
            response = int(input("\nTell your response- "))
        
            if response == 1:
                name2 = input("\nTell your new file name- ")
                p2 = Path(name2)
                p.rename(p2)
        
            if response == 2:
                with open(p, 'w') as fs:
                    data = input("\nTell what you want to write this will overwrite the data- ")
                    fs.write(data)
        
            if response == 3:
                with open(p, 'a') as fs:
                    data = input("\nTell what you want to append- ")
                    fs.write(" "+data)

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("\nWhich file you want to delete- ")
        p = Path(name)
        
        if p.exists() and p.is_file():
            os.remove(name)
        
            print("\nFile removed successfully")
        
        else:
            print("\nNo such file exists\n")

    except Exception as err:
        print(f"An error occured as {err}")
    

print("\nPress 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("\nEnter your response- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()