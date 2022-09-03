from persistencia.consultas import DMAluno

class Aluno:
    def __init__(self, matricula, nome, idade, genero, email, celular, descricao):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.email = email
        self.celular = celular
        self.descricao = descricao
        self.dmodule = DMAluno(self)

    def cadastrar(self):
        self.dmodule.cadastrar_aluno()

    def buscar(self):
        new_aluno = self.dmodule.buscar_aluno()
        self.matricula = new_aluno.matricula
        self.nome = new_aluno.nome
        self.idade = new_aluno.idade
        self.genero = new_aluno.genero
        self.email = new_aluno.email
        self.celular = new_aluno.celular
        self.descricao = new_aluno.descricao