import pytest
pytest.main([__file__, ''])


def por_extenso(valor):
    return 'um'

def test_1():
    assert por_extenso(1) == 'um'

