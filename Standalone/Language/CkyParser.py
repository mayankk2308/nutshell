import pprint
import constants
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
            if line and line[0] != constants.COMMENT_SYMBOL:
                if not line.strip():
                    continue
                left, right = line.split(constants.LEXICON_SPLIT)
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
            if line and line[0] != constants.COMMENT_SYMBOL:
                if not line.strip():
                    continue
                left, right = line.split(constants.GRAMMAR_SPLIT)
                left = left.strip()
                children = right.split()
                rule = (left, tuple(children))
                self.command_rules.append(rule)

    def expand_lexicon(self, key, value):
        self.command_lexicon[key].append(value)


    @staticmethod
    def pre_process(command):
        quotes = 0
        command += " "
        current_arg = ""
        tokens = []
        for character in command:
            if character is " " and quotes % 2 is 0:
                tokens.append(current_arg)
                current_arg = ""
            elif character is "'":
                quotes += 1
            else:
                current_arg += character
        return tokens

    def cky_parse(self, original_command):
        command = self.pre_process(original_command)
        N = len(command)
        cells = {}
        for i in range(N):
            for j in range(i + 1, N + 1):
                cells[(i, j)] = []

        # Fill in the bottom most row of the table
        command_included = False
        for i in range(N):
            entry = []
            for key in self.command_lexicon:
                if command[i] in self.command_lexicon[key]:
                    if "command" in key:
                        if not command_included:
                            entry.append((key, 0, command[i], constants.TERMINAL))
                            command_included = True
                        else:
                            entry.append(('file_folder_lex', 0, command[i], constants.TERMINAL))
                    else:
                        entry.append((key, 0, command[i], constants.TERMINAL))
            if not entry:
                entry.extend([('misc', 0, command[i], constants.TERMINAL), ('file_folder_lex', 0, command[i], constants.TERMINAL), ('application', 0, command[i], constants.TERMINAL)])
            cells[(i, i + 1)] += entry

        for diff in range(constants.LEFT_BP, N + 1):
            for i in range(N - diff + 1):
                for k in range(i + 1, i + diff):
                    for A in cells[(i, k)]:
                        for B in cells[(k, i + diff)]:
                            for rule in self.command_rules:
                                if rule[1] == (A[constants.RULE_PARENT], B[constants.RULE_PARENT]):
                                    cells[(i, i + diff)] += [(rule[0], k, A[constants.RULE_PARENT], B[constants.RULE_PARENT])]

        # pprint.pprint(cells)
        for tups in cells[(0, N)]:
            if tups[constants.RULE_PARENT] == constants.COMMAND_SYMBOL:
                return self.resolve_args(tups, cells, N)
        return 255, original_command

    def extract_args(self, current_cell, cells, i, j):
        if current_cell[constants.RIGHT_BP] == constants.TERMINAL and current_cell[0] in constants.ARG_TYPE:
            return [current_cell[constants.LEFT_BP]]
        if current_cell[constants.RIGHT_BP] == constants.TERMINAL and current_cell[0] in constants.NL_REDUNDANCIES:
            return []
        splitpoint = current_cell[constants.SPLIT_INDEX]
        leftchild = cells[(i, splitpoint)]
        rightchild = cells[(splitpoint, j)]
        for tups in leftchild:
            if tups[constants.RULE_PARENT] == current_cell[constants.LEFT_BP]:
                left_tup = tups
        for tups in rightchild:
            if tups[constants.RULE_PARENT] == current_cell[constants.RIGHT_BP]:
                right_tup = tups
        return self.extract_args(left_tup, cells, i, splitpoint) + self.extract_args(right_tup, cells, splitpoint, j)

    def resolve_args(self, cell, cells, N):
        first_split = cell[constants.SPLIT_INDEX]
        command_type = cell[constants.LEFT_BP]
        right_subtree = cells[(first_split, N)]
        for tups in right_subtree:
            if tups[constants.RULE_PARENT] == cell[constants.RIGHT_BP]:
                right = tups
        arg_array = []
        arg_array += [command_type]
        arguments = self.extract_args(right, cells, first_split, N)
        arg_array = arg_array + arguments
        return arg_array


# Testing

# ckyObj = CkyParser("command_grammar.txt", "command_lexicon.txt")
#
# print(ckyObj.cky_parse("open 'mydog.txt'"))
# print(ckyObj.cky_parse("launch mydog.txt"))
# print(ckyObj.cky_parse("locate mydog.txt"))
# print(ckyObj.cky_parse("find mydog.txt"))
# print(ckyObj.cky_parse("move mydog.txt to Trash"))
# print(ckyObj.cky_parse("move mydog.txt from Downloads to Trash"))
# print(ckyObj.cky_parse("organize everything in Downloads"))
# print(ckyObj.cky_parse("copy mydog.txt to Trash"))
# print(ckyObj.cky_parse("copy mydog.txt from Downloads to Trash"))
# print(ckyObj.cky_parse("copy mydog.txt to 'my cat'"))
# print(ckyObj.cky_parse("copy mydog.txt in Downloads to cat.txt"))
# print(ckyObj.cky_parse("find my.dog from 'my computer'"))
#
# print(ckyObj.cky_parse("move 'Open Source Projects' to 'Hello World'"))
