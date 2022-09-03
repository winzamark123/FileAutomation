import os
import shutil

#moving the files using shutil
def Move_Files(src_path, file_name, dest_path):
    shutil.move(src_path, dest_path + file_name)
    

class Scan_Files:
    #Starting Directory
    source_dir = "/Users/wincheng/Downloads"

    #Destination Directory
    CSV_dir = "/Users/wincheng/Downloads/CSV_Downloads/"
    Vids_dir = "/Users/wincheng/Downloads/Vids_Downloads/"
    Photos_dir = "/Users/wincheng/Downloads/Photos_Downloads/"
    PDF_dir = "/Users/wincheng/Downloads/PDF_Downloads/"

    #-------------------------------------
    # Scan the directory and get an iterator of os.DirEntry objects
    # corresponding to entries in it using os.scandir() method
    obj = os.scandir(source_dir)
    
    # List all files and directories in the specified source_dir
    print("Files and Directories in '% s':" % source_dir)
    with os.scandir(source_dir) as itr:

    #starting the loop running through all files contained within the directory 
        for entry in itr :
            if entry.is_dir() or entry.is_file():

                #init destination as Downloads folder in case of other type of files
                src_path = entry.name
                dest_path = source_dir 

                if src_path.endswith(".png") or src_path.endswith(".jpeg"):
                    dest_path = Photos_dir

                if src_path.endswith(".csv"):
                    dest_path = CSV_dir

                if src_path.endswith(".pdf"):
                    dest_path = PDF_dir

                if src_path.endswith(".mp4"):
                    dest_path = Vids_dir

                print(src_path)
                Move_Files(src_path, entry.name, dest_path)
        
        #closing the scan 
        obj.close() 






