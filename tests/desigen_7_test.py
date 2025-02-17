import re
from unittest import result

import pytest
from desigen_7 import roll_dice ,yahtzee
from unittest.mock import patch
def test_roll_dice_n_times_len():
    n = 100
    result = len(roll_dice(n))
    assert result == n
    
def test_roll_dice_n_times_values():
    n = 100
    result = roll_dice(n)
    assert all([1 <= x <= 6 for x in result])
    
@patch("random.choice", side_effect=[1, 1, 1, 1, 1])
def test_roll_dice_all_same(mock_choice):
    result = roll_dice(5)
    assert result == [1, 1, 1, 1, 1]


def test_yahtzee_Probability():
    num_games = 10000
    winning_games = list(
        filter(
            lambda x: x == 5,
            [yahtzee() for _ in range(num_games)],
        )
    )
    return len(winning_games)
    

    
@pytest.mark.parametrize("itereation", range(10))
def test_func_test_yahtzee_Probability(itereation):
   result = test_yahtzee_Probability()
   print(result)
   assert result in range (200, 800)
   
@patch("random.choice", side_effect=[
    2, 2, 2, 3, 4,  
    2, 3,           
    2             
])
def test_func_test_yahtzee_Probability(mock_choice):
    result = yahtzee()
    assert result == 5