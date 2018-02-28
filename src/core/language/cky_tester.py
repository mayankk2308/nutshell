from language import nlp_playground as nlp
from language import CkyParser as OOP

# # Working and should be working
assert nlp.cky_acceptance("open mydog.txt")
assert nlp.cky_acceptance("launch mydog.txt")
assert nlp.cky_acceptance("locate mydog.txt")
assert nlp.cky_acceptance("find mydog.txt")
assert nlp.cky_acceptance("move mydog.txt to Trash")
assert nlp.cky_acceptance("move mydog.txt from Downloads to Trash")
assert nlp.cky_acceptance("organize everything in Downloads")
assert nlp.cky_acceptance("copy mydog.txt to Trash")
assert nlp.cky_acceptance("copy mydog.txt from Downloads to Trash")
assert nlp.cky_acceptance("copy mydog.txt to my cat")
assert nlp.cky_acceptance("copy mydog.txt in Downloads to cat.txt")
assert nlp.cky_acceptance("find my.dog from my computer")

# Not working and shouldn't be working
assert not nlp.cky_acceptance("boot mydog.txt")
assert not nlp.cky_acceptance("organize Downloads")
assert not nlp.cky_acceptance("organize everything to Downloads")
assert not nlp.cky_acceptance("organize everything from Downloads")





# Testing


ckyObj = OOP.CkyParser('command_grammar.txt')


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
