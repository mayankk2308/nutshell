#
#       CKY parsing method
#


# The rules defining the break down of a command and all of its constituents
command_rules = """
C -> Find_lex file_folder_lex
C -> Move_lex file_folder_lex?to?file_folder_lex
C -> Rename file_folder_lex?to?file_folder_lex
C -> Copy_lex file_folder_lex?to?file_folder_lex
C -> Copy_lex from?file_folder_lex?to?file_folder_lex
C -> Open_lex file_folder_lex
C -> Organize_lex type?in?file_folder_lex
type?in?file_folder_lex -> everything in?file_folder_lex
type?in?file_folder_lex -> extension_lex in?file_folder_lex
in?file_folder_lex -> in file_folder_lex
from?file_folder_lex?to?file_folder_lex -> from file_folder_lex?to?file_folder_lex 
file_folder_lex?to?file_folder_lex -> file_folder_lex to?file_folder_lex
to?file_folder_lex -> to file_folder_lex

"""


# Lexicon containing synonyms of command constituents
command_lexicon = {
    'Find_lex': set(),           # synonyms of find
    'Move_lex': set(),           # synonyms of move
    'Rename_lex': set(),         # synonyms of rename
    'Copy_lex': set(),           # synonyms of copy
    'Open_lex': set(),           # synonyms of open
    'Organize_lex': set(),       # synonyms of organize
    'file_folder_lex': set(),    # regex to match a string(file or folder name)
    'extension_lex': set(),      # set of extensions supported in organize
}



