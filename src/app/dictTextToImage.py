#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from excelParse import *
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os.path
from os import mkdir
from os import getcwd
Image.init()
Image.SAVE.keys()


def dict_to_img(image_dir,action):
    # STATIC VALUES
    sizefont = 45
    validinputs = ['y','Y','n','N','']
    sizefontoccupation = 0.75 * float(sizefont)
    colorName = (100, 100, 100)
    coloroccupation = (100, 100, 100)
    font_dir = 'C:/Windows/Fonts/Tahoma.ttf'
    # image_dir = 'test.jpg'
    font = ImageFont.truetype(font_dir, sizefont)
    fontoccupation = ImageFont.truetype(font_dir, int(sizefontoccupation))
    #occupations=[u'Φοιτητής',u'Διδακτορικός',u'Καθηγητής']
    occupations=['STUDENT','TEACHER','VOLUNTEER']
    # Dict from Excel
    print(
        "\nReading dictionary from file. Each identity read from the excel file is now being written on the template. Please wait...")
    users = open('Attendees.txt', 'r')
    dict = users.readlines()[0]
    dict = eval(dict)
    read = False
    for i in range(0, len(dict)):
        overwrite = 0
        if not read:
            if not os.path.exists("Badges Wave 2016"):
                mkdir("Badges Wave 2016")
            os.chdir("Badges Wave 2016")
            read = True
            if not os.path.exists(occupations[0]):
                mkdir(occupations[0])
            if not os.path.exists(occupations[1]):
                mkdir(occupations[1])
            if not os.path.exists(occupations[2]):
                mkdir(occupations[2])

        # Initializing needed variables and opening template.
        badgetemplate = Image.open(image_dir)
        width, height = badgetemplate.size  # Get image width-height to calculate coordinates for centered text
        fullname = dict[i]['Name'].decode('UTF-8') + " " + dict[i]['Surname'].decode('UTF-8')  # 'Name Surname'
        occupation = dict[i]['Occupation']        # 'Occupation' for each person
        occupation = occupation.decode('UTF-8')
        occupationlength, occupationheight = font.getsize(occupation)
        draw = ImageDraw.Draw(badgetemplate)
        namelength, nameheight = draw.textsize(fullname, font)  # Get size of string in pixels.
        # Calculate center by: padding1+textLength+padding2 \= totalWidth, where padding1 = padding 2
        xPadding = (width - namelength) / 2
        yPadding = (height - nameheight) / 2  # Ditto
        draw.text((xPadding, yPadding), fullname, colorName, font=font)
        occupationlength, occupationheight = draw.textsize(occupation, fontoccupation)
        xPadding = (width - occupationlength) / 2
        yPadding = (height / 2) + 50
        draw.text((xPadding, yPadding), occupation, coloroccupation,
                  font=fontoccupation)  # yPadding is static here because
        # we want it to be independent of text height, always in the same spot.
        # Saving...
        filename = dict[i]['Name'].decode('UTF-8') + "_" + dict[i]['Surname'].decode('UTF-8') + ".jpeg"

        print("[+] Saving: " + filename)
        # Save each file to corresponding directory, based on their occupation
        # Action = 1 means everything gets overwritten
        # Action = 2 means if a file already exists do not overwrite it
        # Overwrite has Yes as default
        scriptDir = getcwd()
       # path3 = os.path.join(scriptDir,occupations)
        if occupation == occupations[0]:
            path1 = os.path.join(scriptDir, occupations[0])
            path1 = os.path.join(path1, filename)
            if (action==1):
                badgetemplate.save(path1)
            elif os.path.isfile(path1):
                if(action == 2):
                    continue
                print ("[!] File Exists.")
                overwrite = raw_input("Overwrite? [Y] > ")
                while str(overwrite) not in validinputs:
                    print("[-] Invalid input.")
                    overwrite = raw_input("Overwrite? [Y] > ")
                if str(overwrite) in ['y','Y','']:
                    print ("[+] Overwriting "+filename)
                    badgetemplate.save(path1)
                else:
                    print ("[-] Skipping...")
                    continue
            else:
                badgetemplate.save(path1)

        elif occupation ==  occupations[1]:
            path2 = os.path.join(scriptDir,  occupations[1])
            path2 = os.path.join(path2, filename)
            if (action==1):
                badgetemplate.save(path2)

            elif os.path.isfile(path2):
                if (action == 2):
                    continue
                print("[!] File Exists.")
                overwrite = raw_input("Overwrite? [Y] > ")
                while str(overwrite) not in validinputs:
                    print("[-] Invalid input.")
                    overwrite = raw_input("Overwrite? [Y] > ")
                if str(overwrite) in ['y', 'Y','']:
                    print("[+] Overwriting " + filename)
                    badgetemplate.save(path2)
                else:
                    print("[-] Skipping...")
                    continue
            else:
                badgetemplate.save(path2)
        elif occupation == occupations[2]:
            path3 = os.path.join(scriptDir,  occupations[2])
            path3 = os.path.join(path3, filename)
            if (action==1):
                badgetemplate.save(path3)
            elif os.path.isfile(path3):
                if (action == 2):
                    continue
                print("[!] File Exists.")
                overwrite = raw_input("Overwrite? [Y] > ")
                while str(overwrite) not in validinputs:
                    print("[-] Invalid input.")
                    overwrite = raw_input("Overwrite? [Y] > ")
                if str(overwrite) in ['y', 'Y','']:
                    print("[+] Overwriting " + filename)
                    badgetemplate.save(path3)
                else:
                    print("[-] Skipping...")
                    continue
            else:
                badgetemplate.save(path3)
        #else:
         #  path3 = os.path.join(path3, filename)
          # badgetemplate.save(path3)
    print("[!] Done. Exiting.")
