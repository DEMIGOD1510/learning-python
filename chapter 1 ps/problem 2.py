import os

# Specify the directory path (use '.' for the current directory)
directory_path = input("chapter 1")

# Check if the path exists and is a directory
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print(f"\nContents of '{directory_path}':\n")
    
    # List the contents of the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            print(f"[DIR]  {item}")
        else:
            print(f"[FILE] {item}")
else:
    print("chapter 1")
