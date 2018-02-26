# SETUP GUIDE

# STEP 1: PY2APP + PYOBJC
Install both using **pip3**. Both packages are essential.

# STEP 2: RUN setup.py
Switch the parent directory (at `$PROJECT_ROOT/src/apps/macos/Plugins/Unix\ Layer/`) and run as:
```shell
$ python3 setup.py py2app
```

This will create the Plugin. Xcode should auto-detect its presence and the application should function normally.
