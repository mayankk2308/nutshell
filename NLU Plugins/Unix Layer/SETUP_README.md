# SETUP GUIDE
Before running the macOS application and opening **Xcode**, follow these steps to set up your environment and prepare the Python Unix Layer plugin.

## STEP 1: PY2APP + PYOBJC
Install both using **pip3**. Both packages are essential.

## STEP 2: RUN setup.py
Switch the parent directory (at `$PROJECT_ROOT/src/apps/macos/Plugins/Unix\ Layer/`) and run as:
```shell
$ python3 setup.py py2app
```

This will create the Plugin. Xcode should auto-detect its presence and the application should function normally.
