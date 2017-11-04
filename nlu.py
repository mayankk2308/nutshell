import sys
import subprocess
import shlex

mapping = {}
mapping["find"] = "scripts/find.sh"
mapping["copy"] = "scripts/copy.sh"
mapping["move"] = "scripts/move.sh"


def find(x):
    proc = subprocess.Popen([mapping[x[0]], x[1]], stdout=subprocess.PIPE)
    line = proc.stdout.readline().rstrip().decode("utf-8")
    print(line)

def copy(x):
    proc = subprocess.Popen([mapping[x[0]], x[1], x[3]], stdout=subprocess.PIPE)

def move(x):
    proc = subprocess.Popen([mapping[x[0]], x[1], x[3]], stdout=subprocess.PIPE)



x = input()
x = x.split(" ")
# print(x)
if x[0] == "find":
    find(x)

if x[0] == "copy":
    copy(x)

if x[0] == "move":
    move(x)





