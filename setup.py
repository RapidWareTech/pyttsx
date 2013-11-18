'''
pyttsx setup script.

Copyright (c) 2009, 2013 Peter Parente

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED 'AS IS' AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''
import platform
from setuptools import setup

install_requires = []
if platform.system() == 'Windows':
    install_requires = [
        'win32com'
    ]
elif platform.system() == 'Darwin':
    install_requires = [
        'pyobjc>=2.4'
    ]

setup(name='pyttsx',
      version='1.2',
      description='pyttsx - cross platform text-to-speech',
      long_description='pyttsx is a Python package supporting common text-to-speech engines on Mac OS X, Windows, and Linux.',
      author='Peter Parente',
      author_email='parente@cs.unc.edu',
      url='https://github.com/parente/pyttsx',
      download_url='http://pypi.python.org/pypi/pyttsx',
      license='BSD License',
      packages=['pyttsx', 'pyttsx.drivers'],
      install_requires=install_requires
)