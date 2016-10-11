import sys
import argparse
import os
from argparse import RawTextHelpFormatter

import dictTextToImage
import excelParse

parser = argparse.ArgumentParser(description="""
    Conference Badge Creator\n
    Version: 1.0
    Author: Georgios A. Konstantopoulos
    Occupation: Electrical Engineering & Computer Engineering
                student at AUTh
    --
    Parse data from excel or dictionary.txt file and print it on your badge.
    Fast, Easy, Open Source.
    """, epilog='Enjoy!', formatter_class=RawTextHelpFormatter)
group = parser.add_mutually_exclusive_group()
parser.add_argument("-e","--exceldir", type=str, help='Absolute path to the excel file.')
parser.add_argument("-t","--template",type=str,help='Absolute path to the template image file.')
group.add_argument("-o","--overwrite",help='Use when you want to overwrite all files if they exist',action="store_true")
group.add_argument("-s","--skip",help='Use when don\'t want to overwrite existing files',action="store_true")
option = parser.parse_args()

def is_valid_file(parser,arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        parser.print_help()


def badge_creator():
    excel_dir = option.exceldir
    file_dir = option.template
    action = 0
    if option.skip:
        action = 2
        print "Skip Mode: ON."
    elif option.overwrite:
        action = 1
        print "Overwrite Mode: ON"
    else:
        print "Normal Mode: ON"
    excelParse.excel_to_dict(excel_dir)
    dictTextToImage.dict_to_img(file_dir,action)
if __name__ == '__main__':
    badge_creator()