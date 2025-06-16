import streamlit as st
import pandas as pd

# Caminho correto para o arquivo Excel
EXCEL_PATH = "CNAEvsCLASSE_app.xlsx"

# Carrega os dados
df = pd.read_excel(EXCEL_PATH)
df["CNAE"] = df["CNAE"].astype(str).str.zfill(7)

# Configura a página
st.set_page_config(page_title="Consulta CNAE", layout="centered")

# Título
st.markdown("""
    <h1 style='text-align: center; font-size: 2.2em; margin-bottom: 30px;'>🔍 Consulta CNAE x Classe</h1>
""", unsafe_allow_html=True)

# Campo de entrada
codigo = st.text_input("Código CNAE (7 dígitos):", max_chars=7)

# Resultado ao digitar
if codigo:
    codigo = codigo.zfill(7)
    resultados = df[df["CNAE"] == codigo]

    if not resultados.empty:
        st.success(f"Classes encontradas para o CNAE {codigo}:")
        descricoes = resultados["CNT_Classe"].unique()
        for descricao in descricoes:
            st.markdown(f"<p style='margin-bottom: 25px;'>• {descricao}</p>", unsafe_allow_html=True)
    else:
        st.warning("Nenhuma classe encontrada para este código CNAE.")
        st.markdown("<p style='color:gray;'>Verifique se digitou corretamente os 7 números. Exemplo válido: <code>1041400</code>.</p>", unsafe_allow_html=True)

# Rodapé ao final da página
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style='text-align: center; font-size: 0.85em; color: gray;'>
        Desenvolvido por <strong>Data & Intelligence | RCO</strong>
    </div>
""", unsafe_allow_html=True)
