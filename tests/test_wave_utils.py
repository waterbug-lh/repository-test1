import pytest
from wave_utils import safe_divide,fibonacci_ratio

def test_safe_divide():
    assert safe_divide(10,2)==5
    assert safe_divide(1,0) is None

def test_fibonacci_ratio():
    assert fibonacci_ratio(1,1.618,tol=0.02)
    assert not fibonacci_ratio(1,2.0)
