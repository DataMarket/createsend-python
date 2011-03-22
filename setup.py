import sys
import os
import re
from setuptools import setup

v = open(os.path.join(os.path.dirname(__file__), 'createsend', 'createsend.py'))
__version__ = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

setup(name = "createsend",
      version = __version__,
      description = "A library which implements the complete functionality of v3 of the createsend API.",
      author = "James Dennes",
      author_email = 'jdennes@gmail.com',
      install_requires = ['simplejson'] if sys.version_info < (2, 6) else [],
      packages = ['createsend'])
