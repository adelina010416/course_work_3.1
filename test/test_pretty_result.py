from main.main import pretty_result, path, read_, get_the_last_5


data = read_(path)
last_5 = get_the_last_5(data)


def test_result():
    assert len(pretty_result(last_5)) == 5
    assert type(pretty_result(last_5)) == list


