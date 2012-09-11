import os
from distutils.core import setup

from brick import __version__

try:
    import setuptools
except ImportError:
    pass


with open(os.path.abspath('README.md')) as f:
    long_description = f.read()

setup(

    name="brick",
    version=__version__,
    packages=['brick'],
    author="Garindra Prahandono",
    author_email="garindraprahandono@gmail.com",
    url='https://github.com/garindra/brick',
    description="brick is a pure python templating system.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)

