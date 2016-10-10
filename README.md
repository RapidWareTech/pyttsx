# pyttsx

Cross-platform Python wrapper for text-to-speech synthesis

## Quickstart

```python
import pyttsx
engine = pyttsx.init()
engine.say('Greetings!')
engine.say('How are you today?')
engine.runAndWait()
```

See http://pyttsx.readthedocs.org/ for documentation of the full API.

## Included drivers

* nsss - NSSpeechSynthesizer on Mac OS X 10.5 and higher
* sapi5 - SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7
* espeak - eSpeak on any distro / platform that can host the shared library (e.g., Ubuntu / Fedora Linux)

## Project links

* Python Package Index for downloads (http://pypi.python.org/pyttsx)
* GitHub site for source, bugs, and q&a (https://github.com/parente/pyttsx)
* ReadTheDocs for docs (http://pyttsx.readthedocs.org)

## See Also

https://github.com/parente/espeakbox - espeak in a 16.5 MB Docker container with a simple REST API

## Release guide

1. Update `doc/releases.rst` with the release notes and commit it to master.
2. Run the unit tests `python test/unit/test_all.py` on all platforms of interest.
3. Git tag the last commit (e.g., v1.3) and push the tag to GitHub.
4. Run `python setup.py register upload` to push a release to PyPI.
5. Bump the version number in `setup.py` and `docs/conf.py` (e.g., 1.4).
6. Commit and push the version bump to GitHub.
