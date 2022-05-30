import pytest
from school import *


@pytest.fixture(scope='class')
def students():
    print('\nAdding students to school')
    school = School()
    ulyana = Students("Hampe", 1, [9, 10, 9, 10, 9])
    vladislav = Students("Medvedev", 2, [8, 9, 8, 9, 7])
    dmitry = Students('Sadovskiy', 2, [5, 5, 6, 6, 5])
    alesya = Students("Kapashilova", 3, [8, 7, 7, 8, 7])
    school.add_student(ulyana)
    school.add_student(vladislav)
    school.add_student(dmitry)
    school.add_student(alesya)
    yield school
    del school.students[:]
    print('\nThere is no any student at school')

