import os

folders = input("Enter the folder names separated by space: ").split(" ")
print(folders)

for folder in folders:
    
    try:
        files = os.listdir(folder)
    
    except FileNotFoundError:
        print("No such file or directory: " + folder)
        continue;

    except PermissionError:
        print("You don't have enough permissions for the directory : " + folder)
        continue;

    print(folder)
    print("=========")
    
    for file in files:
        print(file)
    
    print(" ")
    
