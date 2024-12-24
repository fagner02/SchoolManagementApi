from typing import Optional, List
from sqlalchemy import Column, LargeBinary
from sqlmodel import Relationship, SQLModel, Field, BLOB


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    semester: str
    entry_date: str
    assignment_submissions: List["AssignmentSubmission"] = Relationship(
        back_populates="student"
    )
    enrollments: List["Enrollment"] = Relationship(back_populates="student")


class Teacher(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
    qualification: str
    entry_date: str


class Subject(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    syllabus: str
    code: str
    workload: int
    prerequisite: str
    classes: List["Class"] = Relationship(back_populates="subject")


class Class(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    grade: str
    subject_id: int = Field(default=None, foreign_key="subject.id")
    teacher: str
    student_limit: int
    schedule: str
    subject: Optional[Subject] = Relationship(back_populates="classes")
    assignments: List["Assignment"] = Relationship(back_populates="class_")
    enrollments: List["Enrollment"] = Relationship(back_populates="class_")
    class_grades: List["ClassGrades"] = Relationship(back_populates="class_")


class Assignment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    class_id: int = Field(default=None, foreign_key="class.id")
    description: str
    due_date: str
    created_at: str
    class_: Optional[Class] = Relationship(back_populates="assignments")
    submissions: List["AssignmentSubmission"] = Relationship(
        back_populates="assignment"
    )


class AssignmentSubmission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="student.id")
    assignment_id: int = Field(default=None, foreign_key="assignment.id")
    submission_date: str
    comments: str
    submission_file: Optional[bytes] = Field(sa_column=Column(LargeBinary))
    grade: Optional["AssignmentGrade"] = Relationship(back_populates="submission")
    student: Optional[Student] = Relationship(back_populates="assignment_submissions")
    assignment: Optional[Assignment] = Relationship(back_populates="submissions")


class AssignmentGrade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    submission_id: int = Field(default=None, foreign_key="assignment_submission.id")
    grade: float
    submission: Optional[AssignmentSubmission] = Relationship(back_populates="grade")


class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="student.id")
    class_id: int = Field(default=None, foreign_key="class.id")
    student: Optional[Student] = Relationship(back_populates="enrollments")
    class_: Optional[Class] = Relationship(back_populates="enrollments")


class ClassGrades(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="student.id")
    class_id: int = Field(default=None, foreign_key="class.id")
    grade: float
    student: Optional[Student] = Relationship(back_populates="class_grades")
    class_: Optional[Class] = Relationship(back_populates="class_grades")
