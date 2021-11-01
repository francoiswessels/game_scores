from typing import List, Tuple
import pandas as pd



def get_win_loss_draw_df(games_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Returns number of won, lost and drawn games per team given a df of game data.
    
    Expected columns for games_df are:
        ['player_1_name', 'player_1_score', 'player_2_name', 'player_2_score']
    '''
    new_df = games_df.copy()
    new_df['player_1_win'] = new_df['player_1_score'] > new_df['player_2_score']
    new_df['player_1_loss'] = new_df['player_1_score'] < new_df['player_2_score']
    new_df['player_1_draw'] = new_df['player_1_score'] == new_df['player_2_score']

    new_df['player_2_win'] = new_df['player_1_loss']
    new_df['player_2_loss'] = new_df['player_1_win']    
    new_df['player_2_draw'] = new_df['player_1_draw']
    
    p1_df = new_df[['player_1_name', 'player_1_win', 'player_1_loss', 'player_1_draw']] \
        .rename(columns={'player_1_name' : 'name', 'player_1_win' : 'won', 'player_1_loss' : 'lost', 'player_1_draw' : 'drawn'})

    p2_df = new_df[['player_2_name', 'player_2_win', 'player_2_loss', 'player_2_draw']] \
        .rename(columns={'player_2_name' : 'name', 'player_2_win' : 'won', 'player_2_loss' : 'lost', 'player_2_draw' : 'drawn'})
    
    wld_df = pd.concat([p1_df, p2_df]).groupby(by='name').agg('sum')

    return wld_df.reset_index() # name, won, lost, drawn


def get_team_points_df(games_df: pd.DataFrame, include_stats=False) -> pd.DataFrame:
    '''
    Where a win earns 3 points, a draw 1 point and loss no points, calculates points scored
    by a team given a df of game data and returns a conveniently sorted df.
    
    Expected columns for games_df are:
        ['player_1_name', 'player_1_score', 'player_2_name', 'player_2_score']
    '''
    wld_df = get_win_loss_draw_df(games_df)
    wld_df['points'] = wld_df.apply(lambda row : row['won'] * 3 + row['drawn'], axis=1 )

    wld_df = wld_df.sort_values(['points', 'name'], ascending=[False, True])

    if include_stats:
        return wld_df[['name', 'points', 'won', 'lost', 'drawn']].reset_index(drop=True)
    else:
        return wld_df[['name', 'points']].reset_index(drop=True)