import pytest

@pytest.mark.skip(reason='Причина пропуска')
def test_skip():
    assert True


@pytest.mark.xfail(condition=True, reason='причина по которой тестовая функция помечена как xfail')
def test_xfail_1():

    """
    если тест упадет, он пометится как skipped - тест пропущен
    если тест пройдет, он пометится как passed - тест пройден
    в этих двух случаях в отчет добавится тег ожидаемый сбой
    """
    assert False

@pytest.mark.xfail(condition=True, reason='причина по которой тестовая функция помечена как xfail')
def test_xfail_2():
    assert True


@pytest.mark.skipif(condition='2+2 != 5')
def test_skip_by_triggered_condition():
    pass


@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0