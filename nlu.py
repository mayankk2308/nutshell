import sys
import subprocess
import shlex
import os
from os.path import splitext, isfile, join

script_exec = {}
script_exec["find"] = "scripts/find.sh"
script_exec["copy"] = "scripts/copy.sh"
script_exec["move"] = "scripts/move.sh"
script_exec["open"] = "scripts/open.sh"
script_exec["organize"] = "scripts/organize.sh"


def find(request):
    response = subprocess.Popen([script_exec[request[0]], request[1]], stdout=subprocess.PIPE)
    options = []
    while True:
        line = response.stdout.readline()
        if line != b'':
            options.append(line.rstrip().decode("utf-8"))
        else:
            break
    return 0 if len(options) == 0 else options


def copy_or_move(request):
    process_response = subprocess.Popen([script_exec[request[0]], request[1], request[3]], stdout=subprocess.PIPE)


def prefetch_file(request):
    request[0] = "find"
    std_out = find(request)
    if len(std_out) == 0:
        print("File or folder not found.")
        return None
    return std_out


def opencmd(request):
    if prefetch_file(request) is not None:
        request[0] = "open"
        subprocess.Popen([script_exec[request[0]], request[1]], stdout=subprocess.PIPE)


def rename(request):
    std_out = prefetch_file(request)
    if std_out is not None:
        request[0] = "move"
        source = std_out
        std_out = std_out[0:std_out.rfind("/") + 1]
        request[1] = source[source.rfind("/") + 1:]
        request[3] = std_out + request[3]
        copy_or_move(request)
        return "Rename Successful"
    else:
        return "File/Folder not found"


def findAllExtensions(filePath):
    extensions = set()
    for f in os.listdir(filePath):
        print(f)
        if "." in f and isfile(join(filePath, f)):
            file_name, extension = splitext(f)
            # extensions.add(f.split(".")[-1])
            if len(extension) > 0:
                extensions.add(extension[1:])
    return extensions
    # print(extensions)

def organize(request):
    folder = request[3]
    new_request = ["find", folder]
    location = find(new_request)
    if request[1] == "everything":
        extensions = findAllExtensions(location)
        for ext in extensions:
            ext_request = ["organize", ext, "in", request[3]]
            subprocess.Popen([script_exec[ext_request[0]], ext_request[3], ext_request[1]], stdout=subprocess.PIPE)
    else:
        subprocess.Popen([script_exec[request[0]], request[3], request[1]], stdout=subprocess.PIPE)
    pass


def main(request):
    request = request.split(" ")

    if request[0] == "find":
        return "find",find(request)

    if request[0] == "copy" or request[0] == "move":
        return copy_or_move(request)

    if request[0] == "open":
        return opencmd(request)

    if request[0] == "rename":
        return rename(request)

    if request[0] == "organize":
        return organize(request)
