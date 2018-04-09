#!/usr/bin/python
#coding: utf-8
import os

def RenameFiles():
    #(1)get files names from a folder
    fileList = os.listdir("./prank")
    savedPath = os.getcwd()
    print(savedPath)
    os.chdir("./prank")
    print(os.getcwd())
    #(2)for each file, rename filename
    #os.rename(src, dst)
    for fileName in fileList:
        print("Old name: " + fileName)
        print("New name: " + fileName.translate(None, "0123456789"))
        os.rename(fileName, fileName.translate(None, "0123456789"))
    os.chdir(savedPath)

RenameFiles()
