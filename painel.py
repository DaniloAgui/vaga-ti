import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# --------- DADOS (edite se quiser) ---------
jobs = [
    {
        "Empresa": "Cliente FC",
        "Vaga": "Pessoa Desenvolvedora Front-end Angular",
        "Local": "Rio de Janeiro (possível remoto)",
        "Senioridade": "Junior/Pleno/Sênior (indet.)",
        "Obrigatórias (hard)": ["Angular", "AWS", "Desenvolvimento Front-end",],
        "Soft skills": ["Trabalho em equipe", "Boas práticas/arquitetura", "Aprendizado contínuo", "performance", "usabalidade"],
        "Salário (faixa)": "R$ 9k-10k/mês"
    },
    {
        "Empresa": "Grupo AMP",
        "Vaga": "Programador",
        "Local": "Santo andre, Sp (Presencial/Tempo integral)",
        "Senioridade": "Estagiário (Cursando ensino superior em TI)",
        "Obrigatórias (hard)": ["SQL", "Php", "JavaScript", "HTML"],
        "Soft skills": ["Comunicação", "Trabalho em equipe", "Organização"],
        "Salário (faixa)": "R$ 1.145,00 + VR R$ 13,50 ao dia + VT"
    },
    {
        "Empresa": "Bradesco",
        "Vaga": "Data Scientist I",
        "Local": "Osasco (SP)",
        "Senioridade": "Júnior/Pleno inicial",
        "Obrigatórias (hard)": ["Python", "SQL", "Spark", "Estatística/ML", "pandas", "scikit-learn", "matplotlib", "Databricks"],
        "Desejáveis (hard)": ["Big Data", "Engenharia de dados", "Cloud (Azure)"],
        "Soft skills": ["Resolução de problemas", "Trabalho com grandes volumes de dados", "Colaboração"],
        "Salário (faixa)": "R$ 79k–130k/ano (~R$ 6.5k–10.8k/mês)"
    },
    {
        "Empresa": "Autou",
        "Vaga": "Desenvolvedor Fullstack (Estágio/Trainee/Dev)",
        "Local": "Brasil (não informado)",
        "Senioridade": "Estágio/Trainee/Junior",
        "Obrigatórias (hard)": ["Fundamentos Web", "Stack Full (ex.: Node.js + React)"],
        "Desejáveis (hard)": ["SQL", "Git", "Testes"],
        "Soft skills": ["Vontade de aprender", "Trabalho em equipe"],
        "Salário (faixa)": "Estágio: ~R$900–1.200/mês (mercado)"
    },
    {
        "Empresa": "Foursys",
        "Vaga": "Analista de Segurança da Informação - SOC",
        "Local": "Brasil (varia)",
        "Senioridade": "Júnior/Pleno",
        "Obrigatórias (hard)": ["Monitoramento SOC", "SIEM", "Resposta a incidentes", "Normas (LGPD/ISO/NIST)"],
        "Desejáveis (hard)": ["Automação (scripts)", "Cloud/EDR/Firewall"],
        "Soft skills": ["Comunicação clara (relatórios)", "Trabalho sob pressão", "Trabalho em equipe"],
        "Salário (faixa)": "Jr/Pl: ~R$3.2k–5.4k/mês (mercado)"
    }
]

# Criação dos DataFrames necessários
df = pd.DataFrame(jobs)

# Hard skills
from collections import Counter

hard_skills = []
for job in jobs:
    hard_skills.extend(job["Obrigatórias (hard)"])
hard_counter = Counter(hard_skills)
hard_df = pd.DataFrame(hard_counter.items(), columns=["Skill", "Qtd_vagas"]).sort_values(by="Qtd_vagas", ascending=False)

# Soft skills
soft_skills = []
for job in jobs:
    soft_skills.extend(job["Soft skills"])
soft_counter = Counter(soft_skills)
soft_df = pd.DataFrame(soft_counter.items(), columns=["Soft skill", "Qtd_vagas"]).sort_values(by="Qtd_vagas", ascending=False)

# Salários
sal_df = df[["Empresa", "Vaga", "Salário (faixa)"]]

st.title("Dashboard de Vagas de TI 26/08/2025")

st.header("Comparativo de Vagas")
st.dataframe(df)

st.header("Hard Skills mais comuns")
st.dataframe(hard_df)
fig1, ax1 = plt.subplots()
ax1.bar(hard_df["Skill"], hard_df["Qtd_vagas"])
ax1.set_title("Hard skills mais comuns")
ax1.set_xlabel("Skill")
ax1.set_ylabel("Qtd de vagas")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig1)

st.header("Soft Skills mais pedidas")
st.dataframe(soft_df)
fig2, ax2 = plt.subplots()
ax2.bar(soft_df["Soft skill"], soft_df["Qtd_vagas"])
ax2.set_title("Soft skills mais pedidas")
ax2.set_xlabel("Soft skill")
ax2.set_ylabel("Qtd de vagas")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig2)

st.header("Salários (Comparativo)")
st.dataframe(sal_df)