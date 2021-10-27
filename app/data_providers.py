from abc import ABC, abstractmethod
from typing import List

from .models.game import GameResult



class DataProviderBase(ABC):
    @abstractmethod
    def get_all(self) -> List[GameResult]:
        pass


class FileDataProvider(DataProviderBase):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    
    def get_all(self) -> List[GameResult]:
        with open(self.file_name, 'r') as file:
            return [self._process_line(l) for l in file.readlines()]
    
    def _process_line(self, line: str) -> GameResult:
        # consider using csv module here instead, but this works
        result = dict()
        for i, half_res in enumerate(line.strip().split(',')):
            assert i < 2, 'Found more than two results in data row'
            score = half_res.strip().split(' ')[-1]
            result[f'p{i}'] = half_res.replace(score, '').strip()
            result[f'p{i}_r'] = int(score)
        return GameResult(result['p0'], result['p0_r'], result['p1'], result['p1_r'])