'''https://stepik.org/lesson/236918/step/6?unit=209305'''

import pytest

@pytest.mark.xfail(strict = True)
def test_succeed():
    print(1)
    assert True

print(1.1)


@pytest.mark.xfail(reason='причина неизвестна')
def test_not_succeed():
    print(2)
    assert False


@pytest.mark.skip
def test_skipped():
    print(3)
    assert False

'''pytest -rx -v -s test_lesson3_5_step6_strict.py'''
print(3.1)