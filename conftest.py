import pytest
 
@pytest.fixture
def input_total( ):
    total = 100
    return total

@pytest.fixture
def day1_6s_file( ):
    return "test_inputs/day1_6s.txt"


@pytest.fixture
def day1_1_file( ):
    return "test_inputs/day1_1.txt"