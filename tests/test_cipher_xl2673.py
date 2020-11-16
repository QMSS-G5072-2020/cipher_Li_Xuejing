from cipher_xl2673 import __version__
from cipher_xl2673 import cipher_xl2673

def test_version():
    assert __version__ == '0.1.0'

def test_singleword_cipher():
    example = 'bird'
    expected = 'cjse'
    actual = cipher_xl2673.cipher(example, shift=True)
    assert actual == expected
