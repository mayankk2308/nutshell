class CkyParser:
    def __init__(self, grammar_rules_file, lexicon_file):
        self.rule_file = grammar_rules_file
        self.lexicon_file = lexicon_file
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
                return self.rec_backtrack(tups, cells, 0, N)
        return 255, original_command

    def rec_backtrack(self, curr_tuple, cells, i, j):
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
        return [curr_tuple[0]] + [
            [self.rec_backtrack(left_tup, cells, i, splitpoint)] + [self.rec_backtrack(right_tup, cells, splitpoint, j)]]

