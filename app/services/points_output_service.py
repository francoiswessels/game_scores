from typing import List
import pandas as pd



def get_leader_board(points_df: pd.DataFrame, include_stats: bool = False) -> List[str]:
    lines = []
    if include_stats:
        lines += [f'{"":22}  W   L   D   Pts']
    
    for i, row in enumerate(points_df.iterrows()):
        row = row[1]
        points = row['points']
        name = row['name']
        if include_stats:
            lines += [f'{i+1}. {name[:20]:20} {row["won"]}   {row["lost"]}   {row["drawn"]}    {points}']
        else:
            lines += [f'{i+1}. {name}, {points} pt{"s" if points > 1 else ""}']
    
    return lines