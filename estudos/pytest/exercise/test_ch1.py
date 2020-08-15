def test_one():
    assert 1 in [2, 3, 4]


def test_two():
    a = 3
    b = 7
    assert a < b


def test_three():
    assert 'fizz' not in 'fizzbuzz'


def test_four():
    systema = ['dragon', 'falcon', 'grifo']
    assert 'dragon' in systema
    assert systema != []