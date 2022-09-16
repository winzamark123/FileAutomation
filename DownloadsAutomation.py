import os
import shutil

#moving the files using shutil
def Move_Files(source_dir, file_name, dest_path):
    
    files_exist = os.path.exists(dest_path + "/" + file_name)

    #if the file is already in the folder 
    if files_exist:
        print("The file is already in the folder")
        return

    #updates the src_path with the folder's name + the file name
    src_path = source_dir + "/" + file_name

    shutil.move(src_path, dest_path)
    

class Scan_Files:
    #Starting Directory
    source_dir = "/Users/wincheng/Downloads"

    #Destination Directory
    CSV_dir = "/Users/wincheng/Downloads/CSV_Downloads/"
    Vids_dir = "/Users/wincheng/Downloads/Vids_Downloads/"
    Photos_dir = "/Users/wincheng/Downloads/Photos_Downloads/"
    PDF_dir = "/Users/wincheng/Downloads/PDF_Downloads/"

    #=======================================================================
    #STARTING THE PROGRAM
    #=======================================================================

    # Scan the directory and get an iterator of os.DirEntry objects
    # corresponding to entries in it using os.scandir() method
    obj = os.scandir(source_dir)
    
    # List all files and directories in the specified source_dir
    with os.scandir(source_dir) as itr:

    #starting the loop running through all files contained within the directory 
        for entry in itr :
            if entry.is_dir() or entry.is_file():

                #init destination as Downloads folder in case of other type of files
                file_name = entry.name
                dest_path = source_dir

                #ignore the current folders within the download directory
                if file_name.lower() in ["pdf_downloads", "csv_downloads", \
                    "photos_downloads", "vids_downloads"] or file_name.startswith("."):
                    continue
                
                #specifying the destination folder based on types of file
                if file_name.endswith(".png") or file_name.endswith(".jpeg") or file_name.endswith(".heic") or file_name.endswith(".HEIC"):
                    dest_path = Photos_dir

                elif file_name.endswith(".csv"):
                    dest_path = CSV_dir

                elif file_name.endswith(".pdf"):
                    dest_path = PDF_dir

                elif file_name.endswith(".mp4"):
                    dest_path = Vids_dir
                
                print(file_name)
                Move_Files(source_dir, file_name, dest_path)
        
        #closing the scan 
        obj.close() 





