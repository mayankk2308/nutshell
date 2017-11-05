import os
from os import path

_abs_path = path.abspath(__file__)
_core = _abs_path[0 : _abs_path.rfind("/")]
_src = _core[0 : _core.rfind("/")]
_base_dir = _src[0 : _src.rfind("/") + 1]
UNIX_SCRIPTS_DIR = _base_dir + "scripts/unix_scripts/"
WIN_SCRIPTS_DIR = _base_dir + "scripts/win_scripts/"
LOG_DIR = _base_dir + "logs/"
