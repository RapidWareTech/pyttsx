'''
Tests say.

Copyright (c) 2009, 2013 Peter Parente

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''
import unittest
import test_setup
import pyttsx
import itertools
from pyttsx.six.moves import filter

class TestSay(unittest.TestCase):
    utters = ['This is the first utterance and is longer now',
              'The second is an utterance as well']
    names = ['utter1', 'utter2']

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

    def testSay(self):
        self.engine.say(self.utters[0], self.names[0])
        self.engine.runAndWait()

        # number of events check
        self.assert_(len(self.events) == len(self.correct[0]))
        # event data check
        for cevent, tevent in zip(self.correct[0], self.events):
            self.assert_(cevent == tevent)

    def testMultipleSay(self):
        self.engine.say(self.utters[0], self.names[0])
        self.engine.say(self.utters[1], self.names[1])
        self.engine.runAndWait()
        # number of events check
        self.assert_(len(self.events) == len(self.correct[0]) + len(self.correct[1]))
        # event data check
        correct = itertools.chain(*self.correct)
        for cevent, tevent in zip(correct, self.events):
            self.assert_(cevent == tevent)

    def testSayTypes(self):
        self.engine.say(1.0)
        self.engine.say(None)
        self.engine.say(object())
        self.engine.runAndWait()
        # event data check
        errors = list(filter(lambda e: e['type'] == 'error', self.events))
        self.assert_(len(errors) == 0)

    def testStop(self):
        tok = None
        def _onWord(**kwargs):
            self.engine.stop()
            self.engine.disconnect(tok)
        tok = self.engine.connect('started-word', _onWord)
        self.engine.say(self.utters[0], self.names[0])
        self.engine.runAndWait()
        # make sure it stopped short
        self.assert_(len(self.events) < len(self.correct[0]))
        end = self.events[-1]
        self.assert_(not end['completed'])

    def testStopBeforeSay(self):
        self.engine.stop()
        self.testSay()

    def testMultipleStopBeforeSay(self):
        self.engine.stop()
        self.engine.stop()
        self.testSay()

    def testStartEndLoop(self):
        def _onEnd(**kwargs):
            self.engine.endLoop()
        self.engine.connect('finished-utterance', _onEnd)
        self.engine.say(self.utters[0], self.names[0])
        self.engine.startLoop()
        # number of events check
        self.assert_(len(self.events) == len(self.correct[0]))
        # event data check
        for cevent, tevent in zip(self.correct[0], self.events):
            self.assert_(cevent == tevent)

    def testExternalLoop(self):
        def _onEnd(**kwargs):
            self.engine.endLoop()

        # kill the engine built by setUp
        del self.engine
        self.engine = pyttsx.init('dummy')
        self.engine.connect('started-utterance', self._onUtterStart)
        self.engine.connect('started-word', self._onUtterWord)
        self.engine.connect('finished-utterance', self._onUtterEnd)
        self.engine.connect('error', self._onUtterError)
        self.engine.connect('finished-utterance', _onEnd)
        self.engine.say(self.utters[0], self.names[0])
        self.engine.startLoop(False)
        self.engine.iterate()
        # number of events check
        self.assert_(len(self.events) == len(self.correct[0]))
        # event data check
        for cevent, tevent in zip(self.correct[0], self.events):
            self.assert_(cevent == tevent)

    def testMultipleRuns(self):
        self.testSay()
        self.events = []
        self.testSay()

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSay)
    #suite = unittest.TestLoader().loadTestsFromName('testStop', TestSay)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
