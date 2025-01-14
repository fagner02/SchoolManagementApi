from datetime import datetime
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
teacher3 = Teacher(
    name="Tom Doe",
    age=25,
    email="tom@gmail.com",
    qualification="BSc",
    entry_date="2024-05-05",
)
teacher4 = Teacher(
    name="Jerry Doe",
    age=40,
    email="jerry@hotmail.com",
    qualification="MSc",
    entry_date="2023-02-05",
)
teacher5 = Teacher(
    name="Alice Doe",
    age=29,
    email="alice@yahoo.com",
    qualification="PhD",
    entry_date="2022-01-01",
)
teacher6 = Teacher(
    name="Bob Doe",
    age=33,
    email="bob@yahoo.com",
    qualification="BSc",
    entry_date="2025-01-01",
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
student3 = Student(
    name="Charlie",
    age=18,
    semester="8st",
    entry_date="2023-04-01",
)
student4 = Student(
    name="David",
    age=19,
    semester="6st",
    entry_date="2024-03-01",
)
student5 = Student(
    name="Eve",
    age=20,
    semester="2st",
    entry_date="2023-08-11",
)
student6 = Student(
    name="Frank",
    age=21,
    semester="4st",
    entry_date="2020-03-12",
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
subject4 = Subject(
    name="History", syllabus="World History", code="HIST101", workload=4, prerequisite="None"
)
subject5 = Subject(
    name="Computer Science", syllabus="Python", code="CS101", workload=4, prerequisite="None"
)
subject6 = Subject(
    name="Biology", syllabus="Anatomy", code="BIO101", workload=4, prerequisite="None"
)

# class
class1 = Class(subject_id=1, teacher_id=1, student_limit=20, schedule="Monday 9-11")
class2 = Class(subject_id=2, teacher_id=2, student_limit=20, schedule="Tuesday 9-11")
class3 = Class(subject_id=3, teacher_id=1, student_limit=20, schedule="Wednesday 9-11")
class4 = Class(subject_id=4, teacher_id=4, student_limit=20, schedule="Thursday 9-11")
class5 = Class(subject_id=5, teacher_id=5, student_limit=20, schedule="Friday 9-11")
class6 = Class(subject_id=6, teacher_id=6, student_limit=20, schedule="Saturday 9-11")

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
assignment3 = Assignment(
    class_id=3,
    description="Assignment 3",
    due_date="2022-11-12",
    created_at="2022-11-12",
)
assignment4 = Assignment(
    class_id=4,
    description="Assignment 4",
    due_date="2023-09-05",
    created_at="2023-09-05",
)
assignment5 = Assignment(
    class_id=5,
    description="Assignment 5",
    due_date="2024-03-22",
    created_at="2024-03-22",
)
assignment6 = Assignment(
    class_id=6,
    description="Assignment 6",
    due_date="2025-01-14",
    created_at="2025-01-14",
)

# assignment submission
assignment_submission1 = AssignmentSubmission(
    student_id=1, assignment_id=1, submission_date=datetime.fromisoformat("2021-01-01"), comments="Good job!"
)
assignment_submission2 = AssignmentSubmission(
    student_id=2, assignment_id=2, submission_date=datetime.fromisoformat("2021-01-01"), comments="Good job!"
)
assignment_submission3 = AssignmentSubmission(
    student_id=1, assignment_id=3, submission_date=datetime.fromisoformat("2021-01-01"), comments="Good job!"
)
assignment_submission4 = AssignmentSubmission(
    student_id=2, assignment_id=4, submission_date=datetime.fromisoformat("2021-01-01"), comments="Good job!"
)
assignment_submission5 = AssignmentSubmission(
    student_id=1, assignment_id=5, submission_date=datetime.fromisoformat("2022-11-12"), comments="Good job!"
)
assignment_submission6 = AssignmentSubmission(
    student_id=2, assignment_id=6, submission_date=datetime.fromisoformat("2022-11-12"), comments="Good job!"
)

# assignment grade
assignment_grade1 = AssignmentGrade(submission_id=1, grade=100)
assignment_grade2 = AssignmentGrade(submission_id=2, grade=90)
assignment_grade3 = AssignmentGrade(submission_id=3, grade=80)
assignment_grade4 = AssignmentGrade(submission_id=4, grade=70)
assignment_grade5 = AssignmentGrade(submission_id=5, grade=60)
assignment_grade6 = AssignmentGrade(submission_id=6, grade=50)

# enrollment
enrollment1 = Enrollment(student_id=1, class_id=1)
enrollment2 = Enrollment(student_id=2, class_id=1)
enrollment3 = Enrollment(student_id=3, class_id=3)
enrollment4 = Enrollment(student_id=4, class_id=4)
enrollment5 = Enrollment(student_id=5, class_id=5)
enrollment6 = Enrollment(student_id=6, class_id=6)

# class grades
class_grades1 = ClassGrades(class_id=1, student_id=1, grade=100)
class_grades2 = ClassGrades(class_id=1, student_id=2, grade=90)
class_grades3 = ClassGrades(class_id=3, student_id=3, grade=80)
class_grades4 = ClassGrades(class_id=4, student_id=4, grade=70)
class_grades5 = ClassGrades(class_id=5, student_id=5, grade=60)
class_grades6 = ClassGrades(class_id=6, student_id=6, grade=50)

session = get_session()

session.add(student1)
session.add(student2)
session.add(student3)
session.add(student4)
session.add(student5)
session.add(student6)
session.commit()

session.add(teacher1)
session.add(teacher2)
session.add(teacher3)
session.add(teacher4)
session.add(teacher5)
session.add(teacher6)

session.add(subject1)
session.add(subject2)
session.add(subject3)
session.add(subject4)
session.add(subject5)
session.add(subject6)

session.add(class1)
session.add(class2)
session.add(class3)
session.add(class4)
session.add(class5)
session.add(class6)
session.commit()

session.add(assignment1)
session.add(assignment2)
session.add(assignment3)
session.add(assignment4)
session.add(assignment5)
session.add(assignment6)

session.add(assignment_submission1)
session.add(assignment_submission2)
session.add(assignment_submission3)
session.add(assignment_submission4)
session.add(assignment_submission5)
session.add(assignment_submission6)

session.add(assignment_grade1)
session.add(assignment_grade2)
session.add(assignment_grade3)
session.add(assignment_grade4)
session.add(assignment_grade5)
session.add(assignment_grade6)

session.add(enrollment1)
session.add(enrollment2)
session.add(enrollment3)
session.add(enrollment4)
session.add(enrollment5)
session.add(enrollment6)

session.add(class_grades1)
session.add(class_grades2)
session.add(class_grades3)
session.add(class_grades4)
session.add(class_grades5)
session.add(class_grades6)

session.commit()
