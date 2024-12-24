from typing import Optional
from sqlalchemy import Column, LargeBinary
from sqlmodel import SQLModel, Field, BLOB


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    semester: str
    entry_date: str


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


class Class(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    grade: str
    subject: str
    teacher: str
    student_limit: int
    schedule: str


class Assignment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    class_id: int
    description: str
    due_date: str
    created_at: str


class AssignmentSubmission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int
    assignment_id: str
    submission_date: str
    comments: str
    submission_file: Optional[bytes] = Field(sa_column=BLOB)


class AssignmentGrade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    submission_id: int
    grade: float


class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int
    class_id: int


class ClassGrades(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int
    class_id: int
    grade: float
