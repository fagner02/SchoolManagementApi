from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    semester: str
    registration: int
    entry_date: str


class Teacher(BaseModel):
    name: str
    age: int
    email: str
    qualification: str
    entry_date: str


class Subject(BaseModel):
    name: str
    syllabus: str
    code: str
    workload: int
    prerequisite: str


class Class(BaseModel):
    grade: str
    subject: str
    teacher: str
    student_limit: int
    schedule: str


class Assignment(BaseModel):
    class_id: int
    description: str
    due_date: str
    created_at: str


class AssignmentSubmission(BaseModel):
    student_id: int
    assignment_id: str
    submission_date: str
    comments: str
    submission_file: bytearray


class AssignmentGrade(BaseModel):
    submission_id: int
    grade: float


class Enrollment(BaseModel):
    student_id: int
    class_id: int


class ClassGrades(BaseModel):
    student_id: int
    class_id: int
    grade: float
