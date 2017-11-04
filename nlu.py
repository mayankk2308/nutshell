import sys
import subprocess
import shlex

mapping = {}
mapping["find"] = "scripts/find.sh"
mapping["copy"] = "scripts/copy.sh"
mapping["move"] = "scripts/move.sh"
mapping["open"] = "scripts/open.sh"



def find(x):
    proc = subprocess.Popen([mapping[x[0]], x[1]], stdout=subprocess.PIPE)
    line = proc.stdout.readline().rstrip().decode("utf-8")
    print(line)
    return line

def copy(x):
    proc = subprocess.Popen([mapping[x[0]], x[1], x[3]], stdout=subprocess.PIPE)

def move(x):
    proc = subprocess.Popen([mapping[x[0]], x[1], x[3]], stdout=subprocess.PIPE)

def opencmd(x):
    x[0] = "find"
    line = find(x)
    if len(line) == 0:
        print("File or folder not found")
        return
    else:
        x[0] = "open"
        subprocess.Popen([mapping[x[0]], x[1]], stdout=subprocess.PIPE)

def rename(x):
    x[0] = "find"
    line = find(x)
    if len(line) == 0:
        print("File or folder not found")
        return
    else:
        x[0] = "move"
        initial = line
        line = line[0:line.rfind("/") + 1]
        x[1] = initial[initial.rfind("/") + 1:]
        x[3] = line + x[3]
        move(x)



x = input()
x = x.split(" ")
# print(x)
if x[0] == "find":
    find(x)

if x[0] == "copy":
    copy(x)

if x[0] == "move":
    move(x)

if x[0] == "open":
    opencmd(x)

if x[0] == "rename":
    rename(x)





