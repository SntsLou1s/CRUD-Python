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

    def buscar_aluno(self):
        sql_busca = f"SELECT * FROM alunos WHERE matricula ='{self.aluno.matricula}' or nome = '{self.aluno.nome}';"
        self.cursor.execute(sql_busca)
        dados = self.cursor.fetchall()[0]
        self.aluno.matricula = dados[0] 
        self.aluno.nome = dados[1]
        self.aluno.idade = dados[2]  
        self.aluno.genero = dados[3] 
        self.aluno.email = dados[4]
        self.aluno.celular = dados[5]
        self.aluno.descricao = dados[6]
        self.cursor.close()
        self.database.close()
        return self.aluno
