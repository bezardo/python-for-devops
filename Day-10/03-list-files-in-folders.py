import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None  # returning as a tuple
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)  # refer bottom x,y example we are unpacking tuple data and assigning as vars
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()


Tuple Packing and Unpacking
You can pack multiple values into a tuple and unpack them into separate variables.

coordinates = (3, 4)  # line 6 , 8 , 10
x, y = coordinates  # line 16
