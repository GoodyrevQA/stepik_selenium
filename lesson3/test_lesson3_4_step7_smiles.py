'''https://stepik.org/lesson/237257/step/7?unit=209645'''
'''1. если у фикстуры указан параметр scope = "class", то она выполняться будет только 1 раз для этого класса. 
То есть: 
@pytest.fixture(scope="class") 
 def prepare_faces():
выполнится 1 раз для класса,  но проигнорирует вызов в методе
test_first_smiling_faces(self, prepare_faces, very_important_fixture)
Этот нюанс можно упустить в 5 шаге, если невнимательно изучить его.

2. если у фикстуры есть параметр autouse=True, то она выполнится для всех тестов.
То есть
@pytest.fixture(autouse=True)
 def print_smiling_faces():
выполнится 1 раз для каждого теста и проигнорирует любые дополнительные ее вызовы, если они будут.'''

import pytest

@pytest.fixture(scope="class") #выполняется 1 раз для класса, игнорирует вызов в методе
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True) #выполняется 1 раз для каждого теста, игнорирует вызов в методе
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        pass

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        pass

'''pytest -s -v test_lesson3_4_step7_smiles.py'''