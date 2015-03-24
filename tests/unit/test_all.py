'''
Runs all unit tests.

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
import test_say
import test_prop
import test_lifecycle
import test_utilities

def suite():
    suite = unittest.TestSuite([
        test_lifecycle.suite(),
        test_prop.suite(),
        test_say.suite(),
        test_utilities.suite()
    ])
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())