import os

#Directory / Folder to be scanned
source_dir = "/Users/wincheng/Downloads"


# Scan the directory and get
# an iterator of os.DirEntry objects
# corresponding to entries in it
# using os.scandir() method
obj = os.scandir(source_dir)
 
# List all files and directories
# in the specified source_dir
print("Files and Directories in '% s':" % source_dir)
for entry in obj :
    if entry.is_dir() or entry.is_file():
        print(entry.name)
 
#closing the scan
obj.close()