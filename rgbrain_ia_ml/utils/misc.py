import streamlit as st
import os

import yaml

SEP = os.sep
NOME_PROJETO = "rgbrain_ia_ml"
CAMINHO_CONFIGURACOES_SERVICOS = os.path.join(NOME_PROJETO, "servicos", "configuracoes_servicos.yaml")
CAMINHO_CONFIGURACOES_PAGINA = os.path.join(NOME_PROJETO, "pages", "configuracoes_pagina.yaml")

def _carregar_configuracoes(caminho_configuracaoes):
    with open(caminho_configuracaoes, "r", encoding='utf8') as configuracoes:
        configuracoes_pagina = yaml.safe_load(configuracoes)
    return configuracoes_pagina

def new_line(n=1):
    for i in range(n):
        st.write("\n")

def nome_laboratorio(arquivo_laboratorio: str) -> str:
    return arquivo_laboratorio.split(f"{NOME_PROJETO}{SEP}pages{SEP}")[1].split(SEP)[0].replace(".py", "")

def carregar_configuracoes_servicos():  
    return _carregar_configuracoes(CAMINHO_CONFIGURACOES_SERVICOS)

def carregar_configuracoes_pagina():
    return _carregar_configuracoes(CAMINHO_CONFIGURACOES_PAGINA)