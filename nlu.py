
import subprocess
import os
from os.path import splitext, isfile, join

# global parameters
script_exec = {}
script_exec["find"] = "scripts/find.sh"
script_exec["copy"] = "scripts/copy.sh"
script_exec["move"] = "scripts/move.sh"
script_exec["open"] = "scripts/open.sh"
script_exec["organize"] = "scripts/organize.sh"
script_exec["find_slow"] = "scripts/find_slow.sh"

# parse standard output
def parse_std_out(response):
    full_std_out = []
    while True:
        line = response.stdout.readline()
        if line == b'':
            break;
        full_std_out.append(line.rstrip().decode("utf-8"))
    return full_std_out

# find absolute path of possible file_name matches
def find_slow(file_name):
    response = subprocess.Popen([script_exec["find_slow"], file_name], stdout=subprocess.PIPE)
    std_out = parse_std_out(response)
    return None if not std_out else std_out

def find(file_name):
    response = subprocess.Popen([script_exec["find"], file_name], stdout=subprocess.PIPE)
    std_out = parse_std_out(response)
    return None if not std_out else std_out

# copy or move source file to given destination
def copy_or_move(cmd, source, destination):
    response = subprocess.Popen([script_exec[cmd], source, destination], stdout=subprocess.PIPE)
    std_out = parse_std_out(response)
    return cmd + " from " + source + " to " + destination + " successful" if not std_out else std_out

# open file or directory at unique_filepath
def opencmd(unique_filepath):
    response = subprocess.Popen([script_exec["open"], unique_filepath], stdout=subprocess.PIPE)
    std_out = parse_std_out(response)
    return "opened " + unique_filepath + " successfully" if not std_out else std_out

# rename source_name file with source_new_name
def rename(source_name, source_new_name):
    directory = source_name[0 : source_name.rfind("/") + 1]
    source_new_name = directory + source_new_name
    return copy_or_move("move", source_name, source_new_name)

# find all extensions in given directory
def findAllExtensions(file_path):
    extensions = set()
    for f in os.listdir(file_path):
        if "." in f and isfile(join(file_path, f)):
            file_name, extension = splitext(f)
            if len(extension) > 0:
                extensions.add(extension[1:])
    return extensions

# organize given folder_name with doc_type
def organize(folder_name, doc_type):
    response = ""
    if doc_type == "everything":
        # for all types of documents
        extensions = findAllExtensions(folder_name)
        for ext in extensions:
            response = subprocess.Popen([script_exec["organize"], folder_name, ext], stdout=subprocess.PIPE)
            std_out = parse_std_out(response)
            if std_out:
                return std_out
    else:
        # for single doc_type
        response = subprocess.Popen([script_exec["organize"], folder_name, doc_type], stdout=subprocess.PIPE)
        std_out = parse_std_out(response)
        if std_out:
            return std_out
    return "organizing " + doc_type + " successful in " + folder_name


# handle a user request
def requestHandler(request):
    if request[0] == "find":
        return_code = find_slow(request[1])
        if return_code is None:
            return "Unable to find file/folder", None
        else:
            return "find", return_code

    elif request[0] == "copy" or request[0] == "move":
        source_check = find(request[1])
        dest_check = find(request[3])
        if source_check is None:
            return "Unable to find source file. Please input a valid source", None
        elif dest_check is None:
            return "Unable to find destination folder. Please input a valid destination", None
        return request[0], (source_check, dest_check)

    elif request[0] == "open":
        source_check = find(request[1])
        if source_check is None:
            return "Unable to locate the file/folder. Please input a valid file/folder name", None
        return "open", source_check

    elif request[0] == "rename":
        source_check = find(request[1])
        if source_check is None:
            return "Unable to locate the file/folder. Please input a valid file/folder name", None
        return "rename", (source_check, request[3])

    elif request[0] == "organize":
        source_check = find(request[3])
        if source_check is None:
            return "Unable to locate the file/folder. Please input a valid file/folder name", None
        return "organize", (source_check, request[1])

    else:
        return "Syntax currently not supported", None


# primary entry point
def main(request):
    request = request.split(" ")
    return requestHandler(request)
