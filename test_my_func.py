import pytest
from my_func import my_func_plus


@pytest.mark.parametrize('args, expected_result', [
    ((2,4,1), (6)),
    ((15, 25, 5), (8))
])
def test_my_func_pytest(args, expected_result):
    res = my_func_plus(*args)
    assert res ==expected_result