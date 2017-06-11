import unittest
from unittests.test_loadjson import LoadJsonTestCase
from unittests.test_makerequest import MakeRequestTestCase
from unittests.test_rest import RestCallTestCase


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(RestCallTestCase())
    test_suite.addTest(MakeRequestTestCase())
    test_suite.addTest(LoadJsonTestCase())
    return test_suite

if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)