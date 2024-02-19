from main import StudentsInMLOps

def test_enrollStudents():
    s = StudentsInMLOps()
    s.enrollStudents(5)
    assert s.getTotalStrength() == 5

def test_dropStudents():
    s = StudentsInMLOps()
    s.enrollStudents(5)
    s.dropStudents(2)
    assert s.getTotalStrength() == 3

def test_getTotalStrength():
    s = StudentsInMLOps()
    assert s.getTotalStrength() == 0

def test_getClassName():
    s = StudentsInMLOps()
    assert s.getClassName() == "StudentsInMLOps"
