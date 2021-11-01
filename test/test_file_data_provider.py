import unittest

import pandas as pd

from app.data.game_results import GameResultsFile



class TestGameFileProvider(unittest.TestCase):
    def setUp(self):
        self.fileProvider = GameResultsFile('./test/sample_data.dat')
        self.expected_file_contents = pd.DataFrame(data=
            {   
                'player_1_name' : ['Lions', 'Tarantulas', 'Lions', 'Tarantulas', 'Lions'],
                'player_1_score' : [3, 1, 1, 3, 4],
                'player_2_name' : ['Snakes', 'FC Awesome', 'FC Awesome', 'Snakes', 'Grouches'],
                'player_2_score' : [3, 0, 1, 1, 0],
            })
    
    def test_get_all_returns_expected_data(self):
        games_expected = self.expected_file_contents.copy()
        games_actual = self.fileProvider.get_all()
        
        self.assertEqual(len(games_actual), len(games_expected), 'Some game data are missing')
        pd.testing.assert_frame_equal(games_expected, games_actual)
        
    def tearDown(self) -> None:
        self.fileProvider = None
        self.expected_file_contents = []