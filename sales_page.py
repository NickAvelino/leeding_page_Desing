import streamlit as st
import pandas as pd
import re
import base64

st.set_page_config(
    page_title="Cadastro",
    page_icon="📚"
)

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def gravar_dados(nome, email, empresa, rede_social):
    if not nome or not empresa or not rede_social or not email:
        st.error("Preencha todos os campos!", icon="🚨")
    elif not validar_email(email):
        st.error("E-mail inválido. Por favor, tente novamente.", icon="🚨")
    else:
        st.success("Cadastrado com sucesso!", icon="✅")

def adicionar_imagem_de_fundo(imagem_path, opacidade):
    with open(imagem_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_image});
            background-size: cover;
            opacity: {opacidade};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Adicione o caminho para a sua imagem de fundo e defina a opacidade desejada (0.0 a 1.0)
adicionar_imagem_de_fundo("@designmodernoempresas.png", 1.0)

st.title("Cadastro")
st.divider()

nome = st.text_input("Nome Completo", key="nome")
email = st.text_input("E-mail", key="email")
empresa = st.text_input("Nome da Empresa ou apelido", key="empresa")
rede_social = st.selectbox("Rede Social", ("Instagram", "Facebook", "LinkedIn", "Twitter", "Google", "Youtube", "Whatsapp", "Indicação de Amigos", "Outros"))
btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=(nome, email, empresa, rede_social))





