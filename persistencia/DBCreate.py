import sqlite3 as sql

database = sql.connect('database.db')
cursor = database.cursor()

string_sql = 'CREATE TABLE alunos ('\
    'matricula TEXT PRIMARY KEY,'\
    'nome TEXT,'\
    'idade INTEGER,'\
    'genero TEXT,'\
    'email TEXT,'\
    'celular TEXT,'\
    'descricao TEXT);'

print(string_sql)
cursor.execute(string_sql)
