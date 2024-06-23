import os
import time

from datetime import datetime

class Output():
    def __init__(self) -> None:
        self.startTime = time.time()

    def printHeader(self):
        print("################################################################################")
        print("")
        print("dtgn (datagen) by 5f0")
        print("Creates folder structures and puts data in it")
        print("")
        print("Current working directory: " + os.getcwd())
        print("")
        print("Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("################################################################################")
        print("")

    def printFolderFileInfo(self, args, rootPath):
        print("Mode: " + args.mode)
        print("Create folder structure under " + rootPath)
        print("Create folder depth of " + str(args.depth))
        print("Create " + str(args.fileCount) + " files per folder")
        if(args.mode == "fixed"):
            print("Size per file: " + str(args.fileMinSize) + " Bytes")
        elif(args.mode == "random"):
            print("Size per file: between " + str(args.fileMinSize) + " and " + str(args.fileMaxSize) + " Bytes")
        print("")
        print("################################################################################")
        print("")

    def printSizeInfo(self, totalSize):
        print("Total File Size created: " + str(totalSize) + " Bytes")
        kb = totalSize/1000
        print("                         " + str(kb) + " KB")
        mb = kb/1000
        print("                         " + str(mb) + " MB")
        gb = mb/1000
        print("                         " + str(gb) + " GB")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("################################################################################")
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")