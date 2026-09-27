"""
Module 2 — Activity: File Sorting with os and shutil
Student: Manganti, Justin Rey A.
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
i built a python script that automatically organize files in a folder by their file extentension, 
it scans a folder, checks each file type like(.pdf, .jpg, .txt) creates matching subfolders,
and move the files into them.



============================================
KEY VOCABULARY
============================================
- os module: pythons tool for interacting woth your computers folders and files
- shutil module: tool for copying and moving files around
- file path: the web address for a file on your computer
- directory:plain text word for a folder
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---
list_of_files = os.listdir()
print(list_of_files)



filename = input("enter file: ")
if os.path.exists(filename):
    print("it exists")

else:
    print("it does not exist")


#counter
img = 0
doc = 0
vid = 0
other = 0

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
        doc +=1
    elif filename.endswith(".pptx"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
        doc +=1
    elif filename.endswith(".png"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
        img += 1
    elif filename.endswith(".jpeg"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
        img += 1
    elif filename.endswith(".mp4"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
        vid +=1
    elif filename.endswith(".mov"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
        vid +=1

print(f"="*30)
print("Folder Summary")
print(f"Images moved: {img}")
print(f"Documents moved: {doc}")
print(f"Videos moved: {vid}")
print(f"Others moved: {other}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
trying to move file before checking if the target folder existed which caused an error
fixed it by adding "os.path.exists" to create the folder first before moving any files

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
this works just like real world automation that sorts downloaded files, organize student assignments 
by class, or back up files automatically to save time on daily repetitive task
"""
