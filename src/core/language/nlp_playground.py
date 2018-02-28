#
#       CKY parsing method
#

from pprint import pprint

# The rules defining the break down of a command and all of its constituents
command_rules = list()


def populate_rules(grammar_file):
    global command_rules
    with open(grammar_file) as f:
        content = f.readlines()
    command_text = [x.strip() for x in content]
    command_rules = []
    for line in command_text:
        if line and line[0] != '#':
            if not line.strip():
                continue
            left, right = line.split("->")
            left = left.strip()
            children = right.split()
            rule = (left, tuple(children))
            command_rules.append(rule)


def pre_process(command):
    command = command.lower()
    tokens = command.split()
    return tokens

# Lexicon containing synonyms of command constituents
command_lexicon = {
    'Find_lex': {'find', 'locate'},          # synonyms of find
    'Move_lex': {'move', 'shift'},           # synonyms of move
    'Rename_lex': {'rename'},                # synonyms of rename
    'Copy_lex': {'copy'},                    # synonyms of copy
    'Open_lex': {'open', 'launch'},          # synonyms of open
    'Organize_lex': {'organize'},            # synonyms of organize
    'file_folder_lex': {},                   # regex to match a string(file or folder name)
    'extension_lex': {'everything'},         # set of extensions supported in organize
    'from': {'from'},
    'to': {'to'},
    'in': {'in'},
    'with': {'with'},
}


# return True or False depending whether the command is parseable by the grammar.
def cky_acceptance(command):

    global command_rules, command_lexicon
    command = pre_process(command)
    N = len(command)
    cells = {}
    for i in range(N):
        for j in range(i + 1, N + 1):
            cells[(i, j)] = []

    # Fill in the bottom most row of the table
    for i in range(N):
        entry = []
        if '.' in command[i]:
            entry.append('file_folder_lex')
        for key in command_lexicon:
            if command[i] in command_lexicon[key]:
                entry.append(key)
        if not entry:
            entry.append('misc')
            entry.append('file_folder_lex')
            entry.append('application')
        cells[(i, i + 1)] += entry

    for diff in range(2, N + 1):
        for i in range(N - diff + 1):
            for k in range(i + 1, i + diff):
                for A in cells[(i, k)]:
                    for B in cells[(k, i + diff)]:
                        for rule in command_rules:
                            if rule[1] == (A, B):
                                cells[(i, i + diff)] += [rule[0]]

    # pprint(cells)
    if "C" in cells[(0, N)]:
        return True
    return False


# return parse tree for parseable command
def cky_parse(command):

    global command_rules, command_lexicon
    command = pre_process(command)
    N = len(command)
    cells = {}
    for i in range(N):
        for j in range(i + 1, N + 1):
            cells[(i, j)] = []

    # Fill in the bottom most row of the table
    for i in range(N):
        entry = []
        if '.' in command[i]:
            entry.append(('file_folder_lex', 0, command[i], -1))
        for key in command_lexicon:
            if command[i] in command_lexicon[key]:
                entry.append((key, 0, command[i], -1))
        if not entry:
            entry.append(('misc', 0, command[i], -1))
            entry.append(('file_folder_lex', 0, command[i], -1))
            entry.append(('application', 0, command[i], -1))
        cells[(i, i + 1)] += entry

    for diff in range(2, N + 1):
        for i in range(N - diff + 1):
            for k in range(i + 1, i + diff):
                for A in cells[(i, k)]:
                    for B in cells[(k, i + diff)]:
                        for rule in command_rules:
                            if rule[1] == (A[0], B[0]):
                                cells[(i, i + diff)] += [(rule[0], k, A[0], B[0])]

    # pprint(cells)
    for tups in cells[(0, N)]:
        if tups[0] == "C":
            return rec_backtrack(tups, cells, 0, N)
    return None


def rec_backtrack(curr_tuple, cells, i, j):
    if curr_tuple[3] == -1:
        return [curr_tuple[0]] + [curr_tuple[2]]
    splitpoint = curr_tuple[1]
    leftchild = cells[(i, splitpoint)]
    rightchild = cells[(splitpoint, j)]
    for tups in leftchild:
        if tups[0] == curr_tuple[2]:
            left_tup = tups
    for tups in rightchild:
        if tups[0] == curr_tuple[3]:
            right_tup = tups
    return [curr_tuple[0]] + [[rec_backtrack(left_tup, cells, i, splitpoint)] + [rec_backtrack(right_tup, cells, splitpoint, j)]]

populate_rules('command_grammar.txt')


print(cky_parse("open mydog.txt"))
print(cky_parse("launch mydog.txt"))
print(cky_parse("locate mydog.txt"))
print(cky_parse("find mydog.txt"))
print(cky_parse("move mydog.txt to Trash"))
print(cky_parse("move mydog.txt from Downloads to Trash"))
print(cky_parse("organize everything in Downloads"))
print(cky_parse("copy mydog.txt to Trash"))
print(cky_parse("copy mydog.txt from Downloads to Trash"))
print(cky_parse("copy mydog.txt to my cat"))
print(cky_parse("copy mydog.txt in Downloads to cat.txt"))
print(cky_parse("find my.dog from my computer"))

# Not working and shouldn't be working
print(cky_parse("boot mydog.txt"))
print(cky_parse("organize Downloads"))
print(cky_parse("organize everything to Downloads"))
print(cky_parse("organize everything from Downloads"))

