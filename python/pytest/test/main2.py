from src.folder.code2 import inc, dinc, ceil


def test_inc2():
    assert inc(3) == 4


def test_dinc2():
    assert dinc(3) == 2

def test_ceil():
    assert ceil(1.1) == 2