import streamlit as st
import pandas as pd

# Caminho para o arquivo Excel
EXCEL_PATH = "CNAEvsCLASSE.xlsx"

# Carrega os dados
df = pd.read_excel(EXCEL_PATH)
df["CNAE"] = df["CNAE"].astype(str).str.zfill(7)

# Configura a página
st.set_page_config(page_title="Consulta CNAE", layout="centered")

# Título
st.markdown("""
    <h1 style='text-align: center; font-size: 2.2em; margin-bottom: 30px;'>🔍 Consulta CNAE x Classe</h1>
""", unsafe_allow_html=True)

# Campo com botão de lupa sutil
with st.form(key="form_cnae"):
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input {
            font-size: 1rem;
        }
        .lupa-button button {
            background-color: transparent;
            border: none;
            font-size: 1.3em;
            margin-top: 1.7em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([6, 1])
    with col1:
        codigo = st.text_input("Código CNAE (7 dígitos – apenas números):", max_chars=7)
    with col2:
        with st.container():
            submit = st.form_submit_button(label="🔍", help="Pesquisar")

# Resultado
if submit and codigo:
    codigo = codigo.zfill(7)
    resultados = df[df["CNAE"] == codigo]

    if not resultados.empty:
        st.success(f"Classes encontradas para o CNAE {codigo}:")
        for _, row in resultados.iterrows():
            st.markdown(f"""
                <div style='margin: 0px 10px 20px 10px; padding: 10px; background-color: #181c25; border-radius: 5px;'>
                    {row['CNT_Classe__c']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Nenhuma classe encontrada para este código CNAE.")
        st.markdown("<p style='color:gray;'>Verifique se digitou corretamente os 7 números. Exemplo válido: <code>1041400</code>.</p>", unsafe_allow_html=True)

# Rodapé final
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style='text-align: center; font-size: 0.85em; color: gray;'>
        Desenvolvido por <strong>Data & Intelligence | RCO</strong>
    </div>
""", unsafe_allow_html=True)
