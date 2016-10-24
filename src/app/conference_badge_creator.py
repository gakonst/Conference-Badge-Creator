import argparse
from argparse import RawTextHelpFormatter
from os import *
import dictTextToImage
import excelParse
import grid_print
import sys


def get_script_path():
    return path.dirname(path.realpath(sys.argv[0]))


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
parser.add_argument("-e", "--exceldir", type=str, help='Absolute path to the excel file.')
parser.add_argument("-t", "--template", type=str, help='Absolute path to the template image file.')
group.add_argument("-o", "--overwrite", help='Use when you want to overwrite all files if they exist',
                   action="store_true")
group.add_argument("-s", "--skip", help='Use when you don\'t want to overwrite existing files', action="store_true")
option = parser.parse_args()


def badge_creator():
    excel_dir = option.exceldir
    file_dir = option.template
    validinputs = ['Y', 'y', 'n', 'N']
    action = 0
    if option.skip:
        action = 2
        print "Skip Mode: ON."
    elif option.overwrite:
        action = 1
        print "Overwrite Mode: ON"
    else:
        print "Normal Mode: ON"
    folders = raw_input("Group based on occupation > ")
    while folders not in validinputs:
        folders = raw_input("Try again\nGroup? > ")
    if folders == 'Y' or folders == 'y':
        folders = True
    else:
        folders = False
    excelParse.excel_to_dict(excel_dir)
    dictTextToImage.dictionary_to_img(file_dir, action, folders)
    combine = raw_input("Do you want to combine all your files in a grid?\nCombine? [N] > ")
    while str(combine) not in validinputs:
        print "Invalid input. Try again."
        combine = input("Combine? [N] > ")
    if str(combine) == 'Y' or str(combine) == 'y':
        grid_size = input("Input grid size > ")
        # print "Current dir: "+getcwd()
        # wavedir = os.path.join(get_script_path(),"Badges Wave 2016")
        # print "Wave dir is "+wavedir
        # chdir(wavedir)
        # print "Current dir: "+getcwd()
        for dir in listdir(getcwd()):
            if dir == 'Combined':
                continue
            chdir(dir)
            print "Combining files in directory: " + str(dir)
            grid_print.combine_badges(grid_size)
            chdir('..')


if __name__ == '__main__':
    badge_creator()
