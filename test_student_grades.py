import pytest
from student_grades import StudentGrades

@pytest.fixture
def student():
    """Fixture to create a StudentGrades instance."""
    return StudentGrades(student_name="Test Student")

def test_set_grades_valid(student):
    """Test setting valid grades."""
    student.set_grades(15, 10, 30)
    assert student.CA1_CA2 == 15
    assert student.MSE == 10
    assert student.ESE == 30

def test_set_grades_invalid(student):
    """Test setting invalid grades."""
    with pytest.raises(ValueError, match="CA1_CA2 must be between 0 and 20"):
        student.set_grades(25, 18, 45)

    with pytest.raises(ValueError, match="MSE must be between 0 and 20"):
        student.set_grades(15, 25, 45)

    with pytest.raises(ValueError, match="ESE must be between 0 and 60"):
        student.set_grades(15, 18, 65)

def test_check_pass_fail_pass_criteria(student):
    """Test pass criteria."""
    student.set_grades(10, 10, 20)  # Total: 40, ESE: 20
    assert student.check_pass_fail() == "Pass"

    student.set_grades(20, 10, 10)  # Total: 40, ESE: 10
    assert student.check_pass_fail() == "Pass"

def test_check_pass_fail_fail_criteria(student):
    """Test fail criteria."""
    student.set_grades(10, 10, 15)  # Total: 35, ESE: 15
    assert student.check_pass_fail() == "Fail"

    student.set_grades(5, 10, 19)  # Total: 34, ESE: 19
    assert student.check_pass_fail() == "Fail"
