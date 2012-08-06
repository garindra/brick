import os
from distutils.core import setup

try:
    import setuptools
except ImportError:
    pass


with open(os.path.abspath('README.md')) as f:
    long_description = f.read()

setup(

    name="brick",
    version="0.0.1",
    packages=['brick'],
    author="Garindra Prahandono",
    author_email="garindraprahandono@gmail.com",
    url='https://github.com/garindra/brick',
    description="brick is a pure python templating system.",
    long_description=long_description
)

