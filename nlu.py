import sys
import subprocess
import shlex

script_exec = {}
script_exec["find"] = "scripts/find.sh"
script_exec["copy"] = "scripts/copy.sh"
script_exec["move"] = "scripts/move.sh"
script_exec["open"] = "scripts/open.sh"

def find(request):
    proc = subprocess.Popen([script_exec[request[0]], request[1]], stdout=subprocess.PIPE)
    std_out = proc.stdout.readline().rstrip().decode("utf-8")
    print(std_out)
    return std_out

def copy(request):
    process_response = subprocess.Popen([script_exec[request[0]], request[1], request[3]], stdout=subprocess.PIPE)

def move(request):
    process_response = subprocess.Popen([script_exec[request[0]], request[1], request[3]], stdout=subprocess.PIPE)

def opencmd(request):
    request[0] = "find"
    std_out = find(request)
    if len(std_out) == 0:
        print("File or folder not found")
        return
    else:
        request[0] = "open"
        subprocess.Popen([script_exec[request[0]], request[1]], stdout=subprocess.PIPE)

def rename(request):
    request[0] = "find"
    line = find(request)
    if len(line) == 0:
        print("File or folder not found")
        return
    else:
        request[0] = "move"
        initial = line
        line = line[0:line.rfind("/") + 1]
        request[1] = initial[initial.rfind("/") + 1:]
        request[3] = line + request[3]
        move(request)

request = input()
request = request.split(" ")

if request[0] == "find":
    find(request)

if request[0] == "copy":
    copy(request)

if request[0] == "move":
    move(request)

if request[0] == "open":
    opencmd(request)

if request[0] == "rename":
    rename(request)
