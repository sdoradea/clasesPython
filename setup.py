from distutils.core import setup
import py2exe
import os
from pathlib import Path
from sqlite3.dbapi2 import Connection
from time import sleep
from random import randint, randrange
import sqlite3
import re
import glob

setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      windows=["bromahack.py"])