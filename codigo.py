import streamlit as st

# Título da página
st.title("Inversor de Frases")

# Caixa de texto para o usuário inserir uma frase
user_input = st.text_input("Escreva uma frase:")

# Função para inverter a frase
def inverter_frase(frase):
    return frase[::-1]

# Botão para executar a inversão
if st.button("Inverter frase"):
    if user_input:
        frase_invertida = inverter_frase(user_input)
        st.text_area("Frase invertida:", frase_invertida)
    else:
        st.warning("Por favor, insira uma frase antes de inverter.")