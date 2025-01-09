import os
from datetime import datetime
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy import Extract, create_engine
from sqlalchemy.orm import Session
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

student_router = CRUDRouter(schema=Student, db_model=Student, db=get_session)
teaher_router = CRUDRouter(schema=Teacher, db_model=Teacher, db=get_session)
subject_router = CRUDRouter(schema=Subject, db_model=Subject, db=get_session)
class_router = CRUDRouter(schema=Class, db_model=Class, db=get_session)
assignment_router = CRUDRouter(schema=Assignment, db_model=Assignment, db=get_session)
assignment_submission_router = CRUDRouter(schema=AssignmentSubmission, db_model=AssignmentSubmission, db=get_session)
assignment_grade_router = CRUDRouter(schema=AssignmentGrade, db_model=AssignmentGrade, db=get_session)
enrollment_router = CRUDRouter(schema=Enrollment, db_model=Enrollment, db=get_session)
class_grades_router = CRUDRouter(schema=ClassGrades, db_model=ClassGrades, db=get_session)

app.include_router(student_router)
app.include_router(teaher_router)
app.include_router(subject_router)
app.include_router(class_router)
app.include_router(assignment_router)
app.include_router(assignment_submission_router)
app.include_router(assignment_grade_router)
app.include_router(enrollment_router)
app.include_router(class_grades_router)


@app.get("/student_qtd", tags=["Student"])
def get_student_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Student).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/teacher_qtd", tags=["Teacher"])
def get_teacher_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Teacher).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/subject_qtd", tags=["Subject"])
def get_subject_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Subject).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/class_qtd", tags=["Class"])
def get_class_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Class).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/assignment_qtd", tags=["Assignment"])
def get_assignment_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Assignment).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("submission_qtd", tags=["Assignment_submission"])
def get_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Student).count()
        return  {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/grade_qtd", tags=["Assignment_grade"])
def get_grade_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(AssignmentGrade).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/enrollment_qtd", tags=["Enrollment"])
def get_enrollment_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(Enrollment).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}

@app.get("/class_grades_qtd", tags=["Class_grades"])
def get_class_grades_qtd(session: Session = Depends(get_session)):
    try:
        qtd = session.query(ClassGrades).count()
        return {"quantidade": qtd}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/student_page",tags=["Student"])
def get_student_page(page: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        students = session.query(Student).limit(limit).offset(page*limit).all()
        return students
    except Exception as e:
        return {"error": str(e)}

@app.get("/teacher_page", tags=["Teacher"])
def get_teacher_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        teachers = session.query(Teacher).limit(limit).offset(page*limit).all()
        return teachers
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/subject_page", tags=["Subject"])    
def get_subject_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        subjects = session.query(Subject).limit(limit).offset(page*limit).all()
        return subjects
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/class_page", tags=["Class"])
def get_class_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        classes = session.query(Class).limit(limit).offset(page*limit).all()
        return classes
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/assignment_page", tags=["Assignment"])
def get_assignment_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        assignments = session.query(Assignment).limit(limit).offset(page*limit).all()
        return assignments
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/submission_page", tags=["Assignment_submission"])
def get_submission_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        submissions = session.query(AssignmentSubmission).limit(limit).offset(page*limit).all()
        return submissions
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/grade_page", tags=["Assignment_grade"])
def get_grade_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        grades = session.query(AssignmentGrade).limit(limit).offset(page*limit).all()
        return grades
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/enrollment_page", tags=["Enrollment"])
def get_enrollment_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        enrollments = session.query(Enrollment).limit(limit).offset(page*limit).all()
        return enrollments
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/class_grades_page", tags=["Class_grades"])
def get_class_grades_page(page: int=0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        class_grades = session.query(ClassGrades).limit(limit).offset(page*limit).all()
        return class_grades
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/student/{student_id}/classes", tags=["Student"])
def get_classes_by_student(student_id: int, session: Session = Depends(get_session)):
    try:
        classes = session.query(Class).join(Enrollment).where(Enrollment.student_id == student_id).all()
        return classes
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/student/{student_id}/assignments", tags=["Student"])
def get_assignments_by_student(student_id: int, session: Session = Depends(get_session)):
    try:
        assignments = session.query(Assignment).join(Enrollment).where(Enrollment.student_id == student_id).all()
        return assignments
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/student_search", tags=["Student"])
def get_student_search(q: str, session: Session = Depends(get_session)):
    try:
        students = session.query(Student).where(Student.name.like(f"%{q}%")).all()
        return students
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/submission_year", tags=["Assignment_submission"])
def get_submission_year(year: int, session: Session = Depends(get_session)):
    try:
        submissions = session.query(AssignmentSubmission).filter(Extract("year",AssignmentSubmission.submission_date) == year).all()
        return submissions
    except Exception as e:
        return {"error": str(e)}

@app.get("/student/{student_id}/workload", tags=["Student"])
def get_workload_by_student(student_id: int, session: Session = Depends(get_session)):
    try:
        classes = session.query(Class).join(Enrollment).where(Enrollment.student_id == student_id).all()
        workload = sum([c.subject.workload for c in classes])
        return {"Carga Horária": f"{workload}H"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/students_sorted", tags=["Student"])
def get_students_sorted(session: Session = Depends(get_session)):
    try:
        students = session.query(Student).order_by(Student.name).all()
        return students
    except Exception as e:
        return {"error": str(e)}

@app.get("/students_sorted_desc", tags=["Student"])
def get_students_sorted_desc(session: Session = Depends(get_session)):
    try:
        students = session.query(Student).order_by(Student.name.desc()).all()
        return students
    except Exception as e:
        return {"error": str(e)}

@app.get("/students_with_classes", tags=["Student"], response_model=list[StudentPublic])
def get_students_with_classes(session: Session = Depends(get_session)):
    try:
        students = session.query(Student).join(Enrollment).join(Class).all()
        return students
    except Exception as e:
        return {"error": str(e)}
