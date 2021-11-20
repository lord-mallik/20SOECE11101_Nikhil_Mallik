# # # Project Name : Auto File Organization
# # # Name : Nikhil Mallik
# # # Enrollment No. : 20SOECE11101
# # # Class : 3CEC



import os
import shutil

# reading the folder's file
folderpath = r"C:\Users\nikhi\Desktop\Notes\Python"
os.chdir(folderpath)
os.getcwd()

# # check the files
os.listdir()

# #get extension
list_extension = []
for fl in os.listdir():
    extension = fl.split(".")[-1]
    list_extension.append(extension)
    # print(list_extension)

list_extension = set(list_extension)
print(list_extension)
print(len(list_extension))

# # create a folder on the desktop
path = os.environ["UserProfile"] + "\\" + "Desktop" + "\\" + "New file"
print(path)
os.mkdir(path)
try:
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)

# # we can transfer the file with specific folder
for ex in list_extension:
    print(ex, end=",")
    os.mkdir(path + "\\" + ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl, path + "\\" + ex)