from pathlib import Path
import os


def readFileAndFolder():

    path = Path(__file__).parent
    items = list(path.iterdir())

    for i, items in enumerate(items):
        print(f"{i+1} : {items.name}")


def createFile():
    try:
        readFileAndFolder()
        name = input("Write file name:- ")
        p = Path(__file__).parent / name

        if not p.exists():

            with open(p, "w") as fs:
                data = input("write file content:- ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")

        else:
            print("File already exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def readFile():
    try:
        readFileAndFolder()
        name = input("write which file you want to read:- ")
        p = Path(__file__).parent / name

        if p.exists() and p.is_file():

            with open(p, "r") as fr:
                data = fr.read()
                print(data)

            print("READ COMPLETED")

        else:
            print("This file doesn't exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def updateFile():
    try:
        readFileAndFolder()
        name = input("which file you want to update:- ")
        p = Path(__file__).parent / name

        if p.exists() and p.is_file():
            print("press 1 to rename this file:- ")
            print("press 2 to overwrite the content in this file:- ")
            print("press 3 to append the content in this file:- ")

            action = int(input("please tell your response :- "))

            if action == 1:
                data = input("write a new name for this file:- ")
                p2 = Path(__file__).parent / data
                p.rename(p2)

                print("RENAME COMPLETED")

            elif action == 2:
                with open(p, "w") as fs:
                    data = input("write an overwrite content for this file:- ")
                    fs.write(data)

                print("OVERWRITE COMPLETED")

            elif action == 3:
                with open(p, "a") as fs:
                    data = input("write to append the content in the file:- ")
                    fs.write(" " + data)

                print("APPEND COMPLETED")

        else:
            print("File with this name doesn't exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def deleteFile():
    try:
        readFileAndFolder()
        file = input("which file you want to delete:- ")
        p = Path(__file__).parent / file

        if p.exists() and p.is_file():
            os.remove(file)

            print("FILE DELETED SUCCESSFULLY")

        else:
            print("No such file exist")

    except Exception as err:
        print(f"An error occurred as {err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("please tell your response:- "))

if check == 1:
    createFile()

elif check == 2:
    readFile()

elif check == 3:
    updateFile()

elif check == 4:
    deleteFile()
