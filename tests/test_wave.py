
import pytest
from wave_engine.structures import Wave

def test_length():
    w=Wave(0,5,'3',1)
    assert w.length()==5

def test_repr():
    w=Wave(10,12,'A',2)    
    assert repr(w)=="<Wave A L2 [10,12]>"


