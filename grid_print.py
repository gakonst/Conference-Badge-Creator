#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from PIL import Image
from os import *
import random

def get_script_path():
    return path.dirname(path.realpath(sys.argv[0]))

def combine_badges(grid_size):
    offset = 10
    badge_x, badge_y = 886, 1276
    dims = grid_size * (badge_x + offset), grid_size * (badge_y + offset)
    groups = grid_size * grid_size 
    x,y = 0,0
    usedfiles = []
    no_total_files = len(listdir(getcwd()))
    page_number= 0
    npages = no_total_files / groups + 1
    for _ in range(npages):
        i = 0
        j = 0
        page = Image.new('RGB', dims, (255, 255, 255))
        items = listdir(unicode(getcwd()))
        for filename in items:
            #print (item)
            #filename = item.decode('UTF-8')
            #print (filename)
            if filename.endswith(".jpg") and (filename not in usedfiles):
                img = Image.open(filename)
                x,y = i*(badge_x+offset),j*(badge_y+offset)
                i+=1
                if i == grid_size:
                    j+=1
                    i = 0
                page.paste(img, (x, y))
                usedfiles.append(filename)
            else:
                continue
            if j == grid_size and i==0:
                break

        page_number += 1
        #print ("Printing page:" + str(page_number))
        occupationDir = getcwd()
        occupationDir = path.split(occupationDir)[1]
        filename = str(occupationDir)+"_"+str(page_number)+".jpeg"
        chdir('..')
        if not path.exists("Combined"):
            mkdir("Combined")
        chdir('Combined')
        page.save(filename,dpi=(300.0, 300.0))
        chdir('..')
        chdir(occupationDir)
        if len(usedfiles) == no_total_files:
            break
