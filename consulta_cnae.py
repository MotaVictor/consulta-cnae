import streamlit as st
import pandas as pd

# Caminho para o arquivo Excel
EXCEL_PATH = "CNAEvsCLASSE.xlsx"

# Carrega os dados
df = pd.read_excel(EXCEL_PATH)
df["CNAE"] = df["CNAE"].astype(str).str.zfill(7)

# Configura a página
st.set_page_config(page_title="Consulta CNAE", layout="centered")

# Título visualmente compacto
st.markdown("""
    <h1 style='text-align: center; font-size: 2.2em; margin-bottom: 10px;'>🔍 Consulta CNAE x Classe</h1>
    <p style='text-align: center; color: gray;'>Digite o código CNAE da empresa para visualizar as classes possíveis.</p>
""", unsafe_allow_html=True)

# Campo de entrada
codigo = st.text_input("Código CNAE (7 dígitos – apenas números):", max_chars=7)

# Resultado
if codigo:
    codigo = codigo.zfill(7)
    resultados = df[df["CNAE"] == codigo]

    if not resultados.empty:
        st.success(f"Classes encontradas para o CNAE {codigo}:")
        for _, row in resultados.iterrows():
            st.markdown(f"<div style='margin-left:10px;'>• <strong>{row['CNT_Classe__c']}</strong></div>", unsafe_allow_html=True)
    else:
        st.warning("Nenhuma classe encontrada para este código CNAE.")
        st.markdown("<p style='color:gray;'>Verifique se digitou corretamente os 7 números. Exemplo de formato válido: <code>1041400</code>.</p>", unsafe_allow_html=True)

# Rodapé fixo
st.markdown("""
    <hr style="margin-top:50px;">
    <div style='text-align: center; font-size: 0.85em; color: gray;'>
        Desenvolvido por <strong>Data & Intelligence | RCO</strong>
    </div>
""", unsafe_allow_html=True)
