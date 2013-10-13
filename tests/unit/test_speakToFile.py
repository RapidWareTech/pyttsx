'''
Created on Oct 13, 2013

@author: humbled
'''
import unittest
import test_setup
import itertools

from test_base_commands import BaseCommandTest
import tempfile
import os
import logging

class TestSpeakToFile(BaseCommandTest):
    utters = ['This is the first utterance',
              'The second is an utterance as well']
    # Filenames to save to in tests that will get saved in tmp dir (full paths at self.filepaths)
    _filenames = ['test_one.wav', 'test_two.wav']
    names = ['utter1', 'utter2']
    
    def setUp(self):
        self._tmpdir = tempfile.mkdtemp(prefix="pyttsx_test")
        self.filepaths = [os.path.join(self._tmpdir, f) for f in self._filenames]
        super(TestSpeakToFile, self).setUp()
        
    def testSpeakToFile(self):
        filepath = self.filepaths[0]
        self.engine.speakToFile(self.utters[0], filepath, self.names[0])
        logging.info("test attempting to save speech file to: %s" % filepath)
        self.engine.runAndWait()

        # number of events check
        self.assert_(len(self.events) == len(self.correct[0]))
        # event data check
        for cevent, tevent in zip(self.correct[0], self.events):
            self.assertEqual(cevent, tevent)
            
        # Now check file is there
        self.assert_(os.path.exists(filepath))
        # And is a file
        self.assert_(os.path.isfile(filepath))
        self.assert_(os.path.getsize(filepath) > 0)
        
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpeakToFile)
    return suite

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    unittest.TextTestRunner(verbosity=2).run(suite())