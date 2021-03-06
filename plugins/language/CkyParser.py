import objc
from Foundation import NSObject
from OutputCodes import OCODE
import os

LanguageInterface = objc.protocolNamed("Nutshell.LanguageInterface")

class CkyParser(NSObject, protocols=[LanguageInterface]):
    """
    A natural-language parser to check command validity and extract args

    Attributes:
        command_lexicon:     Dictionary of all commands
        command_rules:       Synctactic rules governing the commands
        rule_file:           Text file from which rules are read in
        lexicon_file:        Text file from which lexicon is read in
    """
    command_lexicon = {}
    command_rules = list()
    rule_file = os.environ['RESOURCEPATH'] + "/command_grammar.txt"
    lexicon_file = os.environ['RESOURCEPATH'] + "/command_lexicon.txt"

    @classmethod
    def instance(self):
        """
        Initializer function.

        Args:
            None

        Returns:
            pClass: CkyParser object.
        """
        pClass = CkyParser.alloc().init()
        pClass.populateRules()
        pClass.populateLexicon()
        return pClass

    @objc.python_method
    def populateLexicon(self):
        """
        Read in lexicon file and populate lexicon.

        Args:
            None

        Returns:
            None
        """
        with open(CkyParser.lexicon_file) as f:
            content = f.readlines()
        lexicon_text = [x.strip() for x in content]
        for line in lexicon_text:
            if line and line[0] != '#':
                if not line.strip():
                    continue
                left, right = line.split(":")
                left = left.strip()
                children = right.split(",")
                CkyParser.command_lexicon[left] = []
                for child in children:
                    if len(child) > 0:
                        CkyParser.command_lexicon[left].append(child.strip());

    @objc.python_method
    def populateRules(self):
        """
        Read in lexicon file and populate lexicon.

        Args:
            None

        Returns:
            None
        """
        with open(CkyParser.rule_file) as f:
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
                CkyParser.command_rules.append(rule)

    # Callback function after did-you-mean to resolve ambiguity for later
    # def expandLexicon(self, key, value):
    #     CkyParser.command_lexicon[key].append(value)
        # Append to lexicon file to save it persistently


    @staticmethod
    @objc.python_method
    def preProcess(command):
        """
        Processes raw input string.

        Args:
            command: The raw input command.

        Returns:
            tokens:  An array of words with proper formatting
        """
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

    def parseWithCommand_completionHandler_(self, original_command, completionHandler):
        """
        Primary parsing function.

        Args:
            original_command:   Raw command input from the user.
            completionHandler:  A function that handles the completion of this parsing fn.

        Returns:
            completionHandler:  Completion handler with success code. 0, arguments for success, 255 otherwise.
        """
        command = self.preProcess(original_command)
        N = len(command)
        cells = {}
        for i in range(N):
            for j in range(i + 1, N + 1):
                cells[(i, j)] = []

        # Fill in the bottom most row of the table
        command_included = False
        for i in range(N):
            entry = []
            if '.' in command[i]:
                entry.append(('file_folder_lex', 0, command[i], -1))
            for key in CkyParser.command_lexicon:
                if command[i] in CkyParser.command_lexicon[key]:
                    if "command" in key:
                        if not command_included:
                            entry.append((key, 0, command[i], -1))
                            command_included = True
                        else:
                            entry.append(('file_folder_lex', 0, command[i], -1))
                    else:
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
                            for rule in CkyParser.command_rules:
                                if rule[1] == (A[0], B[0]):
                                    cells[(i, i + diff)] += [(rule[0], k, A[0], B[0])]

        # pprint.pprint(cells)
        for tups in cells[(0, N)]:
            if tups[0] == "C":
                completionHandler(0, self.resolveArgs(tups, cells, N))
                return
        completionHandler(255, [OCODE[255]])

    @objc.python_method
    def extractArgs(self, current_cell, cells, i, j):
        """
        Backtracking function to get arguments.

        Args:
            current_cell: The cell at hand in recursion.
            cells:        The CKY Parse matrix.
            i:            Row index of the cell.
            j:            Column index of the cell.

        Returns:
            []:           An array of the command arguments.
        """
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
        return self.extractArgs(left_tup, cells, i, splitpoint) + self.extractArgs(right_tup, cells, splitpoint, j)

    @objc.python_method
    def resolveArgs(self, cell, cells, N):
        """
        Primary function to form the array to be passed to UNIX layer.
        Calls the recursive fn: extractArgs

        Args:
            cell:       The top-most cell of the CKY matrix.
            cells:      The CKY Parse matrix.
            N:          # of columns of CKY matrix.

        Returns:
            arg_array:  Command + arguments in a single array.
        """
        first_split = cell[1]
        command_type = cells[(0, first_split)][0][0]
        right_subtree = cells[(first_split, N)]
        for tups in right_subtree:
            if tups[0] == cell[3]:
                right = tups
        arg_array = list()
        arg_array.append(command_type)
        arguments = self.extractArgs(right, cells, first_split, N)
        arg_array = arg_array + arguments
        return arg_array


# Testing
#
# ckyObj = CkyParser()
#
# print(ckyObj.ckyParse("open mydog.txt"))
# print(ckyObj.ckyParse("launch mydog.txt"))
# print(ckyObj.ckyParse("locate mydog.txt"))
# print(ckyObj.ckyParse("find mydog.txt"))
# print(ckyObj.ckyParse("move mydog.txt to Trash"))
# def handler(error, msg):
#     print(error)
#     print(msg)

# ckyObj.parseWithCommand_completionHandler_("move mydog.txt from Downloads to Trash", handler)
# print(ckyObj.ckyParse("organize everything in Downloads"))
# print(ckyObj.ckyParse("copy mydog.txt to Trash"))
# print(ckyObj.ckyParse("copy mydog.txt from Downloads to Trash"))
# print(ckyObj.ckyParse("copy mydog.txt to my cat"))
# print(ckyObj.ckyParse("copy mydog.txt in Downloads to cat.txt"))
# print(ckyObj.ckyParse("find my.dog from my computer"))
#
# print(ckyObj.ckyParse("open Open Source Projects"))
# print(ckyObj.ckyParse("open Find Source Projects"))
# print(ckyObj.ckyParse("open Copy Source Projects"))
# print(ckyObj.ckyParse("open organize Source Projects"))
# print(ckyObj.ckyParse("open move Source Projects"))
# print(ckyObj.ckyParse("open rename Source Projects"))
