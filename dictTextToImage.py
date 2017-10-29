#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from excelParse import *

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import os
import os.path
from os import mkdir

Image.init()
Image.SAVE.keys()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MAIN_FONT = "C:/Windows/Fonts/GOTHICB.ttf"
MAIN_FONT_SIZE = 85
OCCUPATIONS_FONT = "C:/Windows/Fonts/Cocomat Light-trial.ttf"
OCCUPATIONS_FONT_SIZE = 0.75 * float(MAIN_FONT_SIZE)
UNIVERSITIES_FONT =  "C:/Windows/Fonts/GOTHICI.TTF"
UNIVERSITIES_FONT_SIZE = OCCUPATIONS_FONT_SIZE

EXCESS_FONT_SIZE = 65

def initialize_occupation_directories(occupations, size):
    read = False
    for i in range(size):
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

def draw_data_to_img(img, name, surname, occupation, university):
        # Values and offsets modified through trial and error

        ######################### HACKS TO FIT TEXT PROPERLY TO TEMPLATE  ####################################

        # pad for proper styling on template
        name_xpad = 63
        name_ypad = 750

        surname_xpad = name_xpad
        surname_ypad = name_ypad + 85

        occupation_xpad = name_xpad
        occupation_ypad = 1010

        university_xpad = name_xpad
        university_ypad = 1110
        
        ############# Adjust sizes so that text doesnt spill from black box
        name_font = ImageFont.truetype(MAIN_FONT, MAIN_FONT_SIZE)
        if len(name) > 10:
            name_font = ImageFont.truetype(MAIN_FONT, EXCESS_FONT_SIZE)
            name_ypad += 10

        surname_font = ImageFont.truetype(MAIN_FONT, MAIN_FONT_SIZE)
        if len(surname) > 10:
            surname_font = ImageFont.truetype(MAIN_FONT, EXCESS_FONT_SIZE)
            surname_ypad += 20

        occupation_font = ImageFont.truetype(OCCUPATIONS_FONT,int(OCCUPATIONS_FONT_SIZE))
        if len(occupation) > 25:
            OCCUPATIONS_FONT_SIZE = 0.63 * float(OCCUPATIONS_FONT_SIZE)
            occupation_xpad = 55
            occupation_ypad += 5
        elif len(occupation) > 20:
            OCCUPATIONS_FONT_SIZE = 0.76 * float(OCCUPATIONS_FONT_SIZE)

        if university!='0':
            university_nl = university
            uni_words = university.split()
            if university == "THE AMERICAN COLLEGE OF THESSALONIKI":
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
            uni_font = ImageFont.truetype(UNIVERSITIES_FONT, int(size_uni_font))

        ######################### END OF HACKS ####################################

        draw = ImageDraw.Draw(img)
        draw.text((name_xpad, name_ypad), name, white, name_font)
        draw.text((surname_xpad, surname_ypad), surname, white, surname_font)
        draw.text((x_pad, occupation_y_pad), occupation, black, OCCUPATIONS_FONT
        draw.text((x_pad+1, occupation_y_pad), occupation, black, OCCUPATIONS_FONT) # Simulate bold with +1 offset
        if university != '0':
            draw.text((x_pad, uni_y_pad), university_nl, black, uni_font)

def save_image(img, fname, occupation, occupations, group, action)
        # Save each file to corresponding directory
        scriptdir = os.getcwd()
        if group:
            for k in range(len(occupations)):
                if occupation == occupations[k]:
                    path = os.path.join(scriptdir, occupations[k]) # Dir/Occupation
                    path = os.path.join(path, fname)
                    if action == 1: # overwrite mode
                        print("[+] Saving: " + fname)
                        img.save(path, dpi=(300.0, 300.0))
                    elif os.path.isfile(path): # if file exists and action is not overwrite
                        if action == 2: # skip mode
                            continue
                        print("[!] "+fname+" exists.")
                        overwrite = raw_input("Overwrite? [Y] > ")
                        while overwrite.lower() not in ['y','n']:
                            print("[-] Invalid input.")
                            overwrite = raw_input("Overwrite? [Y] > ")
                        if overwrite.lower() in ['y', '']:
                            print("[+] Overwriting " + fname+"\n")
                            img.save(path, dpi=(300.0, 300.0))
                        else:
                            print("[-] Skipping...\n")
                            continue
                    else:
                        print("[+] Saving: " + fname)
                        img.save(path, dpi=(300.0, 300.0))
        else:
            path = os.path.join(scriptdir, "Occupations")
            path = os.path.join(path, fname)
            img.save(path, dpi=(300.0, 300.0))

def dictionary_to_img(image_dir, data_file, action, group):
    with open(data_file) as f:
        dictionary = eval(f.read()) # CAREFUL
    occupations = []
    for i in range(len(dictionary)):
        if dictionary[i]['Occupation'] not in occupations:
            occupations.append(dictionary[i]['Occupation'])

    initialize_occupation_directories(occupations, len(dictionary))

    # Is this needed?
    #for i in range(0,len(occupations)):
    # occupations[i]= unicode(occupations[i],"utf-8")

    for i in range(len(dictionary)):
        name = dictionary[i]['Name'].decode('UTF-8')
        surname = dictionary[i]['Surname'].decode('UTF-8')
        occupation = dictionary[i]['Occupation'].decode('UTF-8')
        university = dictionary[i]['University'].decode('UTF-8')

        img = Image.open(image_dir)
        draw_data_to_img(img, name, surname, occupation, university)
        fileName = dictionary[i]['Name'].decode('UTF-8') + "_" + dictionary[i]['Surname'].decode('UTF-8') + ".jpg"
        save_image(img, fileName, occupation, occupations, group, action)
    print("[!] Done. Exiting.")
