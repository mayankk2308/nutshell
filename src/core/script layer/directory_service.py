import os
from os import path

_abs_path = path.abspath(__file__)
_script_layer = _abs_path[: _abs_path.rfind("/")]
_core = _script_layer[: _script_layer.rfind("/")]
_src = _core[: _core.rfind("/")]
_base_dir = _src[: _src.rfind("/") + 1]
UNIX_SCRIPTS_DIR = _base_dir + "scripts/unix_scripts/"
WIN_SCRIPTS_DIR = _base_dir + "scripts/win_scripts/"
LOG_DIR = _base_dir + "logs/"
