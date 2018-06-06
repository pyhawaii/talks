import pytest

from factorial import factorial


class TestFactorial(object):

    def test_base_case(self):
        assert factorial(1) == 1

    def test_some_values(self):
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(10) == 3628800

    def test_boundary(self):
        assert factorial(0) == 1

    def test_negative_input(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_non_integer(self):
        with pytest.raises(TypeError):
            factorial('bob')
