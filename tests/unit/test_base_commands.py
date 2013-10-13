'''
Common base code for tests of pyttsx commands

Created on Oct 13, 2013

@author: humbled
'''
import unittest
import pyttsx

class BaseCommandTest(unittest.TestCase):
    
    def setUp(self):
        self.correct = []
        for utter, name in zip(self.utters, self.names):
            events = [{'type' : 'started-utterance'}]
            last = 0
            for word in utter.split(' '):
                event = {'type' : 'started-word'}
                event['length'] = len(word)
                event['location'] = last
                events.append(event)
                last += len(word) + 1
            events.append({'type' : 'finished-utterance', 'completed' : True})
            for event in events:
                event['name'] = name
            self.correct.append(events)

        self.events = []
        self.engine = pyttsx.init(debug=False)
        self.engine.connect('started-utterance', self._onUtterStart)
        self.engine.connect('started-word', self._onUtterWord)
        self.engine.connect('finished-utterance', self._onUtterEnd)
        self.engine.connect('error', self._onUtterError)
    
    def tearDown(self):
        del self.engine

    def _onUtterStart(self, **kwargs):
        event = {'type' : 'started-utterance'}
        event.update(kwargs)
        self.events.append(event)

    def _onUtterWord(self, **kwargs):
        event = {'type' : 'started-word'}
        event.update(kwargs)
        self.events.append(event)

    def _onUtterEnd(self, **kwargs):
        event = {'type' : 'finished-utterance'}
        event.update(kwargs)
        self.events.append(event)

    def _onUtterError(self, **kwargs):
        event = {'type' : 'error'}
        event.update(kwargs)
        self.events.append(event)