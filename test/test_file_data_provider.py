import unittest
import copy

from app.models.game import GameResult
from app.data_providers import FileDataProvider



class GameDataProvider(unittest.TestCase):
    def setUp(self):
        self.fileProvider = FileDataProvider('./test/sample_data.dat')
        self.expected_file_contents = [
                GameResult('Lions', 3, 'Snakes', 3),
                GameResult('Tarantulas', 1, 'FC Awesome', 0),
                GameResult('Lions', 1, 'FC Awesome', 1),
                GameResult('Tarantulas', 3, 'Snakes', 1),
                GameResult('Lions', 4, 'Grouches', 0)
            ]
    
    def test_get_all_returns_expected_data(self):
        games_expected = copy.deepcopy(self.expected_file_contents)
        games_actual = self.fileProvider.get_all()
        
        self.assertEqual(len(games_actual), len(games_expected), 'Some game data are missing')
        for a, e in zip(games_actual, games_expected):
            self.assertEqual(a, e)
        

    def tearDown(self) -> None:
        self.fileProvider = None
        self.expected_file_contents = []