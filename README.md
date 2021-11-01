# CLI League Ranking

game_score is a maintainable, testable command-line application that will calculate the ranking table for a league, given some standard input, which looks like this:

>Lions 3, Snakes 3  
>Tarantulas 1, FC Awesome 0  
>Lions 1, FC Awesome 1  
>Tarantulas 3, Snakes 1  
>Lions 4, Grouches 0  

## Requirements

The solution was developed using pandas 1.2.5 and Python 3.8. This is not the latest version of either pandas or Python, and the solution is fairly simple so should not be particualrly sensitive to these versions straying a bit from the dev versions. The solution does rely on pandas test functions for some unit testing, so if you do encounter some errors, double check your pandas version - this is the most likely to be a source of error, because pandas testing does evolve a bit.

## Usage

There are two result format available, the standard one:`

```shell
user@host:~$ python3 app.py ./test/sample_data.dat
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
4. Snakes, 1 pt
5. Grouches, 0 pt
```
... and a 'with stats' (-s) view that includes wins, losses, and draws:

```shell
user@host:~$ python3 app.py -s ./test/sample_data.dat
                        W   L   D   Pts
1. Tarantulas           2   0   0    6
2. Lions                1   0   2    5
3. FC Awesome           0   1   1    1
4. Snakes               0   1   1    1
5. Grouches             0   1   0    0
```

`python3` may need to be substituted with `python`, depending on the specifics if your installation.

Guidance on usage is also available as follows:

```shell
user@host:~$ python3 app.py -h
usage: app.py [-h] [-s] file_path

CLI League Ranking

positional arguments:
  file_path   the path to the game results file

optional arguments:
  -h, --help  show this help message and exit
  -s, --stat  include the won, lost, drawn stats ahead of the leaderboard
```

## Testing

The solution contains automated tests, written using unittest from the Python standard library. They can be run as follows:


```shell
user@host:~$ python3 -m unittest -v
test_get_all_returns_expected_data (test.test_file_data_provider.TestGameFileProvider) ... ok
test_get_team_points (test.test_score_calc_service.TestScoreCalcs) ... ok
test_get_team_points_with_stats (test.test_score_calc_service.TestScoreCalcs) ... ok
test_get_wins_losses_draws (test.test_score_calc_service.TestScoreCalcs) ... ok
test_basic_output (test.test_score_printing.TestScorePringing) ... ok
test_full_output (test.test_score_printing.TestScorePringing) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.098s

OK
```

or if you don't want to see the test details:

```shell
user@host:~$ python3 -m unittest
......
----------------------------------------------------------------------
Ran 6 tests in 0.094s

OK
```
