import json
import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Response, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload, Query
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
engine = create_engine(os.getenv("DATABASE_URL"), echo=False)
SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    return Session(engine)

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Bem-vindo ao Sistema de Gerenciamento Escolar"}

# ---------------------------
# CRUD para Student
# ---------------------------

@app.get("/student")
def get_students(session: Session = Depends(get_session)):
    try:
        res = session.query(Student).all()
        return res
    except Exception as e:
        return {"error": str(e)}


@app.post("/student")
def create_student(student: Student, session: Session = Depends(get_session)):
    try:
        session.add(student)
        session.commit()
        return student
    except Exception as e:
        return {"error": str(e)}
    
@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student, session: Session = Depends(get_session)):
    try:
        existing_student = session.get(Student, student_id)
        if not existing_student:
            return {"error": "Estudante não encontrado"}
        for key, value in student.dict(exclude_unset=True).items():
            setattr(existing_student, key, value)
        session.add(existing_student)
        session.commit()
        return existing_student
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/student/{student_id}")
def delete_student(student_id: int, session: Session = Depends(get_session)):
    try:
        existing_student = session.get(Student, student_id)
        if not existing_student:
            return {"error": "Estudante não encontrado"}
        session.delete(existing_student)
        session.commit()
        return {"msg": "Estudante deletado com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# CRUD para Teacher
# ---------------------------

@app.get("/teacher")
def get_teachers(session: Session = Depends(get_session)):
    try:
        return session.query(Teacher).all()
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
    
@app.put("/teacher/{teacher_id}")
def update_teacher(teacher_id: int, teacher: Teacher, session: Session = Depends(get_session)):
    try:
        existing_teacher = session.get(Teacher, teacher_id)
        if not existing_teacher:
            return {"error": "Professor não encontrado"}
        for key, value in teacher.dict(exclude_unset=True).items():
            setattr(existing_teacher, key, value)
        session.add(existing_teacher)
        session.commit()
        return existing_teacher
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/teacher/{teacher_id}")
def delete_teacher(teacher_id: int, session: Session = Depends(get_session)):
    try:
        existing_teacher = session.get(Teacher, teacher_id)
        if not existing_teacher:
            return {"error": "Professor não encontrado"}
        session.delete(existing_teacher)
        session.commit()
        return {"msg": "Professor deletado com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# CRUD para Class
# ---------------------------

@app.get("/class")
def get_classes(session: Session = Depends(get_session)):
    try:
        return session.query(Class).all()
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
    
@app.put("/class/{class_id}")
def update_class(class_id: int, class_: Class, session: Session = Depends(get_session)):
    try:
        existing_class = session.get(Class, class_id)
        if not existing_class:
            return {"error": "Turma não encontrada"}
        for key, value in class_.dict(exclude_unset=True).items():
            setattr(existing_class, key, value)
        session.add(existing_class)
        session.commit()
        return existing_class
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/class/{class_id}")
def delete_class(class_id: int, session: Session = Depends(get_session)):
    try:
        existing_class = session.get(Class, class_id)
        if not existing_class:
            return {"error": "Turma não encontrada"}
        session.delete(existing_class)
        session.commit()
        return {"msg": "Turma deletada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}
    
# ---------------------------
# CRUD para Assignment
# ---------------------------

@app.get("/assignment")
def get_assignments(session: Session = Depends(get_session)):
    try:
        return session.query(Assignment).all()
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
    
@app.put("/assignment/{assignment_id}")
def update_assignment(assignment_id: int, assignment_: Assignment, session: Session = Depends(get_session)):
    try:
        existing_assignment = session.get(Assignment, assignment_id)
        if not existing_assignment:
            return {"error": "Atividade não encontrada"}
        for key, value in assignment_.dict(exclude_unset=True).items():
            setattr(existing_assignment, key, value)
        session.add(existing_assignment)
        session.commit()
        return existing_assignment
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/assignment/{assignment_id}")
def delete_assignment(assignment_id: int, session: Session = Depends(get_session)):
    try:
        existing_assignment = session.get(Assignment, assignment_id)
        if not existing_assignment:
            return {"error": "Atividade não encontrada"}
        session.delete(existing_assignment) 
        session.commit()
        return {"msg": "Atividade deletada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# CRUD para AssignmentSubmission
# ---------------------------

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
        
@app.get("/submission")
def get_assignment_submissions(session: Session = Depends(get_session)):
    try:
        return session.query(AssignmentSubmission).all()
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

@app.put("/submission/{submission_id}")
def update_assignment_submission(
    submission_id: int, assignment_submission: AssignmentSubmission, session: Session = Depends(get_session)
):
    try:
        existing_submission = session.get(AssignmentSubmission, submission_id)
        if not existing_submission:
            return {"error": "Submissão não encontrada"}
        for key, value in assignment_submission.dict(exclude_unset=True).items():
            setattr(existing_submission, key, value)
        session.add(existing_submission)
        session.commit()
        return existing_submission
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/submission/{submission_id}")
def delete_assignment_submission(submission_id: int, session: Session = Depends(get_session)):
    try:
        existing_submission = session.get(AssignmentSubmission, submission_id)
        if not existing_submission:
            return {"error": "Submissão não encontrada"}
        session.delete(existing_submission)
        session.commit()
        return {"msg": "Submissão deletada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# CRUD para AssignmentGrade
# ---------------------------

@app.get("/assignment_grade")
def get_assignment_grades(session: Session = Depends(get_session)):
    try:
        return session.query(AssignmentGrade).all()
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

app.put("/assignment_grade/{assignment_grade_id}")
def update_assignment_grade(
    assignment_grade_id: int, assignment_grade: AssignmentGrade, session: Session = Depends(get_session)
):
    try:
        existing_assignment_grade = session.get(AssignmentGrade, assignment_grade_id)
        if not existing_assignment_grade:
            return {"error": "Nota não encontrada"}
        for key, value in assignment_grade.dict(exclude_unset=True).items():
            setattr(existing_assignment_grade, key, value)
        session.add(existing_assignment_grade)
        session.commit()
        return existing_assignment_grade
    except Exception as e:
        return {"error": str(e)}

@app.delete("/assignment_grade/{assignment_grade_id}")
def delete_assignment_grade(assignment_grade_id: int, session: Session = Depends(get_session)):
    try:
        existing_assignment_grade = session.get(AssignmentGrade, assignment_grade_id)
        if not existing_assignment_grade:
            return {"error": "Nota não encontrada"}
        session.delete(existing_assignment_grade)
        session.commit()
        return {"msg": "Nota deletada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# CRUD para Enrollment
# ---------------------------

@app.get("/enrollment")
def get_enrollments(session: Session = Depends(get_session)):
    try:
        return session.query(Enrollment).all()
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

@app.put("/enrollment/{enrollment_id}")
def update_enrollment(enrollment_id: int, enrollment: Enrollment, session: Session = Depends(get_session)):
    try:  
        existing_enrollment = session.get(Enrollment, enrollment_id)
        if not existing_enrollment:
            return {"error": "Matrícula não encontrada"}
        for key, value in enrollment.dict(exclude_unset=True).items():
            setattr(existing_enrollment, key, value)
        session.add(existing_enrollment)
        session.commit()
        return existing_enrollment
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/enrollment/{enrollment_id}")
def delete_enrollment(enrollment_id: int, session: Session = Depends(get_session)):
    try:
        existing_enrollment = session.get(Enrollment, enrollment_id)
        if not existing_enrollment:
            return {"error": "Matrícula não encontrada"}
        session.delete(existing_enrollment)
        session.commit()
        return {"msg": "Matrícula deletada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}
    
# ---------------------------
# CRUD para ClassGrades
# ---------------------------

@app.get("/class_grades")
def get_class_grades(session: Session = Depends(get_session)):
    try:
        return session.query(ClassGrades).all()
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
    
@app.put("/class_grades/{class_grades_id}")
def update_class_grades(
    class_grades_id: int, class_grades: ClassGrades, session: Session = Depends(get_session)
):
    try:
        existing_class_grades = session.get(ClassGrades, class_grades_id)
        if not existing_class_grades:
            return {"error": "Notas da turma não encontrada"}
        for key, value in class_grades.dict(exclude_unset=True).items():
            setattr(existing_class_grades, key, value)
        session.add(existing_class_grades)
        session.commit()
        return existing_class_grades
    except Exception as e:
        return {"error": str(e)}

@app.delete("/class_grades/{class_grades_id}")
def delete_class_grades(class_grades_id: int, session: Session = Depends(get_session)):
    try:
        existing_class_grades = session.get(ClassGrades, class_grades_id)
        if not existing_class_grades:
            return {"error": "Notas da turma não encontrada"}
        session.delete(existing_class_grades)
        session.commit()
        return {"msg": "Notas da turma deletadas com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# CRUD para Subject
# ---------------------------

@app.get("/subject")
def get_subjects(session: Session = Depends(get_session)):
    try:
        return session.query(Subject).all()
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

@app.put("/subject/{subject_id}")
def update_subject(subject_id: int, subject: Subject, session: Session = Depends(get_session)):
    try:
        existing_subject = session.get(Subject, subject_id)
        if not existing_subject:
            return {"error": "Disciplina não encontrada"}
        for key, value in subject.dict(exclude_unset=True).items():
            setattr(existing_subject, key, value)
        session.add(existing_subject)
        session.commit()
        return existing_subject
    except Exception as e:
        return {"error": str(e)}

@app.delete("/subject/{subject_id}")
def delete_subject(subject_id: int, session: Session = Depends(get_session)):
    try:
        existing_subject = session.get(Subject, subject_id)
        if not existing_subject:
            return {"error": "Disciplina não encontrada"}
        session.delete(existing_subject)
        session.commit()
        return {"msg": "Disciplina deletada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/total_entities")
def get_total_entities(session: Session = Depends(get_session)):
    try:
        total_count = (
            session.query(Student).count()
            + session.query(Teacher).count()
            + session.query(Subject).count()
            + session.query(Class).count()
            + session.query(Assignment).count()
            + session.query(AssignmentSubmission).count()
            + session.query(AssignmentGrade).count()
            + session.query(Enrollment).count()
            + session.query(ClassGrades).count()
        )
        return {"total": total_count}
    except Exception as e:
        return {"error": str(e)}
    
def paginate(query: Query, page: int, limit: int):
    offset = (page - 1) * limit
    total = query.count()
    data = query.offset(offset).limit(limit).all()
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": data,
    }
    
@app.get("/register/{entity_name}")
def get_registers(
    entity_name: str, page: int = 1, limit: int = 10, session: Session = Depends(get_session)
):
    try:
        model_map = {
            "student": Student,
            "teacher": Teacher,
            "subject": Subject,
            "class": Class,
            "assignment": Assignment,
            "submission": AssignmentSubmission,
            "grade": AssignmentGrade,
            "enrollment": Enrollment,
            "class_grades": ClassGrades,
        }

        model = model_map.get(entity_name.lower())
        if model is None:
            return {"error": "Entidade não encontrada"}
        
        query = session.query(model)
        return paginate(query, page, limit)
    except Exception as e:
        return {"error": str(e)}