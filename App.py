import streamlit as st
from modelo.aluno import Aluno

def App():
    st.title('Sistema Acadêmico')
    menus = ['Cadastrar', 'Buscar']
    menu = st.sidebar.radio('Menu', menus)
    if menu == 'Cadastrar':
        menu_cadastro()
    elif menu == 'Buscar':
        menu_busca()

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
        genero = st.selectbox('Gênero', ['Masculino', 'Feminino', 'Não-binário', 'Outro'])
        if genero == 'Outro':
            genero = st.text_input('Diga o gênero que se identifica')
    descricao = st.text_area('Descreva-se em um tweet', max_chars=280)
    if st.button('Cadastrar'):
        aluno = Aluno(matricula, nome, idade, genero, email, celular, descricao)
        aluno.cadastrar()
        dados = [nome, idade, email, celular, matricula, genero, descricao]
        for x in dados:
            print(x)

def menu_busca():
    st.subheader('Buscar Aluno')
    col1, col2 = st.columns(2)
    with col1:
        tipo_dado = st.selectbox('Buscar por:', ['Matrícula', 'Nome'])
        if tipo_dado == 'Matrícula':
            with col2:
                dado = st.text_input('Insira a matrícula', max_chars=12)
        elif tipo_dado == 'Nome':
            with col2:
                dado = st.text_input('Insira o nome completo')
    if st.button('Buscar'):
        try:
            if tipo_dado == 'Matrícula':
                aluno = Aluno(dado, '', 0, '', '', '', '')
                aluno.buscar()
            elif tipo_dado == 'Nome':
                aluno = Aluno('', dado, 0, '', '', '', '')
                aluno.buscar()
            st.subheader('Ficha - Aluno')
            col3, col4 = st.columns(2)
            with col3:
                st.markdown(f'**Matrícula:** *{aluno.matricula}*')
                st.markdown(f'**Nome:** *{aluno.nome}*')
                st.markdown(f'**Idade:** *{aluno.idade}*')
            with col4:
                st.markdown(f'**Gênero:** *{aluno.genero}*')
                st.markdown(f'**Celular:** *{aluno.celular}*')
                st.markdown(f'**Email:** *{aluno.email}*')
            st.markdown(f'**Descrição:** *{aluno.descricao}*')
        except:
            st.subheader('Aluno não encontrado')

if __name__ == '__main__':
    App()