import argparse

class Args():
    # parser: argparse instance
    def addArguments(parser):
        parser.add_argument("--mode", "-m", choices=["fixed","random"], default="fixed", help="Data Creation Mode: fixed: all files will be created the same size. Size is taken fom fileMinSize argument. random: the files created will have a random size between fileMinSize and fileMaxSize argument.")
        parser.add_argument("--path", "-p", type=str, required=True, help="Path under which the folder structure shall be located")
        parser.add_argument("--rootName", "-r", type=str, default="data_creator", help="The name of the root folder created")
        parser.add_argument("--depth", "-d", type=int, default=1, help="The depth of the folder structure")
        parser.add_argument("--fileCount", "-f", type=int, default=1, help="Nr. of files per folder depth")
        parser.add_argument("--fileMinSize", "-g", type=int, default=2000, help="The minium file size in bytes")
        parser.add_argument("--fileMaxSize", "-i", type=int, default=2000, help="The maximum file size in bytes")
        parser.add_argument("--purge", "-u", action=argparse.BooleanOptionalAction, help="If true, all files in path+rootName will be deleted. No folder structure is created. Use it carefully.")