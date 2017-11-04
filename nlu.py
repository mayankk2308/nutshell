import sys
import subprocess
import shlex

script_exec = {}
script_exec["find"] = "scripts/find.sh"
script_exec["copy"] = "scripts/copy.sh"
script_exec["move"] = "scripts/move.sh"
script_exec["open"] = "scripts/open.sh"

def find(request):
    response = subprocess.Popen([script_exec[request[0]], request[1]], stdout=subprocess.PIPE)
    std_out = response.stdout.readline().rstrip().decode("utf-8")
    print(std_out)
    return std_out

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

request = input()
request = request.split(" ")

if request[0] == "find":
    find(request)

if request[0] == "copy" or request[0] == "move":
    copy_or_move(request)

if request[0] == "open":
    opencmd(request)

if request[0] == "rename":
    rename(request)
