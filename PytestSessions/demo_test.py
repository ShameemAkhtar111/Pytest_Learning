import pytest

@pytest.mark.login
def test_d4():
    assert True

def test_d5():
    assert False

@pytest.mark.login
def test_d6():
    assert "hello" == "hello"

def test_common():
    assert "common" == "common"

@pytest.mark.login
def test_d7():
    assert "hello" == "hell0", "'o' is not equal to '0'"