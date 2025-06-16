import streamlit as st
import pandas as pd

# Caminho fixo para o Excel
EXCEL_PATH = "CNAEvsCLASSE.xlsx"

# Carrega a base de dados
df = pd.read_excel(EXCEL_PATH)
df["CNAE"] = df["CNAE"].astype(str).str.zfill(7)

st.set_page_config(page_title="Consulta CNAE x Classe", layout="centered")
st.title("🔍 Consulta de Classe por Código CNAE")

codigo = st.text_input("Digite o código CNAE (7 dígitos):", max_chars=7)

if codigo:
    codigo = codigo.zfill(7)
    resultados = df[df["CNAE"] == codigo]
    if not resultados.empty:
        st.success(f"Classes encontradas para o CNAE {codigo}:")
        for classe in resultados["CNT_Classe__c"].unique():
            st.markdown(f"- **{classe}**")
    else:
        st.warning("Nenhuma classe encontrada para este código CNAE.")
