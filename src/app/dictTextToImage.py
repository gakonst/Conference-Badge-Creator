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


def dictionary_to_img(image_dir, action,group):
    #if group = 1 group everything, otherwise pile in folder called occupations
    # STATIC VALUES
    sizefont = 85
    backupsize = 65
    validinputs = ['y', 'Y', 'n', 'N', '']
    sizefontoccupation = 0.75 * float(sizefont)
    white = (255, 255, 255)
    black = (0, 0, 0)
    font_dir = "C:/Windows/Fonts/GOTHICB.ttf"
    occupations_font_dir = "C:/Windows/Fonts/Cocomat Light-trial.ttf"
    uni_font_dir =  "C:/Windows/Fonts/GOTHICI.TTF"
 # image_dir = 'test.jpg'

    #fontoccupation = ImageFont.truetype(occupations_font_dir, int(sizefontoccupation))

    # occupations=[u'Φοιτητής',u'Διδακτορικός',u'Καθηγητής']
    # Dict from Excel
    print(
        "\nReading dictionary from file. Each identity read from the excel" +
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
        if not read:
            if not os.path.exists("Badges Wave 2016"):
                mkdir("Badges Wave 2016")
            os.chdir("Badges Wave 2016")
            read = True
            if group:
                for j in range(0, len(occupations)):
                    if not os.path.exists(occupations[j]):
                        mkdir(occupations[j])
            else:
                if not os.path.exists("Occupations"):
                    mkdir("Occupations")
        size_uni_font = 40
        sizefontoccupation = 0.75 * float(sizefont)

        # Initializing needed variables and opening template.
        badgetemplate = Image.open(image_dir)
        username = dictionary[i]['Name'].decode('UTF-8')
        usersurname = dictionary[i]['Surname'].decode('UTF-8')
        occupation = dictionary[i]['Occupation'].decode('UTF-8')  # 'Occupation' for each person
        university = dictionary[i]['University'].decode('UTF-8')
        draw = ImageDraw.Draw(badgetemplate)

        x_padding = 63
        name_ypadding = 750
        surname_ypadding = name_ypadding + 85
        occupation_y_padding = 1010
        uni_y_padding = 1110

        #Adjust sizes so that text doesnt spill from black box
        if len(username) > 10:
            font = ImageFont.truetype(font_dir, backupsize)
            name_ypadding = name_ypadding+10
            # TODO
        else:
            font = ImageFont.truetype(font_dir, sizefont)
        draw.text((x_padding, name_ypadding), username, white, font=font)
        if len(usersurname) > 10:
            font = ImageFont.truetype(font_dir, backupsize)
            surname_ypadding = surname_ypadding+20
            # TODO
        else:
            font = ImageFont.truetype(font_dir, sizefont)
        draw.text((x_padding, surname_ypadding), usersurname, white, font=font)
        # occupationlength, occupationheight = draw.textsize(occupation, fontoccupation)

        #Type it twice with a +1 offset to simulate bold
        # Values and offsets modified through trial and error
        if len(occupation) > 25:
            sizefontoccupation = 0.63 * float(sizefontoccupation)
            x_padding = 55
            occupation_y_padding += 5
        elif len(occupation)>20:
            sizefontoccupation = 0.76 * float(sizefontoccupation)
        fontoccupation = ImageFont.truetype(occupations_font_dir,int(sizefontoccupation))
        draw.text((x_padding, occupation_y_padding), occupation, black,
                  font=fontoccupation)  # ypadding is static here because
        draw.text((x_padding+1, occupation_y_padding), occupation, black,
                  font=fontoccupation)

        #Hardcoded values for each university
        if university!='0':
            university_nl=university
            uni_words = university.split()
            if university=="THE AMERICAN COLLEGE OF THESSALONIKI":
                university_nl = "THE AMERICAN\nCOLLEGE OF\nTHESSALONIKI"
            elif len(university)>50:
                university_nl = u"ΕΘΝΙΚΟ ΚΑΙ\nΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ\nΑΘΗΝΩΝ/ΑΡΙΣΤΟΤΕΛΕΙΟ\nΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣΣΑΛΟΝΙΚΗΣ"
                size_uni_font = 0.70 * float(size_uni_font)
            elif len(university) > 40:
                university_nl = uni_words[0],uni_words[1]+"\n"+uni_words[2],uni_words[3]+"\n"+uni_words[4]
                size_uni_font = 0.75 * float(size_uni_font)
            elif len(university)>10:
                university_nl = university[:10]+university[10:].replace(" ","\n")
            if not group and len(university)<12:
                size_uni_font = 1.75 * float(size_uni_font)
            uni_font = ImageFont.truetype(uni_font_dir, int(size_uni_font))
            draw.text((x_padding, uni_y_padding), university_nl, black,
                  font=uni_font)
        # Saving...
        filename = dictionary[i]['Name'].decode('UTF-8') + "_" + dictionary[i]['Surname'].decode('UTF-8') + ".jpg"

        # Save each file to corresponding directory, based on their occupation
        # Action = 1 means everything gets overwritten
        # Action = 2 means if a file already exists do not overwrite it
        # Overwrite has Yes as default
        scriptdir = getcwd()
        # path3 = os.path.join(scriptdir,occupations)
        if group:
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
        else:
            path = os.path.join(scriptdir, "Occupations")
            path = os.path.join(path, filename)
            badgetemplate.save(path, dpi=(300.0, 300.0))

    print("[!] Done. Exiting.")
