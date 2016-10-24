import unittest
import doctest
import biografieremoveredlinks

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(biografieremoveredlinks))
    return tests
