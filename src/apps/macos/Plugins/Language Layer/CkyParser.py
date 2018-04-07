import objc
from Foundation import NSObject

class CkyParser:
    def __init__(self):
        self.rule_file = 'parsing_assets/command_grammar.txt'
        self.lexicon_file = 'parsing_assets/command_lexicon.txt'
        self.command_rules = list()
        self.command_lexicon = {}
        self.populate_rules()
        self.populate_lexicon()

    def populate_lexicon(self):
        with open(self.lexicon_file) as f:
            content = f.readlines()
        lexicon_text = [x.strip() for x in content]
        for line in lexicon_text:
            if line and line[0] != '#':
                if not line.strip():
                    continue
                left, right = line.split(":")
                left = left.strip()
                children = right.split(",")
                self.command_lexicon[left] = []
                for child in children:
                    if len(child) > 0:
                        self.command_lexicon[left].append(child.strip());

    def populate_rules(self):
        with open(self.rule_file) as f:
            content = f.readlines()
        command_text = [x.strip() for x in content]
        for line in command_text:
            if line and line[0] != '#':
                if not line.strip():
                    continue
                left, right = line.split("->")
                left = left.strip()
                children = right.split()
                rule = (left, tuple(children))
                self.command_rules.append(rule)

    # Callback function after did-you-mean to resolve ambiguity for later
    def expand_lexicon(self, key, value):
        self.command_lexicon[key].append(value)


    @staticmethod
    def pre_process(command):
        command = command.lower()
        tokens = command.split()
        return tokens

    def cky_parse(self, original_command):
        command = self.pre_process(original_command)
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
            for key in self.command_lexicon:
                if command[i] in self.command_lexicon[key]:
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
                            for rule in self.command_rules:
                                if rule[1] == (A[0], B[0]):
                                    cells[(i, i + diff)] += [(rule[0], k, A[0], B[0])]

        # pprint(cells)
        for tups in cells[(0, N)]:
            if tups[0] == "C":
                return self.resolve_args(tups, cells, N)
        return 255, original_command


    def extract_args(self, current_cell, cells, i, j):
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
        return self.extract_args(left_tup, cells, i, splitpoint) + self.extract_args(right_tup, cells, splitpoint, j)


    def resolve_args(self, cell, cells, N):
        first_split = cell[1]
        command_type = cells[(0, first_split)][0][0]
        right_subtree = cells[(first_split, N)]
        for tups in right_subtree:
            if tups[0] == cell[3]:
                right = tups
        arg_array = list()
        arg_array.append(command_type)
        arguments = self.extract_args(right, cells, first_split, N)
        arg_array = arg_array + arguments
        return arg_array



# Testing

ckyObj = CkyParser()

print(ckyObj.cky_parse("open mydog.txt"))
print(ckyObj.cky_parse("launch mydog.txt"))
print(ckyObj.cky_parse("locate mydog.txt"))
print(ckyObj.cky_parse("find mydog.txt"))
print(ckyObj.cky_parse("move mydog.txt to Trash"))
print(ckyObj.cky_parse("move mydog.txt from Downloads to Trash"))
print(ckyObj.cky_parse("organize everything in Downloads"))
print(ckyObj.cky_parse("copy mydog.txt to Trash"))
print(ckyObj.cky_parse("copy mydog.txt from Downloads to Trash"))
print(ckyObj.cky_parse("copy mydog.txt to my cat"))
print(ckyObj.cky_parse("copy mydog.txt in Downloads to cat.txt"))
print(ckyObj.cky_parse("find my.dog from my computer"))
