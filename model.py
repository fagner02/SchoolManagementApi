from pydantic import BaseModel

# modelos para o Sistema de Gerenciamento Escolar


class Aluno(BaseModel):
    nome: str
    idade: int
    serie: str


class Professor(BaseModel):
    nome: str
    idade: int
    disciplina: str


class Disciplina(BaseModel):
    nome: str
    carga_horaria: int


class Turma(BaseModel):
    serie: str
    disciplina: str
    professor: str


class Nota(BaseModel):
    aluno: str
    disciplina: str
    nota: float


class Matricula(BaseModel):
    aluno: str
    turma: str


class Boletim(BaseModel):
    aluno: str
    serie: str
    disciplina: str
    nota: float


class AlunoNota(BaseModel):
    aluno: str
    nota: float
