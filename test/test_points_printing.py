import unittest

from app.data.game_results_providers import GameResultsFile
from app.services.points_calc_service import get_team_points_df
from app.services.points_output_service import get_leader_board



class TestScorePringing(unittest.TestCase):
    def setUp(self):
        self.fileProvider = GameResultsFile('./test/sample_data.dat')
        self.basic_result = [
            '1. Tarantulas, 6 pts',
            '2. Lions, 5 pts', 
            '3. FC Awesome, 1 pt',
            '4. Snakes, 1 pt',
            '5. Grouches, 0 pt']
        self.full_result = [
            '                        W   L   D   Pts',
            '1. Tarantulas           2   0   0    6',
            '2. Lions                1   0   2    5',
            '3. FC Awesome           0   1   1    1',
            '4. Snakes               0   1   1    1',
            '5. Grouches             0   1   0    0']
    
    def test_basic_output(self):
        games_df = self.fileProvider.get_all()
        score_df = get_team_points_df(games_df, include_stats=False)
        output_df = get_leader_board(score_df, include_stats=False)
        self.assertListEqual(self.basic_result, output_df)

    def test_full_output(self):
        games_df = self.fileProvider.get_all()
        score_df = get_team_points_df(games_df, include_stats=True)
        output_df = get_leader_board(score_df, include_stats=True)
        self.assertListEqual(self.full_result, output_df)

    def tearDown(self):
        self.fileProvider = None
        self.basic_result = None
        self.full_result = None