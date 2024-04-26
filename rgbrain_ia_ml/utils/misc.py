import streamlit as st
import os

import yaml

SEP = os.sep
NOME_PROJETO = "rgbrain_ia_ml"
CAMINHO_CONFIGURACOES_SERVICOS = os.path.join(NOME_PROJETO, "servicos", "configuracoes_servicos.yaml")

def new_line(n=1):
    for i in range(n):
        st.write("\n")

def nome_laboratorio(arquivo_laboratorio: str) -> str:
    return arquivo_laboratorio.split(f"{NOME_PROJETO}{SEP}pages{SEP}")[1].split(SEP)[0].replace(".py", "")

def carregar_configuracoes_servicos():
    with open(CAMINHO_CONFIGURACOES_SERVICOS, "r") as configuracoes:
        configuracoes_servicos = yaml.safe_load(configuracoes)
    return configuracoes_servicos