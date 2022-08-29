import streamlit as st
from modelo.aluno import Aluno

def App():
    st.title('Sistema Acadêmico')
    menus = ['Cadastrar', 'Buscar']
    menu = st.sidebar.radio('Menu', menus)
    if menu == 'Cadastrar':
        menu_cadastro()

def menu_cadastro():
    st.subheader('Cadastrar Aluno')
    st.text('Formulário de cadastro dos alunos do Instituto Louis LXXIII')
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input('Nome', placeholder='Insira seu nome completo')
        email = st.text_input('Email', placeholder='seuemail@domínio')
        matricula = st.text_input('Matrícula', placeholder='Insira sua matrícula', max_chars=12)
    with col2:
        idade = st.number_input('Idade', min_value=10, max_value=100)
        celular = st.text_input('Celular', placeholder='+99 (99) 9999-9999')
        genero = st.selectbox('Gênero', ['Masculino', 'Feminino', 'Transgênero', 'Gênero neutro', 'Não-binário', 'Agênero', 'Pangênero', 'Genderqueer', 'Two-spirit', 'Terceiro gênero', 'Outro'])
        if genero == 'Outro':
            genero = st.text_input('Diga o gênero que se identifica')
    descricao = st.text_area('Descreva-se em um tweet', max_chars=280)
    if st.button('Cadastrar'):
        aluno = Aluno(nome, idade, genero, email, celular, matricula, descricao)
        dados = [nome, idade, email, celular, matricula, genero, descricao]
        for x in dados:
            print(x)

if __name__ == '__main__':
    App()