import pytest
from demonstration import Demonstration

def test_looking_for_last_five_executed():
    assert Demonstration.looking_for_last_five_executed([1, {2: {'sdfgf': 'fdg'}}]) == 22
