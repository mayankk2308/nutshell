import os
from os import path

_abs_path = path.abspath(__file__)
_script_layer = _abs_path[: _abs_path.rfind("/")]
_core = _script_layer[: _script_layer.rfind("/")]
_src = _core[: _core.rfind("/")]
BASE_DIR = _src[: _src.rfind("/") + 1]
MANAGEMENT_DIR = _src + "/management"
UNIX_SCRIPTS_DIR = BASE_DIR + "scripts/unix_scripts/"
WIN_SCRIPTS_DIR = BASE_DIR + "scripts/win_scripts/"
LOG_DIR = BASE_DIR + "logs/"
