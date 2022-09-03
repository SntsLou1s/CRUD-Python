# CRUD - Sistema Acadêmico

Um projeto que, inicialmente, usará os módulos StreamLit e SQLite para ser desenvolvido.

O intuito do projeto é desenvolvimento pessoal, prática da linguagem e aprimoramento de banco de dados.

## Persistência
Dentro deste diretório estão inclusos os arquivos relacionados a persistência de dados. 

Para utilizar o programa, é necessário executar o arquivo **DBCreate.py** uma vez para criar a base de dados local, chamada database.db.

Apósc criar, mova o arquivo **database.db** para o diretório persistencia.

## Como executar
Com a biblioteca streamlit instalada, rode o comando *"streamlit run App.py"* no terminal. Isso abrirá um página no seu navegador padrão, rodando uma página web no seu localhost, que também pode ser acessada por outros dispositivos na rede, através do endereço IP.

Na página, preencha os campos, pressione cadastrar e caso esteja tudo certo, as informações serão armazenadas no arquivo database.db

## Dependências
- sqlite
- streamlit