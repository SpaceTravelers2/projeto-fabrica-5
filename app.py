import streamlit as st
import buscar_cep as cep

st.title("Buscador de cep 🔎")

opcoes = ["Buscar CEP", "Descobrir CEP"]

st.sidebar.header("Menu de Opções")
st.sidebar.image("./bmw_correio.png")
escolha = st.sidebar.selectbox("Escolha uma opção:", opcoes)

if escolha == "Buscar CEP":
    st.image("./CR7_busca_cep.png")
    cep_usuario = st.text_input("Qual o cep?")
    if st.button("Buscar cep"):
        dados = cep.buscar_cep(cep_usuario)
        if dados:
            st.success("Cep encontrado com sucesso")
            st.json(dados)
            st.map({
                "latitude": [ float(dados["lat"]) ],
                "longitude": [ float(dados["lng"]) ]
            })
        else:
            st.error("Cep não encontrado. Verifique o número e tente novamente.")
elif escolha == "Descobrir cep":
    st.image("./CR7_busca_endereço.png", width=500)
    endereco = st.text_input("Digite o endereço completo (rua, número, cidade, estado):")
    if st.button("Descobrir cep"):
        resultado = cep.descobrir_cep(endereco)
        st.info("A busca do cep foi realizada. Veja o link abaixo:")
        st.markdown(f"[Resultado da busca no Google]({resultado})")