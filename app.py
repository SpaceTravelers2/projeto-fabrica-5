import streamlit as st
import buscar_cep as sp

st.title("Buscador de cep 🔎")

opcoes = ["Buscar CEP", "Descobrir CEP"]

st.sidebar.header("Menu de Opções")
st.sidebar.image("./bmw_correio.png")
escolha = st.sidebar.selectbox("Escolha uma opção:", opcoes)

if escolha == "Buscar CEP":
    st.image("./CR7_busca_cep.png")
    st.text_input("Qual o cep?")
    if st.button("Buscar cep"):
        dados = cep.buscar_cep()
        if dados:
            st.success("Cep encontrado com sucesso")
            st.json(dados)
            st.map({
                "latitude": [ float(dados["lat"]) ],
                "longitude": [ float(dados["lng"]) ]
            })
        else:
            st.error("Cep não encontrado. Verifique o número e tente novamente.")
