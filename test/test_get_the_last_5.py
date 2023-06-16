from main.main import get_the_last_5, read_


data = read_('../operations.json')


def test_get_5():
    assert type(get_the_last_5(data)) == list
    # assert len(get_the_last_5(data)) == 5


