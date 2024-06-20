# from fabric_fast_start.main import add_two_numbers
import fabric_fast_start.main as dw


def test_add_two_numbers():
    assert dw.add_two_numbers(1, 2) == 3
    assert dw.add_two_numbers(0, 0) == 0
    assert dw.add_two_numbers(-1, 1) == 0
    assert dw.add_two_numbers(1, -1) == 0
