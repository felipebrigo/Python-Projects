#PHOTO ORGANIZER
from PIL import Image
import os
import shutil

#Global variables declared or initialized
general_data={}
complete_data_list=[]
photo_files=[]
folder_list=[]
extentions=["jpg", "jpeg", "gif", "tiff", "raw"]

#Capture all files in the main path where the program will start to find out pics
def path(path_start):
    global folder_list, photo_files
    files=os.listdir(path_start)
    for file in files:
        if not "." in file:
            folder_list=file
        for a in range (0,len(extentions)):
            if extentions[a] in file.lower():
                photo_files.append(file)
    print(photo_files)

#Capture all photo's data and put on a list
def data_photo(path_start, photo_files):
    global complete_data_list
    for b in range(0,len(photo_files)):
        im=Image.open(path_start + photo_files[b])
        info=im._getexif()
        if 36867 in info:
            complete_date=info[36867]
            date_strip=dt.strptime(date,"%Y:%m:%d %H:%M:%S")
            month=date_strip.strftime("%B")
            year=date_strip.strftime("%Y")
            general_data["Original_Path"]=im
            general_data["File"]=photo_files[b]
            general_data["Year"]=year
            general_data["Month"]=month
            complete_data_list.append(general_data.copy())
        else:
            general_data["Original_Path"]=im
            general_data["File"]=photo_files[b]
            general_data["Year"]="No_Data"
            general_data["Month"]="No_Data"
            complete_data_list.append(general_data.copy())    
            
#--------------------------------

#Creating specific folders and subfolders
def create_folder():
    for year_list in complete_data_list:
        year=general_data["Year"].
                    

path_end=os.path.join(path_start,pic_year,pic_month)
os.makedirs(path_end)
shutil.move(path_start,path_end)    
os.path.basename()    
os.path.join()

#To move pointer inside the path and paste all photo's files
os.chdir(path_start, pic_year, pic_month)

#Main program
path_start=os.getcwd()
path(path_start)
data_photo(path_start, photo_files)


#Generate a .txt report into workspace with from (path) to (new path) and size of the file
report={}
report.update{'filename - from - to - size'}
