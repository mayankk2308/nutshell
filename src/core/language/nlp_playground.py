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

populate_rules('command_grammar.txt')