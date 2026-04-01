import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Painel de Diagnóstico Organizacional",
    page_icon="🏢",
    layout="wide"
)

# -----------------------------------
# CSS (CORRIGIDO + PROFISSIONAL)
# -----------------------------------
st.markdown("""
<style>

.titulo {
    font-size: 2.3rem;
    font-weight: 700;
    color: #3A7CA5;
}

.subtitulo {
    font-size: 1rem;
    color: #cfd8dc;
    margin-bottom: 20px;
}

/* CORRIGE O RESUMO EXECUTIVO */
.card {
    background: linear-gradient(135deg, #1f3b5c, #2c4a6e);
    color: white !important;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}

/* CARDS DE KPI */
.kpi {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

/* SWOTS */
.swot {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# MENU
# -----------------------------------
menu = st.sidebar.radio("Navegação", [
    "Início",
    "SWOT",
    "Matriz GUT",
    "Diagnóstico",
    "Plano de Intervenção",
    "Indicadores"
])

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown('<div class="titulo">Painel de Diagnóstico Organizacional</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Alfa Embalagem Ltda. | Apoio à tomada de decisão</div>', unsafe_allow_html=True)

# -----------------------------------
# INÍCIO
# -----------------------------------
if menu == "Início":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Tempo de mercado", "13 anos")
    col2.metric("Funcionários", "43")
    col3.metric("Porte", "Média")
    col4.metric("Setores", "5")

    st.markdown("### 📊 Resumo Executivo")

    st.markdown("""
    <div class="card">
    A Alfa Embalagem Ltda. apresenta forte atuação no mercado regional, com destaque para qualidade dos produtos,
    capacidade produtiva e agilidade na entrega.

    Entretanto, o diagnóstico identificou fragilidades na gestão organizacional, principalmente relacionadas à
    ausência de um Sistema de Gestão da Qualidade (SGQ), baixa integração entre setores e dependência de processos manuais.

    A Matriz GUT apontou a ausência de SGQ como o problema mais crítico, impactando diretamente a padronização,
    eficiência operacional e tomada de decisão da empresa.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# SWOT
# -----------------------------------
elif menu == "SWOT":

    st.subheader("📊 Análise SWOT")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🟢 Forças")
        st.markdown("""
        - Qualidade dos produtos  
        - Produção em escala  
        - Agilidade na entrega  
        - Boa relação com fornecedor  
        - Estrutura organizacional definida  
        """)

        st.markdown("#### 🟡 Oportunidades")
        st.markdown("""
        - Expansão no Nordeste  
        - Investimento em tecnologia  
        - Fortalecimento digital  
        - Novas parcerias  
        """)

    with col2:
        st.markdown("#### 🔴 Fraquezas")
        st.markdown("""
        - Decisões centralizadas  
        - Processos manuais  
        - Falta de padronização  
        - Baixa integração entre setores  
        """)

        st.markdown("#### ⚫ Ameaças")
        st.markdown("""
        - Concorrência local  
        - Pressão por preços  
        - Dependência de fornecedor  
        - Instabilidade econômica  
        """)

# -----------------------------------
# MATRIZ GUT
# -----------------------------------
elif menu == "Matriz GUT":

    st.subheader("📌 Priorização de Problemas")

    dados = pd.DataFrame({
        "Problema": [
            "Ausência de SGQ",
            "Falta de integração dos dados",
            "Dependência do Excel",
            "Falta de padronização"
        ],
        "G": [5,4,3,4],
        "U": [5,4,4,3],
        "T": [4,5,4,4]
    })

    dados["Total"] = dados["G"] * dados["U"] * dados["T"]

    st.dataframe(dados, use_container_width=True)

    st.subheader("📊 Ranking de Prioridade")

    fig, ax = plt.subplots()
    ax.barh(dados["Problema"], dados["Total"])
    ax.set_title("Prioridade dos Problemas (GUT)")
    ax.set_xlabel("Pontuação")

    st.pyplot(fig)

# -----------------------------------
# DIAGNÓSTICO
# -----------------------------------
elif menu == "Diagnóstico":

    st.subheader("🔍 Diagnóstico Organizacional")

    st.info("""
    A empresa possui forte posicionamento no mercado, porém apresenta fragilidades na gestão interna,
    especialmente na organização de processos, integração de dados e descentralização das decisões.

    A ausência de um Sistema de Gestão da Qualidade (SGQ) foi identificada como o principal problema,
    impactando diretamente a eficiência operacional e a padronização das atividades.
    """)

# -----------------------------------
# PLANO DE INTERVENÇÃO
# -----------------------------------
elif menu == "Plano de Intervenção":

    st.subheader("🛠 Plano de Intervenção")

    plano = pd.DataFrame({
        "Ação": [
            "Padronizar processos",
            "Implantar ERP",
            "Treinar colaboradores",
            "Implantar SGQ",
            "Criar KPIs"
        ],
        "Prazo": ["Curto", "Médio", "Médio", "Longo", "Médio"],
        "Responsável": ["Produção", "Adm", "RH", "Direção", "Todos"],
        "Impacto": ["Alto","Alto","Médio","Alto","Alto"]
    })

    st.dataframe(plano, use_container_width=True)

# -----------------------------------
# INDICADORES
# -----------------------------------
elif menu == "Indicadores":

    st.subheader("📊 Indicadores de Desempenho")

    col1, col2, col3 = st.columns(3)

    col1.metric("Erros operacionais", "-20%")
    col2.metric("Tempo de produção", "-15%")
    col3.metric("Retrabalho", "-25%")

    col4, col5, col6 = st.columns(3)

    col4.metric("Integração entre setores", "+30%")
    col5.metric("Satisfação do cliente", "+18%")
    col6.metric("Produtividade", "+22%")

    st.info("Indicadores estimados após implementação das melhorias propostas.")