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

command_lexicon = {}


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
            return resolve_args(tups, cells, N)
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


def populate_lexicon(lexicon_file):
    global command_lexicon
    with open(lexicon_file) as f:
        content = f.readlines()
    lexicon_text = [x.strip() for x in content]
    for line in lexicon_text:
        if line and line[0] != '#':
            if not line.strip():
                continue
            left, right = line.split(":")
            left = left.strip()
            children = right.split(",")
            command_lexicon[left] = []
            for child in children:
                if len(child) > 0:
                    command_lexicon[left].append(child.strip());



populate_rules('command_grammar.txt')
populate_lexicon('command_lexicon.txt')



#
# Return args playground
#
def extract_args(current_cell, cells, i, j):
    if current_cell[0] == "file_folder_lex" and current_cell[3] == -1:
        return [current_cell[2]]
    if current_cell[0] == "extension_lex" and current_cell[3] == -1:
        return [current_cell[2]]
    if current_cell[0] == "to" or current_cell[0] == "from" or current_cell[0] == "with" or current_cell[0] == "in" and current_cell[3] == -1:
        return []
    splitpoint = current_cell[1]
    leftchild = cells[(i, splitpoint)]
    rightchild = cells[(splitpoint, j)]
    for tups in leftchild:
        if tups[0] == current_cell[2]:
            left_tup = tups
    for tups in rightchild:
        if tups[0] == current_cell[3]:
            right_tup = tups
    return extract_args(left_tup, cells, i, splitpoint) + extract_args(right_tup, cells, splitpoint, j)



def resolve_args(cell, cells, N):
    first_split = cell[1]
    command_type = cells[(0, first_split)][0][0]
    right_subtree = cells[(first_split, N)]
    for tups in right_subtree:
        if tups[0] == cell[3]:
            right = tups
    arg_array = list()
    arg_array.append(command_type)
    arguments = extract_args(right, cells, first_split, N)
    arg_array = arg_array + arguments
    return arg_array





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




#
#   Did you mean & Spell check playground
#
#
# expectation mapping could be used as well and then use it along with edit distance
#
# pseudo code
#
# spell_check(word)
#
# did you mean()
# for words in input command:
#     new_command = ""
#     if spell_check(word) != word:
#         if spell_check(word) belongs to our lexicon:
#             boolean dym = true
#             accumulate new_command

# import re
# from collections import Counter
#
#
# def words(text): return re.findall(r'\w+', text.lower())
#
# WORDS = Counter(words(open('big.txt').read()))
#
#
# def P(word, N=sum(WORDS.values())):
#     """"Probability of `word`."""
#     return WORDS[word] / N
#
#
# def correction(word):
#     """"Most probable spelling correction for word."""
#     return max(candidates(word), key=P)
#
#
# def candidates(word):
#     "Generate possible spelling corrections for word."
#     return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]
#
#
# def known(words):
#     """"The subset of `words` that appear in the dictionary of WORDS."""
#     return set(w for w in words if w in WORDS)
#
#
# def edits1(word):
#     """"All edits that are one edit away from `word`."""
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
#     deletes = [L + R[1:] for L, R in splits if R]
#     transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
#     replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
#     inserts = [L + c + R for L, R in splits for c in letters]
#     return set(deletes + transposes + replaces + inserts)
#
#
# def edits2(word):
#     """"All edits that are two edits away from `word`."""
#     return (e2 for e1 in edits1(word) for e2 in edits1(e1))