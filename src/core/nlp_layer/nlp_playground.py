#
#       CKY parsing method
#


# The rules defining the break down of a command and all of its constituents
command_rules = """
C -> Find_lex file_folder_lex
C -> Move_lex file_folder_lex?preposition?file_folder_lex
C -> Move_lex preposition?file_folder_lex?preposition?file_folder_lex
C -> Rename file_folder_lex?preposition?file_folder_lex
C -> Copy_lex file_folder_lex?preposition?file_folder_lex
C -> Copy_lex preposition?file_folder_lex?preposition?file_folder_lex
C -> Open_lex file_folder_lex
C -> Open_lex file_folder_lex?preposition?file_folder_lex
C -> Organize_lex type?preposition?file_folder_lex
type?preposition?file_folder_lex -> extension_lex preposition?file_folder_lex
preposition?file_folder_lex?preposition?file_folder_lex -> preposition file_folder_lex?preposition?file_folder_lex 
file_folder_lex?preposition?file_folder_lex -> file_folder_lex preposition?file_folder_lex
preposition?file_folder_lex -> preposition file_folder_lex
"""


# Lexicon containing synonyms of command constituents
command_lexicon = {
    'Find_lex': {},                          # synonyms of find
    'Move_lex': {},                          # synonyms of move
    'Rename_lex': {},                        # synonyms of rename
    'Copy_lex': {},                          # synonyms of copy
    'Open_lex': {},                          # synonyms of open
    'Organize_lex': {},                      # synonyms of organize
    'file_folder_lex': {},                   # regex to match a string(file or folder name)
    'extension_lex': {'everything'},         # set of extensions supported in organize
    'preposition': {'from', 'to', 'in'}
}



