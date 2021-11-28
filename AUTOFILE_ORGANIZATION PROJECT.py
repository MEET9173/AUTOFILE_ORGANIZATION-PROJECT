#Automatic File Transfer Project
#Extension Wise File Transfer

#Import this three library
import os
import os.path
import shutil
import gui  #-->import from gui.py

def file_extension(f):
    split_tup = os.path.splitext(f)  #---> for split the file name and it extension
    return split_tup[1]

def directory_exists(temp_dest):
    return os.path.isdir(temp_dest)  #---> for check  path is already exits or not

def create_directory(d, dir):
    path=os.path.join(d, dir)
    os.mkdir(path)   #--->  TO Create directory

def file_exists(f):
    return os.path.exists(f)  #--->To check file is already exit or not 

def movefile(s, d):  #--->Use for move file from source to destination
    shutil.move(s, d)

source = gui.source
destination = gui.destination

source += '/'
destination += '/'

for f in os.listdir(source):

    extension=(file_extension(f))
    extension=extension[1:]  #---->Using slicing method for catch file extension name

    if extension == '':
        continue

    if not(directory_exists(destination + extension)): 
        create_directory(destination, extension)   

    s = source + f
    d = destination + extension + '/' + f

    if file_exists(d):         
        print(f, " already exists")
        continue

    movefile(s, d)  