# DESAFIO 2 ( REGRAS DE NEGÓCIO )
# AQUI USEI O FASTAPI PARA CRIAR A API E FIZ O ACESSO AO BANCO DE DADOS USANDO O PEWEE

from enum import Enum

from fastapi import FastAPI

from models.prof import prof
from models.ra import ra
from models.registration import registration
from models.course import course as cs
from models.student import student

app = FastAPI()


# ADICIONANDO FILTROS DE DE NOTA DO CURSO "ASCENDENTE == CRESCENTE" E "DESCENDENTE == DECRESCENTE"
class ModelName(str, Enum):
    dec = "descendente"
    cres = "ascendente"

# MOSTRANDO TODOS OS ESTUDANTES POR CURSO
@app.get("/students/{notas}")
async def root(notas: ModelName):
    courses = cs.select()
    yay = {}
    if notas is ModelName.cres:
        for course in courses:
            regs = registration.select().join(student).where(registration.course_id == course.courseId).order_by(registration.grade.asc())
            if len(regs) > 0:
                yay[str(course.courseId)] = []
                for reg in regs:
                    yay[str(course.courseId)].append(reg)

    if notas is ModelName.dec:
        for course in courses:
            regs = registration.select().join(student).where(registration.course_id == course.courseId).order_by(registration.grade.desc())
            if len(regs) > 0:
                yay[str(course.courseId)] = []
                for reg in regs:
                    yay[str(course.courseId)].append(reg)
    return yay


# MOSTRANDO O RELATORIO DOS TOP 5 ESTUDANTE DA ESCOLA
@app.get("/relatorio/aluno")
async def top5estudante():
        registrations = registration.select().join(student).limit(5).order_by(student.ranking.desc())

        return {registrations[i] for i in range(len(registrations))}

# MOSTRANDO OS MELHORES PROFESSORES POR POPULARIDADE
@app.get("/relatorio/professor")
async def topprofessores():
        profs = prof.select().limit().order_by(prof.popularity.desc())

        return {profs[i] for i in range(len(profs))}


# MOSTRANDO A QUANTIDADE DE ALUNOS POR CURSO
@app.get("/relatorio/curso")
async def quantalunos():
    courses = cs.select()

    cursos = {}
    for course in courses:
        regs_count = registration.select().where(registration.course_id == course.courseId).count()
        if regs_count > 0:
            cursos[str(course.courseId)] = {"quant": regs_count}
    return cursos
