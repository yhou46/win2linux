#!/usr/bin/python3

import sys
import re
import argparse
import os


#-------------------------------------------------
# Functions
#-------------------------------------------------
def initializeCommandParser():
    parser = argparse.ArgumentParser(description = "change behaviors")

    # parser.add_argument( "-m", "--mode", type=str, required=True, choices=argsMode.values(),
    #                      help="Mode for this script")
    # parser.add_argument( "-f", "--file", type=str, required=True, help="File name for the change")

    parser.add_argument( "-l", "--linux", help="Linux format", action="store_true")
    parser.add_argument( "-w", "--windows", help="Windows format", action="store_true")
    parser.add_argument( "-p", "--path", type=str, help="path, default is current path")
    return parser


# Convert a linux path to windows path
# Should handle cases with spaces like:
# Test cases:
#
# 1. with spaces, should return path with quotes
# ./abc\ def/file -> ".\abc def\file"
#
# 2. handle different drives in windows subsystems: C drive is in pth /mnt/c/
# /mnt/c -> C:\
#
# 3. Check invalid path: in this case, throw exceptions
#
def linuxPathToWindows( linuxPath ):

    # Deal with drive symbol, like /mnt/c
    drivePattern = "/mnt/[a-z]"
    if re.match(drivePattern, linuxPath):
        driveSymbol = re.match(drivePattern, linuxPath).group(0)[-1].upper() # last character is drive symbol
        linuxPath = re.sub(drivePattern, driveSymbol+":", linuxPath)

    spaceFlag = False # by default no spaces in linux Path

    if linuxPath.find(" ") != -1:
        spaceFlag = True

    windowsPath = linuxPath.replace("\\", "")
    windowsPath = windowsPath.replace("/", "\\")

    if spaceFlag:
        return "\"" + windowsPath + "\""
    else:
        return windowsPath


def main(inputArgs):
    # Initialize command line parser and parse
    parser = initializeCommandParser()
    parsedArgs = parser.parse_args(inputArgs)

    # Get path
    path = os.getcwd() # Default to current working directory
    if parsedArgs.path != None:
        path = parsedArgs.path

    if parsedArgs.windows:
        print( linuxPathToWindows(path) )
    else: # linux
        print(path)

if __name__ == "__main__":
    

    # path = "test\\ 1/"

    # if len(sys.argv) > 1:
    #     path = sys.argv[1]
    #     print(path)

    # print(linuxPathToWindows(path) )
    main(sys.argv[1:])


    