import os
import sys
sys.path.insert(0, os.path.join('..', '..'))
import pyttsx
import time

count = 0

def started(name):
    print 'started', name

def word(location, length, name):
    print 'word', location, length, name

def finished(completed, name):
    print 'finished', completed, name
    engine.endLoop()

engine = pyttsx.Engine()
engine.connect('started-utterance', started)
engine.connect('finished-utterance', finished)
engine.connect('started-word', word)
print engine.getProperty('rate')
print engine.getProperty('volume')
print engine.getProperty('voice')
print [v.id for v in engine.getProperty('voices')]
#engine.stop()
engine.say('Hello out there. This is a test.', 'utter1')
engine.say('Hello out there again.', 'utter2')
#engine.setProperty('voice', vs[2].id)
#engine.say('This is another one.', 'utter2')
#engine.runAndWait()
engine.startLoop()
#engine.startLoop()
time.sleep(2)