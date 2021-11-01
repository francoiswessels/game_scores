from abc import ABC, abstractmethod
from typing import List

import pandas as pd

GAME_RESULT_COLUMNS = ['player_1_name', 'player_1_score', 'player_2_name', 'player_2_score']


class ResultsProviderBase(ABC):
    @abstractmethod
    def get_all(self) -> pd.DataFrame:
        pass


class GameResultsFile(ResultsProviderBase):
    '''Reads game results from a text file and returns them in a pandas dataframe.
    
    Expects data to be arranged:
        player_1_name player_1_score, player_2_name player_2_score
    '''
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    
    def get_all(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_name, sep=',', names=['game_1', 'game_2'])
        df = df.apply(self._process_game_row, axis=1)
        return df[GAME_RESULT_COLUMNS]
    
    def _process_game_row(self, row: str) -> pd.DataFrame:
        names, scores = [], []
        for i in [1,2]:
            stpd = row[f'game_{i}'].strip()
            g = stpd.split(' ')
            scores += [int(g[-1])]
            names += [stpd.replace(g[-1], '').strip()]

        row['player_1_name'], row['player_1_score'] = names[0], scores[0]
        row['player_2_name'], row['player_2_score'] = names[1], scores[1]
        
        return row