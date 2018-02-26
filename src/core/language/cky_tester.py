from language import nlp_playground as nlp

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
