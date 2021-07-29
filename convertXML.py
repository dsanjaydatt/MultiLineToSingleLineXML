#!/usr/bin/python

import os
import datetime

#change the path of xml input directory
#for windows
#for linux give normal path without r
path = r"E:\xml"
os.chdir(path)

def read_xml_file(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    mystr = ''.join([line.strip() for line in lines])
    time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
#change the directory wherever you want to save the output.
#Note that output directory should be different from your xml input directory.
#Else it gonna read the output file as well.
#If you want to keep the same directory then change the output file extension to something else.    
    filename = r"E:\Check\Out_#.xml"
    filename = filename.replace("#", time_now)
    ta = open(filename, 'a')
    a = ta.write(mystr + '\n')
    ta.close()


for file in os.listdir():

    if file.endswith('.xml'):

        file_path = f"{path}\{file}"

        read_xml_file(file_path)
    else:
        print('Unsupported file type Found.Processing supported files only..')

print("Conversion completed!")
