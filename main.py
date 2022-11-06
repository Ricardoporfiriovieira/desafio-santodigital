import pandas as pd
from peewee import *

from models.course import course
from models.prof import prof
from models.ra import ra
from models.registration import registration
from models.student import student

#FAZENDO A REQUISIÇÃO DOS DADOS DE CADA PROFESSOR DE FORMA INDIVIDUAL

#  raprof = int(input("Digite o RA do professor desejado: "))

#  newquery = ra.select().where( ra.prof_id == raprof ).count()
#  print(f"quantidade de alunos do Professor de RA {raprof} é: {newquery}")

###########################################################################

profs = prof.select()

for professor in profs:
        students = ra.select().where(ra.prof_id == professor.prof_id)
        registrations = []
        for student in students:
            registrationss = registration.select().where(registration.student_id == student.student_id)
            for reg in registrationss:
                registrations.append(reg.course_id)

        print(f"O professor {professor.prof_id} tem {students.count()} alunos, tem a capacidade de ensino de {professor.teachingability} e dá {len([*set(registrations)])} cursos")

#db.loc[] pegar primeira celula