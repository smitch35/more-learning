import unittest
from src.game.adventure import Adventure

class TestAdventure(unittest.TestCase):

    def setUp(self):
        self.adventure = Adventure()

    def test_initial_state(self):
        self.assertEqual(self.adventure.state, 'not started')

    def test_start_game(self):
        self.adventure.start_game()
        self.assertEqual(self.adventure.state, 'in progress')

    def test_player_action(self):
        self.adventure.start_game()
        self.adventure.player_action('explore')
        self.assertIn('You explore the surroundings.', self.adventure.messages)

    def test_game_over(self):
        self.adventure.start_game()
        self.adventure.player_action('fail')
        self.assertEqual(self.adventure.state, 'game over')

    def test_restart_game(self):
        self.adventure.start_game()
        self.adventure.player_action('fail')
        self.adventure.restart_game()
        self.assertEqual(self.adventure.state, 'not started')

if __name__ == '__main__':
    unittest.main()