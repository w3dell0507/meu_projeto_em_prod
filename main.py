
import streamlit as st
import pandas as pd


# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Calculadora e Análise",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# CARREGAR CSV
# =========================================================

dados = pd.read_csv("vendas.csv")


# =========================================================
# MEMÓRIA DOS BOTÕES
# =========================================================

if "analise_aberta" not in st.session_state:
    st.session_state.analise_aberta = False

if "mapa_aberto" not in st.session_state:
    st.session_state.mapa_aberto = False


# =========================================================
# TÍTULO
# =========================================================

st.title("📊 Calculadora e Análise de Vendas")

st.write(
    "Use a calculadora e visualize os dados de vendas."
)

st.markdown("---")


# =========================================================
# CALCULADORA
# =========================================================

st.header("🧮 Calculadora")

col1, col2 = st.columns(2)

with col1:
    n1 = st.number_input(
        "Digite o primeiro número:",
        value=0.0
    )

with col2:
    n2 = st.number_input(
        "Digite o segundo número:",
        value=0.0
    )


# =========================================================
# OPERAÇÕES
# =========================================================

col_soma, col_sub, col_mult, col_div = st.columns(4)

with col_soma:
    if st.button("➕ Somar", use_container_width=True):
        st.success(f"Resultado: {n1 + n2:.2f}")

with col_sub:
    if st.button("➖ Subtrair", use_container_width=True):
        st.success(f"Resultado: {n1 - n2:.2f}")

with col_mult:
    if st.button("✖️ Multiplicar", use_container_width=True):
        st.success(f"Resultado: {n1 * n2:.2f}")

with col_div:
    if st.button("➗ Dividir", use_container_width=True):

        if n2 == 0:
            st.error("❌ Não é possível dividir por zero.")
        else:
            st.success(f"Resultado: {n1 / n2:.2f}")


st.markdown("---")


# =========================================================
# ANÁLISE DE DADOS
# =========================================================

st.header("📈 Análise de dados")

# Botão abrir/fechar
if st.button(
    "📕 Fechar análise de dados"
    if st.session_state.analise_aberta
    else "📖 Abrir análise de dados",
    use_container_width=True
):

    st.session_state.analise_aberta = (
        not st.session_state.analise_aberta
    )


# =========================================================
# CONTEÚDO DA ANÁLISE
# =========================================================

if st.session_state.analise_aberta:

    st.subheader("📋 Dados de vendas")

    st.dataframe(
        dados,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # GRÁFICO DE LUCRO
    st.subheader("💰 Lucro por ano")

    st.bar_chart(
        dados,
        x="ano",
        y="lucro",
        use_container_width=True
    )

    st.markdown("---")

    # GRÁFICO DE VENDAS
    st.subheader("📊 Vendas por ano")

    st.line_chart(
        dados,
        x="ano",
        y="venda",
        use_container_width=True
    )


# =========================================================
# MAPA
# =========================================================

st.markdown("---")

st.header("🗺️ Mapa")

if st.button(
    "📕 Fechar mapa"
    if st.session_state.mapa_aberto
    else "🗺️ Abrir mapa",
    use_container_width=True
):

    st.session_state.mapa_aberto = (
        not st.session_state.mapa_aberto
    )


# =========================================================
# MAPA INDEPENDENTE DO CSV
# =========================================================

if st.session_state.mapa_aberto:

    st.subheader("📍 Localização")

    # Pontos de exemplo
    mapa = pd.DataFrame(
        {
            "lat": [-23.5505, -22.9068, -15.7939],
            "lon": [-46.6333, -43.1729, -47.8828]
        }
    )

    st.map(mapa)


# =========================================================
# RODAPÉ
# =========================================================

st.markdown("---")

st.caption(
    "📚 Projeto desenvolvido com Python, Pandas e Streamlit."
)