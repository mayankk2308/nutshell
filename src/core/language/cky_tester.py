import CkyParser as OOP

# Testing
ckyObj = OOP.CkyParser('command_grammar.txt', 'command_lexicon.txt')

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


# Not working and shouldn't be working
print(ckyObj.cky_parse("boot mydog.txt"))
print(ckyObj.cky_parse("organize Downloads"))
print(ckyObj.cky_parse("organize everything to Downloads"))
print(ckyObj.cky_parse("organize everything from Downloads"))
