# coding=utf-8
'''
Created on Mar 24, 2015

@author: pace
'''

import unittest
import test_setup
import codecs
from pyttsx.drivers import toUtf8, fromUtf8
from pyttsx.six import indexbytes, binary_type

#Some constants for testing
LOWER_CASE_L_UTF_8 = 0x6C
LOWER_CASE_S_UTF_8 = 0x73
LOWER_CASE_O_WITH_UMLAUT_UTF_8_1 = 0xC3
LOWER_CASE_O_WITH_UMLAUT_UTF_8_2 = 0xB6
MOSE_WITH_UMLAUT_HEX = b"\x6D\xC3\xB6\x73\x65"

class TestUtilities(unittest.TestCase):
    
    
    class SimpleObj(object):
        
        def __str__(self):
            return "Hello"
        
        def __repr__(self):
            return "Goodbye"
        
    class NoStrObj(object):
        
        def __repr__(self):
            return "Blah"
        
    class NothingObj(object):
        
        pass
    
    def testToUtf8(self):
        #Converting string literals and unicode string literals (same thing in 3.X)
        utfBytes = toUtf8("This is a test")
        utfBytes2 = toUtf8(u"This is a test")
        self.assertEquals(utfBytes, utfBytes2)
        self.assertEquals(14, len(utfBytes))
        self.assertEquals(LOWER_CASE_S_UTF_8, indexbytes(utfBytes, 3))
        
        #Converting objects with a __str__ method
        utfBytes = toUtf8(TestUtilities.SimpleObj())
        self.assertEquals(5, len(utfBytes))
        self.assertEquals(LOWER_CASE_L_UTF_8, indexbytes(utfBytes, 2))
        
        #Converting objects without a __repr__ method
        utfBytes = toUtf8(TestUtilities.NoStrObj())
        self.assertEquals(4, len(utfBytes))
        self.assertEquals(LOWER_CASE_L_UTF_8, indexbytes(utfBytes, 1))
        
        #Converting objects without __str__ or __repr__ (don't care what it is as long as it is non-empty)
        utfBytes = toUtf8(TestUtilities.NothingObj())
        self.assertTrue(len(utfBytes) > 0)
        
        #Test an actual unicode string with more complex (multi-byte) characters
        utfBytes = toUtf8(u"möse")
        self.assertEquals(5, len(utfBytes))
        self.assertEquals(LOWER_CASE_O_WITH_UMLAUT_UTF_8_1, indexbytes(utfBytes, 1))
        self.assertEquals(LOWER_CASE_O_WITH_UMLAUT_UTF_8_2, indexbytes(utfBytes, 2))
    
    def testFromUtf8(self):
        utfString = fromUtf8(MOSE_WITH_UMLAUT_HEX)
        self.assertEquals(u"möse", utfString)
        
        self.assertEquals(u"Hello World", fromUtf8(toUtf8(u"Hello World")))
        self.assertEquals(u"Hello World", fromUtf8(toUtf8("Hello World")))
        self.assertEquals(u"Hello", fromUtf8(toUtf8(TestUtilities.SimpleObj())))
        self.assertEquals(u"Blah", fromUtf8(toUtf8(TestUtilities.NoStrObj())))
    
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilities)
    #suite = unittest.TestLoader().loadTestsFromName('testToUtf8', TestUtilities)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
