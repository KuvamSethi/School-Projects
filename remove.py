import os

file = input("Enter file name : ")
file = f"{file}.txt"

if os.path.isfile(file):
    os.remove(file)
else:
    print(f"{file} not present.")