"""
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Codec-Graph.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'Resources/Icon.icns',
    'plist': {
        'CFBundleDevelopmentRegion': 'English',
        'CFBundleIdentifier': "com.Core-i99.Codec-Graph",
        'CFBundleVersion': "1.4",
        'NSHumanReadableCopyright': "Copyright © 2022, Stijn Rombouts, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
