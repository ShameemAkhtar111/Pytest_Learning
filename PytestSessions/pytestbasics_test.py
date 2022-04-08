import pytest

def test_d1():
    a=4
    b=5
    assert a+1 == b, "a+1 is not equal to b"
    assert a==b, "a is not equal to b"

def test_d2():
    name="pyt"
    assert name.upper() == "PYT"

@pytest.mark.home
def test_d3():
    name = "selenium"
    assert name == "SELENIUM", "Upper case and lowercase not equal"

def test_common():
    assert "common" == "common"