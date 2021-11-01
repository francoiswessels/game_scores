import unittest
from numpy.lib.shape_base import expand_dims

import pandas as pd

from app.data.game_results import GameResultsFile
from app.services.score_calc_service import get_team_points_df, get_win_loss_draw_df



class TestScoreCalcs(unittest.TestCase):
    def setUp(self):
        self.fileProvider = GameResultsFile('./test/sample_data.dat')
        self.full_expected_results = pd.DataFrame({
            'name' : ['Tarantulas', 'Lions', 'FC Awesome', 'Snakes', 'Grouches'],
            'points' : [ 6, 5, 1, 1, 0],
            'won' : [2, 1, 0, 0, 0],
            'lost' : [0, 0, 1, 1, 1],
            'drawn' : [0, 2, 1, 1, 0]
        })
    
    def test_get_wins_losses_draws(self):
        expected_df = pd.DataFrame({
            'name' : ['FC Awesome','Grouches','Lions','Snakes','Tarantulas'],
            'won' : [0,0,1,0,2],
            'lost' : [1,1,0,1,0],
            'drawn' : [1,0,2,1,0]
        })

        games_df = self.fileProvider.get_all()
        actual_df = get_win_loss_draw_df(games_df)
        pd.testing.assert_frame_equal(expected_df, actual_df)

    def test_get_team_points(self):
        expected_df = self.full_expected_results[['name', 'points']].copy()
        games_df = self.fileProvider.get_all()
        actual_df = get_team_points_df(games_df)
        pd.testing.assert_frame_equal(expected_df, actual_df)
    
    def test_get_team_points_with_stats(self):
        expected_df = self.full_expected_results.copy()
        games_df = self.fileProvider.get_all()
        actual_df = get_team_points_df(games_df, include_stats=True)
        pd.testing.assert_frame_equal(expected_df, actual_df)

    def tearDown(self) -> None:
        self.fileProvider = None
        self.full_expected_results = None