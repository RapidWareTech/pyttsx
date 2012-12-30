'''
Tests lifecycle.

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

class TestLifecycle(unittest.TestCase):
    def setUp(self):
        self.engine = pyttsx.init()

    def tearDown(self):
        del self.engine

    def testSeparateDrivers(self):
        self.engine2 = pyttsx.init('dummy')
        self.assert_(self.engine != self.engine2)
        del self.engine2

    def testReuseDriver(self):
        self.engine2 = pyttsx.init()
        self.assert_(self.engine == self.engine2)
        del self.engine2

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLifecycle)
    #suite = unittest.TestLoader().loadTestsFromName('testBadVoice', TestProperties)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())