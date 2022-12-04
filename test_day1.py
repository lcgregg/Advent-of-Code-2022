import pytest
from day1_caloriecounter import calorie_counter
 
def test_array_of_len_3_w_all_values_of_6(day1_6s_file):
    assert [6,6,6] == calorie_counter(day1_6s_file)

def test_array_of_len_1_w_value_of_1(day1_1_file):
    assert [1] == calorie_counter(day1_1_file)