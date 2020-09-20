#!/usr/bin/env python3
from datetime import datetime
import sys, os, shutil, traceback

trash_path = '/Users/AR/.Trash/'

#get all arguements from cmd
arguments = sys.argv
if len(arguments) < 2:
    print('USAGE\n  trash [file ...]')
    exit(1)

error_flag = False
for trash_file_name in arguments[1:]:
    try:
        #append current directory to file/directory name
        trash_file_path = os.getcwd()+'/'+trash_file_name
        
        #check if specified file/directory exists
        if not os.path.exists(trash_file_path):
            print('trash:',trash_file_name,': No such file or directory')
            error_flag = True
            continue
        
        #check if there exists a file/directory with the same name in trash
        if os.path.exists(trash_path+trash_file_name):
            current_time = datetime.now().strftime("%H.%M.%S")

            #check if the file the file has an extension
            if '.' in trash_file_name and trash_file_name[0] != '.':
                trash_file_parts = trash_file_name.split('.')
                trash_file_name = '.'.join(trash_file_parts[:-1])+' '+current_time+'.'+trash_file_parts[-1]
            else:
                trash_file_name = trash_file_name+' '+current_time
        
        #move the file to trash
        shutil.move(trash_file_path, trash_path+trash_file_name)
    except Exception as err:
        print(err)
        error_flag = True
        continue

#check if there are any errors and set exit status to 1
if error_flag:
    exit(1)
