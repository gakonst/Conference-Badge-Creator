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


def dictionary_to_img(image_dir, action):
    # STATIC VALUES
    sizefont = 85
    backupsize = 65
    validinputs = ['y', 'Y', 'n', 'N', '']
    sizefontoccupation = 0.75 * float(sizefont)
    colorname = (255, 255, 255)
    coloroccupation = (0, 0, 0)
    font_dir = "C:/Windows/Fonts/GOTHICB.ttf"
    occupations_font_dir = "C:/Windows/Fonts/GOTHIC.ttf"

    # image_dir = 'test.jpg'

    fontoccupation = ImageFont.truetype(occupations_font_dir, int(sizefontoccupation))
    # occupations=[u'Φοιτητής',u'Διδακτορικός',u'Καθηγητής']
    # Dict from Excel
    print(
        "\nReading dictionaryionary from file. Each identity read from the excel" +
        "file is now being written on the template. Please wait...")
    users = open('Attendees.txt', 'r')
    dictionary = users.readlines()[0]
    users.close()
    dictionary = eval(dictionary)
    read = False
    occupations = []
    for i in range(0, len(dictionary)):
        if dictionary[i]['Occupation'] not in occupations:
            occupations.append(dictionary[i]['Occupation'])
    for i in range(0,len(occupations)):
        occupations[i]= unicode(occupations[i],"utf-8")
    for i in range(0, len(dictionary)):
        font = ImageFont.truetype(font_dir, sizefont)
        if not read:
            if not os.path.exists("Badges Wave 2016"):
                mkdir("Badges Wave 2016")
            os.chdir("Badges Wave 2016")
            read = True
            for j in range(0, len(occupations)):
                if not os.path.exists(occupations[j]):
                    mkdir(occupations[j])

        # Initializing needed variables and opening template.
        badgetemplate = Image.open(image_dir)
        # width, height = badgetemplate.size  # Get image width-height to calculate coordinates for centered text
        username = dictionary[i]['Name'].decode('UTF-8')
        usersurname = dictionary[i]['Surname'].decode('UTF-8')
        # fullname = username + "\n" + usersurname   # 'Name Surname'
        # fullname = fullname.upper()
        occupation = dictionary[i]['Occupation'].decode('UTF-8')  # 'Occupation' for each person
        draw = ImageDraw.Draw(badgetemplate)
        # namelength, nameheight = draw.textsize(fullname, font)  # Get size of string in pixels.
        # Calculate center by: padding1+textLength+padding2 \= totalWidth, where padding1 = padding 2
        # xpadding = (width - namelength) / 2
        # ypadding = (height - nameheight) / 2  # Ditto\
        ypadding = 680 + 37.1
        xpadding = 74
        draw.text((xpadding, ypadding), username, colorname, font=font)
        occupation_padding = ypadding + 250 + 34.9

        if len(usersurname) > 10:
            font = ImageFont.truetype(font_dir, backupsize)
            ypadding += 100
            # TODO
        else:
            ypadding += 100
        draw.text((xpadding, ypadding), usersurname, colorname, font=font)
        # occupationlength, occupationheight = draw.textsize(occupation, fontoccupation)
        draw.text((xpadding, occupation_padding), occupation, coloroccupation,
                  font=fontoccupation)  # ypadding is static here because
        # we want it to be independent of text height, always in the same spot.
        # Saving...
        filename = dictionary[i]['Name'].decode('UTF-8') + "_" + dictionary[i]['Surname'].decode('UTF-8') + ".jpg"

        # Save each file to corresponding directory, based on their occupation
        # Action = 1 means everything gets overwritten
        # Action = 2 means if a file already exists do not overwrite it
        # Overwrite has Yes as default
        scriptdir = getcwd()
        # path3 = os.path.join(scriptdir,occupations)
        for k in range(0, len(occupations)):
            if occupation == occupations[k]:
                path = os.path.join(scriptdir, occupations[k])
                path = os.path.join(path, filename)
                if action == 1:
                    print("[+] Saving: " + filename)
                    badgetemplate.save(path, dpi=(300.0, 300.0))
                elif os.path.isfile(path):
                    if action == 2:
                        continue
                    print("[!] "+filename+" exists.")
                    overwrite = raw_input("Overwrite? [Y] > ")
                    while str(overwrite) not in validinputs:
                        print("[-] Invalid input.")
                        overwrite = raw_input("Overwrite? [Y] > ")
                    if str(overwrite) in ['y', 'Y', '']:
                        print("[+] Overwriting " + filename+"\n")
                        badgetemplate.save(path, dpi=(300.0, 300.0))
                    else:
                        print("[-] Skipping...\n")
                        continue
                else:
                    print("[+] Saving: " + filename)
                    badgetemplate.save(path, dpi=(300.0, 300.0))

    print("[!] Done. Exiting.")
