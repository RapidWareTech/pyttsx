'''
Tests properties.

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
from pyttsx.six.moves import xrange

class TestProperties(unittest.TestCase):
    
    def setUp(self):
        self.engine = pyttsx.init(debug=False)

    def tearDown(self):
        del self.engine

    def testDefaults(self):
        voices = self.engine.getProperty('voices')
        drate = 200
        dvolume = 1.0

        rate = self.engine.getProperty('rate')
        self.assert_(drate == rate)
        volume = self.engine.getProperty('volume')
        self.assert_(dvolume == volume)
        voice = self.engine.getProperty('voice')
        self.assert_(voice in [v.id for v in voices])

    def testSetRate(self):
        for rate in xrange(100, 400, 10):
            self.engine.setProperty('rate', rate)
            self.engine.runAndWait()
            grate = self.engine.getProperty('rate')
            self.assert_(rate == grate)

    def testSetVoice(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if (any(letter.isupper() for letter in voice.id)):
                #eSpeak has a bug where it is impossible to select a voice by name if the name has a capital letter.
                #One possible workaround is to use the voice 'identifier' instead of the voice 'name' as the pyttsx id field
                continue
            self.engine.setProperty('voice', voice.id)
            self.engine.runAndWait()
            gvoice = self.engine.getProperty('voice')
            self.assert_(voice.id == gvoice)

    def testSetVolume(self):
        for volume in xrange(0, 100, 1):
            volume /= 100.0
            self.engine.setProperty('volume', volume)
            self.engine.runAndWait()
            gvolume = self.engine.getProperty('volume')
            self.assertAlmostEqual(volume, gvolume, 4)

    def testSetMultiple(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('volume', 0.5)
        self.engine.setProperty('rate', 300)
        self.engine.setProperty('voice', voices[0].id)
        self.engine.runAndWait()
        gvoice = self.engine.getProperty('voice')
        self.assert_(gvoice == voices[0].id)
        gvolume = self.engine.getProperty('volume')
        self.assertAlmostEqual(gvolume, 0.5, 4)
        grate = self.engine.getProperty('rate')
        self.assert_(grate == 300)

    def testBadVolume(self):
        errors = []
        def errback(exception, name):
            errors.append(exception)
        tok = self.engine.connect('error', errback)
        self.engine.setProperty('volume', 'foobar')
        self.engine.setProperty('volume', None)
        self.engine.setProperty('volume', object())
        self.engine.runAndWait()
        self.engine.disconnect(tok)
        for error in errors:
            self.assert_(isinstance(error, ValueError))

    def testBadRate(self):
        errors = []
        def errback(exception, name):
            errors.append(exception)
        tok = self.engine.connect('error', errback)
        self.engine.setProperty('rate', 'foobar')
        self.engine.setProperty('rate', None)
        self.engine.setProperty('rate', object())
        self.engine.runAndWait()
        self.engine.disconnect(tok)
        for error in errors:
            self.assert_(isinstance(error, ValueError))

    def testBadVoice(self):
        errors = []
        def errback(exception, name):
            errors.append(exception)
        tok = self.engine.connect('error', errback)
        self.engine.setProperty('voice', 'foobar')
        self.engine.setProperty('voice', 100)
        self.engine.setProperty('voice', 1.0)
        self.engine.setProperty('voice', None)
        self.engine.setProperty('voice', object())
        self.engine.runAndWait()
        self.engine.disconnect(tok)
        for error in errors:
            self.assert_(isinstance(error, ValueError))

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProperties)
    #suite = unittest.TestLoader().loadTestsFromName('testSetVoice', TestProperties)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
