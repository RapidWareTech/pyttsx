======
pyttsx
======

Cross-platform Python wrapper for text-to-speech synthesis

Quickstart
==========

::

   import pyttsx
   engine = pyttsx.init()
   engine.say('Greetings!')
   engine.say('How are you today?')
   engine.runAndWait()

See http://pyttsx.readthedocs.org/ for documentation of the full API.

Included drivers
================

* nsss - NSSpeechSynthesizer on Mac OS X 10.5 and higher
* sapi5 - SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7
* espeak - eSpeak on any distro / platform that can host the shared library (e.g., Ubuntu / Fedora Linux)

Contributing drivers
====================

Email the author if you have wrapped or are interested in wrapping another text-to-speech engine for use with pyttsx.

Project links
=============

* Python Package Index for downloads (http://pypi.python.org/pyttsx)
* GitHub site for source, bugs, and q&a (https://github.com/parente/pyttsx)
* ReadTheDocs for docs (http://pyttsx.readthedocs.org)

License
=======

Copyright (c) 2009, 2013 Peter Parente
All rights reserved.

http://creativecommons.org/licenses/BSD/
