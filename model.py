from functools import partial
import re
from typing import Optional, List
from datetime import datetime
from sqlalchemy import Column, DateTime, LargeBinary
from sqlalchemy.orm import declared_attr, Mapped
from sqlmodel import Relationship, SQLModel as _SQLModel, Field

_snake_1 = partial(re.compile(r"(.)((?<![^A-Za-z])[A-Z][a-z]+)").sub, r"\1_\2")


def snake_case(string: str) -> str:
    return _snake_1(string).lower()


class SQLModel(_SQLModel):
    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)


class Enrollment(SQLModel, table=True):
    student_id: int = Field(default=None, foreign_key="student.id", primary_key=True)
    class_id: int = Field(default=None, foreign_key="class.id", primary_key=True)


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    semester: str
    entry_date: str
    assignment_submissions: List["AssignmentSubmission"] = Relationship(
        back_populates="student"
    )
    classes: List["Class"] = Relationship(
        back_populates="students", link_model=Enrollment
    )
    class_grades: List["ClassGrades"] = Relationship(back_populates="student")


class Teacher(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
    qualification: str
    entry_date: str
    classes: List["Class"] = Relationship(back_populates="teacher")


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
    subject_id: int = Field(default=None, foreign_key="subject.id")
    teacher_id: int = Field(default=None, foreign_key="teacher.id")
    student_limit: int
    schedule: str
    subject: Optional[Subject] = Relationship(back_populates="classes")
    assignments: List["Assignment"] = Relationship(back_populates="class_")
    students: List["Student"] = Relationship(
        back_populates="classes", link_model=Enrollment
    )
    class_grades: Mapped[List["ClassGrades"]] = Relationship(back_populates="class_")
    teacher: Optional[Teacher] = Relationship(back_populates="classes")


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


class AssignmentSubmission(
    SQLModel, table=True, custom_table_name="assignment_submission"
):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="student.id")
    assignment_id: int = Field(default=None, foreign_key="assignment.id")
    submission_date: datetime 
    comments: Optional[str]
    submission_file: Optional[bytes] = Field(sa_column=Column(LargeBinary))
    grade: Optional["AssignmentGrade"] = Relationship(back_populates="submission")
    student: Optional[Student] = Relationship(back_populates="assignment_submissions")
    assignment: Optional[Assignment] = Relationship(back_populates="submissions")


class AssignmentGrade(SQLModel, table=True, custom_table_name="assignment_grade"):
    id: Optional[int] = Field(default=None, primary_key=True)
    submission_id: int = Field(default=None, foreign_key="assignment_submission.id")
    grade: float
    submission: Optional[AssignmentSubmission] = Relationship(back_populates="grade")


class ClassGrades(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="student.id")
    class_id: int = Field(default=None, foreign_key="class.id")
    grade: float
    student: Optional[Student] = Relationship(back_populates="class_grades")
    class_: Optional[Class] = Relationship(back_populates="class_grades")


class SubjectPublic(SQLModel):
    id: Optional[int]
    name: str
    syllabus: str
    code: str
    workload: int
    prerequisite: str


class ClassPublic(SQLModel):
    id: Optional[int]
    subject: "Subject"
    teacher_id: int
    student_limit: int
    schedule: str


class StudentPublic(SQLModel):
    id: Optional[int]
    name: str
    age: int
    semester: str
    classes: list["ClassPublic"] = []
