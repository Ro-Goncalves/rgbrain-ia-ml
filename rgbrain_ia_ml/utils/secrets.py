import os

import streamlit as st

def carregar_secrets():
    for secrets in st.secrets.values():
        for secret_name, secret in secrets.items():            
            os.environ[secret_name] = secret