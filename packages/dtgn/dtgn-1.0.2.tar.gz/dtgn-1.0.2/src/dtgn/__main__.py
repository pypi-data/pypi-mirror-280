import os
import sys
import random
import shutil
import argparse

from pathlib import Path

from dtgn.args.Args import Args
from dtgn.output.Output import Output

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    Args.addArguments(parser)
    args = parser.parse_args()

    # Creates Output instance for printing header and footer of console output
    out = Output()
    out.printHeader()

    # Create root path
    rootPath = os.path.join(args.path, args.rootName)

    if(args.purge):
        shutil.rmtree(rootPath)
        print(rootPath + " purged!")
    else:
        # Print argument configuration
        out.printFolderFileInfo(args, rootPath)

        # Create root dir
        Path(rootPath).mkdir(parents=True, exist_ok=True)

        # Create the folders through the given depth
        totalSize = 0
        for i in range(1,args.depth+1):
            folderName = "folder" + str(i)
            f = os.path.join(rootPath, folderName)
            Path(f).mkdir(parents=True, exist_ok=True)
            # Create files
            for i in range(1, args.fileCount+1):
                filePath = os.path.join(f, folderName + "-" + str(i) + ".bin")
                with open(filePath, 'wb') as file:
                    size = 0
                    if(args.mode == "fixed"):
                        size = args.fileMinSize
                        file.write(bytearray(os.urandom(size)))
                    elif(args.mode == "random"):
                        size = random.randint(args.fileMinSize, args.fileMaxSize)
                        file.write(bytearray(os.urandom(size)))
                    totalSize = totalSize + size
        
            rootPath = f
        out.printSizeInfo(totalSize)

    out.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())
