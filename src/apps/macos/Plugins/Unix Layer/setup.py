from setuptools import setup

APP = ["UnixLayer.py"]
OPTIONS = {
"includes": ["OutputCodes.py"]
}

setup(
plugin=APP,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
install_requires=['pyobjc']
)
