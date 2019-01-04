from setuptools import setup

APP = ["CkyParser.py"]
DATA_FILES = ['parsing_assets/command_grammar.txt', 'parsing_assets/command_lexicon.txt']
OPTIONS = {
"includes": ["OutputCodes.py"]
}

setup(
plugin=APP,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
install_requires=['pyobjc'],
data_files=DATA_FILES
)
