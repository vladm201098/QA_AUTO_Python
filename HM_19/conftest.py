import pytest
from school import *


@pytest.fixture(scope='class')
def students():
    print('\nAdding students to school')
    school = School()
    anastasiya = Students("Skachek", 1, [9, 10, 9, 10, 9])
    mirsad = Students("Proshych", 2, [8, 9, 8, 9, 7])
    yauheni = Students('Vinahradau', 2, [5, 5, 6, 6, 5])
    aliaksei = Students("Zhendi", 3, [8, 7, 7, 8, 7])
    school.add_student(anastasiya)
    school.add_student(mirsad)
    school.add_student(yauheni)
    school.add_student(aliaksei)
    yield school
    del school.students[:]
    print('\nThere is no any student at school')
