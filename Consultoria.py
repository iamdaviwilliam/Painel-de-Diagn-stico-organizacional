import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# -----------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------
st.set_page_config(
    page_title="Painel de Diagnóstico Organizacional",
    page_icon="🏢",
    layout="wide"
)

# -----------------------------------
# CSS PERSONALIZADO
# -----------------------------------
st.markdown("""
<style>
    .titulo {
        font-size: 2.3rem;
        font-weight: 700;
        color: #3A7CA5;
        margin-bottom: 0.2rem;
    }

    .subtitulo {
        font-size: 1rem;
        color: #cfd8dc;
        margin-bottom: 20px;
    }

    .card {
        background: linear-gradient(135deg, #1f3b5c, #2c4a6e);
        color: white !important;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
        line-height: 1.7;
    }

    .secao {
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .stMetric {
        background-color: rgba(255, 255, 255, 0.03);
        padding: 10px;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LOGO
# -----------------------------------
logo = Image.open("logo_alfa.png")

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.image(logo, width=180)

menu = st.sidebar.radio(
    "Navegação",
    [
        "Início",
        "SWOT",
        "Matriz GUT",
        "Diagnóstico",
        "Plano de Intervenção",
        "Indicadores"
    ]
)

# -----------------------------------
# CABEÇALHO
# -----------------------------------
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    st.image(logo, width=140)

with col_titulo:
    st.markdown(
        '<div class="titulo">Painel de Diagnóstico Organizacional</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subtitulo">Alfa Embalagem Ltda. | Apoio à tomada de decisão</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

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
    A Alfa Embalagem Ltda. é uma empresa familiar com atuação consolidada no mercado regional de embalagens de papelão ondulado,
    destacando-se pela qualidade dos produtos, capacidade produtiva, agilidade na entrega e presença em diferentes segmentos do Nordeste.

    O diagnóstico organizacional identificou fragilidades na gestão interna, especialmente relacionadas à ausência de um Sistema de Gestão
    da Qualidade (SGQ), à baixa integração entre setores, à dependência de ferramentas manuais como o Excel e à falta de padronização
    dos processos.

    Por se tratar de uma empresa familiar com decisões centralizadas, observa-se também a necessidade de fortalecimento da estrutura gerencial,
    melhoria da comunicação interna e maior organização dos fluxos operacionais.

    A Matriz GUT apontou a ausência de SGQ como o problema mais crítico, com impacto direto na padronização, na eficiência operacional e
    no suporte à tomada de decisão.
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
        - Forte atuação regional  
        """)

        st.markdown("#### 🟡 Oportunidades")
        st.markdown("""
        - Expansão no mercado do Nordeste  
        - Investimento em tecnologia  
        - Fortalecimento digital  
        - Novas parcerias  
        - Melhoria da integração entre setores  
        """)

    with col2:
        st.markdown("#### 🔴 Fraquezas")
        st.markdown("""
        - Decisões centralizadas  
        - Gestão familiar concentrada  
        - Processos manuais  
        - Falta de padronização  
        - Baixa integração entre setores  
        - Dependência do Excel  
        - Ausência de SGQ  
        """)

        st.markdown("#### ⚫ Ameaças")
        st.markdown("""
        - Concorrência local  
        - Pressão por preços  
        - Dependência de fornecedor  
        - Instabilidade econômica  
        - Aumento dos custos operacionais  
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
        "Gravidade": [5, 4, 3, 4],
        "Urgência": [5, 4, 4, 3],
        "Tendência": [4, 5, 4, 4]
    })

    dados["Total"] = dados["Gravidade"] * dados["Urgência"] * dados["Tendência"]

    st.dataframe(dados, use_container_width=True, hide_index=True)

    st.subheader("📊 Ranking de Prioridade")

    dados_ordenados = dados.sort_values("Total", ascending=True)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.barh(dados_ordenados["Problema"], dados_ordenados["Total"])
    ax.set_title("Pontuação dos Problemas Prioritários")
    ax.set_xlabel("Pontuação Total")
    ax.set_ylabel("Problemas")
    st.pyplot(fig)

    problema_topo = dados.sort_values("Total", ascending=False).iloc[0]["Problema"]
    pontuacao_topo = dados.sort_values("Total", ascending=False).iloc[0]["Total"]

    st.info(f"Problema mais crítico identificado: **{problema_topo}**, com pontuação **{pontuacao_topo}**.")

# -----------------------------------
# DIAGNÓSTICO
# -----------------------------------
elif menu == "Diagnóstico":

    st.subheader("🔍 Diagnóstico Organizacional")

    st.markdown("""
    A Alfa Embalagem Ltda. apresenta um posicionamento sólido no mercado regional, sustentado pela qualidade dos produtos,
    pela capacidade produtiva e pela agilidade nas entregas.

    Apesar desses pontos positivos, o diagnóstico evidenciou fragilidades na gestão interna, principalmente relacionadas
    à centralização das decisões, à ausência de um Sistema de Gestão da Qualidade (SGQ), à baixa integração entre os setores
    e à falta de padronização dos processos.

    Também foi identificada forte dependência de controles manuais e uso recorrente do Excel, o que dificulta a integração
    dos dados e reduz a eficiência do suporte à tomada de decisão.

    Diante disso, conclui-se que a empresa possui grande potencial de crescimento, mas precisa investir na modernização
    da gestão, na organização dos processos e no fortalecimento da sua estrutura administrativa.
    """)

# -----------------------------------
# PLANO DE INTERVENÇÃO
# -----------------------------------
elif menu == "Plano de Intervenção":

    st.subheader("🛠 Plano de Intervenção")

    plano = pd.DataFrame({
        "Ação": [
            "Padronizar os principais processos operacionais",
            "Mapear fluxos de trabalho",
            "Centralizar e organizar os dados existentes",
            "Implantar sistema integrado de gestão (ERP)",
            "Treinar colaboradores nos novos processos",
            "Criar indicadores de desempenho (KPIs)",
            "Implantar Sistema de Gestão da Qualidade (SGQ)"
        ],
        "Prazo": [
            "Curto",
            "Curto",
            "Curto",
            "Médio",
            "Médio",
            "Médio",
            "Longo"
        ],
        "Responsável": [
            "Produção / Supervisão",
            "Direção / Produção",
            "Administrativo",
            "Administrativo / Direção",
            "RH / Direção",
            "Todos os setores",
            "Direção / Consultoria"
        ],
        "Impacto": [
            "Alto",
            "Alto",
            "Alto",
            "Alto",
            "Médio",
            "Alto",
            "Alto"
        ]
    })

    st.dataframe(plano, use_container_width=True, hide_index=True)

    st.markdown("### 📌 Leitura do Plano")
    st.write("""
    As ações de curto prazo concentram-se na organização dos processos e dos dados.
    As ações de médio prazo focam na integração da gestão, na capacitação da equipe e no uso de tecnologia.
    Já as ações de longo prazo visam consolidar uma cultura de qualidade e melhoria contínua por meio da implantação do SGQ.
    """)

# -----------------------------------
# INDICADORES
# -----------------------------------
elif menu == "Indicadores":

    st.subheader("📊 Indicadores de Desempenho Sugeridos")

    col1, col2, col3 = st.columns(3)
    col1.metric("Redução de erros operacionais", "-20%")
    col2.metric("Tempo de produção", "-15%")
    col3.metric("Retrabalho", "-25%")

    col4, col5, col6 = st.columns(3)
    col4.metric("Integração entre setores", "+30%")
    col5.metric("Satisfação do cliente", "+18%")
    col6.metric("Produtividade", "+22%")

    st.info("Esses indicadores representam metas estimadas para acompanhamento após a implementação das melhorias propostas.")

    indicadores = pd.DataFrame({
        "Indicador": [
            "Redução de erros operacionais",
            "Tempo de produção e entrega",
            "Nível de retrabalho",
            "Grau de integração entre setores",
            "Satisfação dos clientes",
            "Produtividade dos colaboradores"
        ],
        "Objetivo": [
            "Melhorar a confiabilidade dos processos",
            "Aumentar a eficiência operacional",
            "Reduzir desperdícios e falhas",
            "Melhorar fluxo de informação",
            "Elevar percepção de qualidade",
            "Aumentar desempenho da equipe"
        ]
    })

    st.dataframe(indicadores, use_container_width=True, hide_index=True)
