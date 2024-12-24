import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlmodel import SQLModel
from model import (
    Student,
    Teacher,
    Subject,
    Class,
    Assignment,
    AssignmentSubmission,
    AssignmentGrade,
    Enrollment,
    ClassGrades,
)


load_dotenv("config.env")
engine = create_engine(os.getenv("DATABASE_URL"))
SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)


# generate instances of all models to populate the database
# teacher
teacher1 = Teacher(
    name="John Doe",
    age=30,
    email="john@gmail.com",
    qualification="MSc",
    entry_date="2021-01-01",
)
teacher2 = Teacher(
    name="Jane Doe",
    age=35,
    email="jon@gmail.com",
    qualification="PhD",
    entry_date="2021-01-01",
)

# student
student1 = Student(
    name="Alice",
    age=20,
    semester="1st",
    entry_date="2021-01-01",
)
student2 = Student(
    name="Bob",
    age=20,
    semester="1st",
    entry_date="2021-01-01",
)

# subject
subject1 = Subject(
    name="Math", syllabus="Algebra", code="MATH101", workload=4, prerequisite="None"
)
subject2 = Subject(
    name="Science", syllabus="Physics", code="SCI101", workload=4, prerequisite="None"
)
subject3 = Subject(
    name="English", syllabus="Grammar", code="ENG101", workload=4, prerequisite="None"
)

# class
class1 = Class(subject_id=1, teacher_id=1, student_limit=20, schedule="Monday 9-11")
class2 = Class(subject_id=2, teacher_id=2, student_limit=20, schedule="Tuesday 9-11")
class3 = Class(subject_id=3, teacher_id=1, student_limit=20, schedule="Wednesday 9-11")

# assignment
assignment1 = Assignment(
    class_id=1,
    description="Assignment 1",
    due_date="2021-01-01",
    created_at="2021-01-01",
)
assignment2 = Assignment(
    class_id=2,
    description="Assignment 2",
    due_date="2021-01-01",
    created_at="2021-01-01",
)

# assignment submission
assignment_submission1 = AssignmentSubmission(
    student_id=1, assignment_id=1, submission_date="2021-01-01"
)

# assignment grade
assignment_grade1 = AssignmentGrade(submission_id=1, grade=100)

# enrollment
enrollment1 = Enrollment(student_id=1, class_id=1)
enrollment2 = Enrollment(student_id=2, class_id=1)

# class grades
class_grades1 = ClassGrades(class_id=1, student_id=1, grade=100)
class_grades2 = ClassGrades(class_id=1, student_id=2, grade=90)

session = get_session()

session.add(student1)
session.add(student2)
session.commit()

session.add(teacher1)
session.add(teacher2)

session.add(subject1)
session.add(subject2)
session.add(subject3)

session.add(class1)
session.add(class2)
session.add(class3)
session.commit()

session.add(assignment1)
session.add(assignment2)

session.add(assignment_submission1)

session.add(assignment_grade1)

session.add(enrollment1)
session.add(enrollment2)

session.add(class_grades1)
session.add(class_grades2)

session.commit()
