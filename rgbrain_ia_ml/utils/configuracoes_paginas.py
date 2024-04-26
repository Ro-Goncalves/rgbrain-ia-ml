import streamlit as st

from .misc import nome_laboratorio as _nome_laboratorio
from .misc import carregar_configuracoes_servicos

def configura_pagina(arquivo_laboratorio):
    nome_laboratorio = _nome_laboratorio(arquivo_laboratorio)
    configuracoes_servicos = carregar_configuracoes_servicos()
    return configuracoes_servicos[nome_laboratorio]