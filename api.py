import json
import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload
from sqlmodel import SQLModel
from model import (
    Student,
    StudentPublic,
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
engine = create_engine(os.getenv("DATABASE_URL"), echo=False)
SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)


app = FastAPI()


@app.get("/student", response_model=StudentPublic)
def get_students(session: Session = Depends(get_session)):
    try:
        res = session.query(Student).first()
        return res
    except Exception as e:
        return {"error": str(e)}


@app.get("/teacher")
def get_teachers(session: Session = Depends(get_session)):
    try:
        return session.query(Teacher).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/subject")
def get_subjects(session: Session = Depends(get_session)):
    try:
        return session.query(Subject).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/class")
def get_classes(session: Session = Depends(get_session)):
    try:
        return session.query(Class).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/assignment")
def get_assignments(session: Session = Depends(get_session)):
    try:
        return session.query(Assignment).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/submission")
def get_assignment_submissions(session: Session = Depends(get_session)):
    try:
        return session.query(AssignmentSubmission).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/assignment_grade")
def get_assignment_grades(session: Session = Depends(get_session)):
    try:
        return session.query(AssignmentGrade).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/enrollment")
def get_enrollments(session: Session = Depends(get_session)):
    try:
        return session.query(Enrollment).all()
    except Exception as e:
        return {"error": str(e)}


@app.get("/class_grades")
def get_class_grades(session: Session = Depends(get_session)):
    try:
        return session.query(ClassGrades).all()
    except Exception as e:
        return {"error": str(e)}


@app.post("/teacher")
def create_teacher(teacher: Teacher, session: Session = Depends(get_session)):
    try:
        session.add(teacher)
        session.commit()
        return teacher
    except Exception as e:
        return {"error": str(e)}


@app.post("/subject")
def create_subject(subject: Subject, session: Session = Depends(get_session)):
    try:
        session.add(subject)
        session.commit()
        return subject
    except Exception as e:
        return {"error": str(e)}


@app.post("/class")
def create_class(class_: Class, session: Session = Depends(get_session)):
    try:
        session.add(class_)
        session.commit()
        return class_
    except Exception as e:
        return {"error": str(e)}


@app.post("/assignment")
def create_assignment(assignment: Assignment, session: Session = Depends(get_session)):
    try:
        session.add(assignment)
        session.commit()
        return assignment
    except Exception as e:
        return {"error": str(e)}


@app.post("/submission")
def create_assignment_submission(
    assignment_submission: AssignmentSubmission, session: Session = Depends(get_session)
):
    try:
        assignment_submission.submission_file = (
            assignment_submission.submission_file.encode("latin1")
        )
        session.add(assignment_submission)
        session.commit()
        return assignment_submission
    except Exception as e:
        return {"error": str(e)}


@app.post("/assignment_grade")
def create_assignment_grade(
    assignment_grade: AssignmentGrade, session: Session = Depends(get_session)
):
    try:
        session.add(assignment_grade)
        session.commit()
        return assignment_grade
    except Exception as e:
        return {"error": str(e)}


@app.post("/enrollment")
def create_enrollment(enrollment: Enrollment, session: Session = Depends(get_session)):
    try:
        session.add(enrollment)
        session.commit()
        return enrollment
    except Exception as e:
        return {"error": str(e)}


@app.post("/class_grades")
def create_class_grades(
    class_grades: ClassGrades, session: Session = Depends(get_session)
):
    try:
        session.add(class_grades)
        session.commit()
        return class_grades
    except Exception as e:
        return {"error": str(e)}


@app.get(
    "/submission/file",
    responses={200: {"content": {"text/txt": {}}}},
    response_class=Response,
)
def get_submission_file(submission_id: int, session: Session = Depends(get_session)):
    try:
        submission = session.get(AssignmentSubmission, submission_id)
        return Response(submission.submission_file, media_type="text/txt")
    except Exception as e:
        return {"error": str(e)}
