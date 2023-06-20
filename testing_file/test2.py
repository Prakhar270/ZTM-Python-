import unittest
import script2

class TestGame(unittest.TestCase):

    def setUp(self):
        print("hey.....")

    def test_game(self):
        answer , guess = 5, 5
        result = script2.run_guess(guess, answer)
        self.assertTrue(result)

    def test_game_wrong_guess(self):
        result = script2.run_guess(5, 0)
        self.assertFalse(result)

    def test_game_wrong_number(self):
        result = script2.run_guess(5, 11)
        self.assertFalse(result)

    def test_game_wrong_type(self):
        result = script2.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()