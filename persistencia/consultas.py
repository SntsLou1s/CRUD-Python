from dataclasses import dataclass
import sqlite3 as sql

class DMAluno:
    def __init__(self, obj_aluno) -> None:
        self.database = sql.connect('persistencia/database.db')
        self.cursor = self.database.cursor()
        self.aluno = obj_aluno
    
    def cadastrar_aluno(self):
        sql_inclusao = f"INSERT INTO alunos VALUES ('{self.aluno.matricula}', '{self.aluno.nome}', '{self.aluno.idade}', '{self.aluno.genero}', '{self.aluno.email}', '{self.aluno.celular}', '{self.aluno.descricao}')"
        self.cursor.execute(sql_inclusao)
        self.database.commit()
        self.cursor.close()
        self.database.close()
