import unittest
import script

class TextMain(unittest.TestCase):

    def setUp(self):
        print('About to run a function')

    def test_do_stuff(self):
        text_pram = 10
        results = script.do_stuff(text_pram)
        self.assertEqual(results, 15)

    #def test_do_stuff2(self):
    #    text_pram = 'kdfuf'
    #    results = script.do_stuff(text_pram)
    #    self.assertTrue(isinstance(results, ValueError))
    def test_do_stuff2(self):
        test_pram = 'dehgfil'
        results = script.do_stuff(test_pram)
        self.assertIsInstance(results, ValueError)

    def test_do_stuff3(self):
        test_pram = None
        results = script.do_stuff(test_pram)
        self.assertEqual(results, 'Please enter number')

    def test_do_stuff4(self):
        test_pram = ''
        results = script.do_stuff(test_pram)
        self.assertEqual(results, 'Please enter number')

    def tearDown(self):
        print('Clearing up')

if __name__ == '__main__':
    unittest.main()


    #python -m unittest -v