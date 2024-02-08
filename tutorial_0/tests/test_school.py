# as per the training video, these codes are all generated with GPT-4

import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

# Fixtures for Hogwarts teachers and students
@pytest.fixture
def mcgonagall():
    return Teacher('McGonagall')

@pytest.fixture
def harry():
    return Student('Harry')

@pytest.fixture
def hermione():
    return Student('Hermione')

@pytest.fixture
def ron():
    return Student('Ron')

@pytest.fixture
def classroom(mcgonagall, harry):
    return Classroom(mcgonagall, [harry], 'Transfiguration')

# Test adding a student
def test_add_student(classroom, hermione):
    classroom.add_student(hermione)
    assert hermione in classroom.student

# Test removing a student
def test_remove_student(classroom, harry):
    classroom.remove_student(harry.name)
    assert harry not in classroom.student

# Test changing a teacher
def test_change_teacher(classroom, mcgonagall):
    new_teacher = Teacher('Snape')
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher

# Test adding too many students
def test_too_many_students(classroom, ron):
    # Add 10 students to the classroom
    for i in range(10):
        classroom.add_student(Student(f'Student{i}'))
    # Try to add one more student
    with pytest.raises(TooManyStudents):
        classroom.add_student(ron)
