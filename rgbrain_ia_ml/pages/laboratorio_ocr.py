import streamlit as st

from utils.menus import laboratorios_menu

st.set_page_config(page_title="LAB OCR", layout="centered")

st.markdown("# LABORATÓRIO OCR")

with st.sidebar:
    laboratorios_menu(__file__)