======
pyttsx
======

Cross-platform Python wrapper for text-to-speech synthesis

Help Wanted
===========

As you can probably tell, I have not had time or in some cases the resources (e.g., specific versions of OSes) to maintain pyttsx very well for some time now. If you are using pyttsx in your day to day work and would like to take over as maintainer of the project, please let me know.

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

See Also
========

https://github.com/parente/espeakbox - espeak in a 16.5 MB Docker container with a simple REST API

License
=======

Copyright (c) 2009, 2013 Peter Parente
All rights reserved.

http://creativecommons.org/licenses/BSD/
