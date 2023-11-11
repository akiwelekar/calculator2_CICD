from calculator.operations import add

def test_add():
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0
