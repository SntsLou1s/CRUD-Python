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