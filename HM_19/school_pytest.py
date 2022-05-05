import pytest

class TestSchool:

    @pytest.mark.positive
    def test_add_student_positive(self, students):
        assert len(students.students) == 4

    @pytest.mark.positive
    def test_marks_one_student_positive(self, students):
        assert students.marks(5, 6) == 'Vinahradau '

    @pytest.mark.positive
    def test_marks_some_students_positive(self, students):
        assert students.marks(7, 8) == ('Zhendi ')

    @pytest.mark.positive
    @pytest.mark.parametrize("group, exp_res", [
        (1, "Skachek "),
        (3, "Zhendi "),
        (2, "Proshych Vinahradau ")
    ])
    def test_group_positive(self, group, exp_res, students):
        assert students.group(group) == exp_res

    @pytest.mark.positive
    @pytest.mark.parametrize("automat, exp_res", [
        (9, "Skachek "),
        (6, "Skachek Proshych Zhendi "),
        (5, "Skachek Proshych Vinahradau Zhendi ")
    ])
    def test_automat_positive(self, automat, exp_res, students):
        assert students.automat(automat) == exp_res

    @pytest.mark.negative
    def test_add_student_negative(self, students):
        assert len(students.students) != 8

    @pytest.mark.negative
    def test_marks_one_student_negative(self, students):
        assert students.marks(9, 10) != 'Vinahradau '

    @pytest.mark.negative
    def test_marks_some_students_negative(self, students):
        assert students.marks(6, 7) != ('Skachek Vinahradau ')

    @pytest.mark.negative
    @pytest.mark.parametrize("group, exp_res", [
        (3, "Proshych Vinahradau "),
        (1, "Zhendi "),
        (2, "Skachek ")
    ])
    def test_group_negative(self, group, exp_res, students):
        assert students.group(group) != exp_res

    @pytest.mark.negative
    @pytest.mark.parametrize("automat, exp_res", [
        (9, "Proshych "),
        (6, "Proshych Zhendi "),
        (5, "Skachek Vinahradau ")
    ])
    def test_automat_negative(self, automat, exp_res, students):
        assert students.automat(automat) != exp_res

    @pytest.mark.valid_input
    def test_marks_args(self, students):
        with pytest.raises(AssertionError):
            students.marks(5)

    @pytest.mark.valid_input
    def test_group_int(self, students):
        with pytest.raises(AssertionError):
            students.group([5])

    @pytest.mark.valid_input
    def test_automat_int(self, students):
        with pytest.raises(AssertionError):
            students.automat('9')