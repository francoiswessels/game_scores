import argparse
import os.path as path
from pathlib import Path

from app.data.game_results import GameResultsFile
from app.services.score_calc_service import get_team_points_df
from app.services.score_output_service import get_leader_board


def run(args):
    if not path.exists(Path(args.file_path)):
        print(f'Could not find {args.file_path}')
        return None

    games_df = GameResultsFile(Path(args.file_path)).get_all()
    points_df = get_team_points_df(games_df, include_stats=args.stat)
    for line in get_leader_board(points_df, include_stats=args.stat):
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI League Ranking')
    parser.add_argument('file_path', help='the path to the game results file', type=str)
    parser.add_argument('-s', '--stat', action='store_true', help='include the won, lost, drawn stats ahead of the leaderboard')
    args = parser.parse_args()
    
    run(args)