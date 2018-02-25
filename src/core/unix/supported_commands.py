from directory_service import UNIX_SCRIPTS_DIR, WIN_SCRIPTS_DIR

AVAILABLE_COMMANDS = {
"open" : UNIX_SCRIPTS_DIR + "open.sh",
"find" : UNIX_SCRIPTS_DIR + "find.sh",
"copy" : UNIX_SCRIPTS_DIR + "copy.sh",
"move" : UNIX_SCRIPTS_DIR + "move.sh",
"rename" : UNIX_SCRIPTS_DIR + "move.sh",
"organize": UNIX_SCRIPTS_DIR + "organize.sh"
}

EXPECTED_ARGS = {
"open": 1,
"find": 1,
"copy": 2,
"move": 2,
"rename": 2,
"organize": 2
}
