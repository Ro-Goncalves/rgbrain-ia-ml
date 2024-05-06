import streamlit as st
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain
from transformers import AutoTokenizer
import transformers
import torch

st.set_page_config(
    page_title = "Análise Sentimento",
    page_icon = "📈"
)

def _model():
    return 'mistralai/Mixtral-8x7B-Instruct-v0.1'


# def _auto_tokenizer():   
#     return AutoTokenizer.from_pretrained(_model())


# def _pipeline():
#     tokenizer = _auto_tokenizer()
#     pipeline = transformers.pipeline(
#         "text-generation",
#         model = _model(),
#         tokenizer=tokenizer,
#         torch_dtype=torch.float16,       
#         max_length=1000,
#         do_sample=True,
#         top_k=20,
#         num_return_sequences=1,
#         eos_token_id=tokenizer.eos_token_id,
#         token=''
#     )
    
#     return pipeline


def _llm():
    # return HuggingFacePipeline(pipeline=_pipeline(), model_kwargs={'temperature': 0.5})
    return HuggingFaceEndpoint(
        repo_id=_model(),
        huggingfacehub_api_token='', 
        temperature=0.5,
        model_kwargs={'max_length':512})


def _template():
    # return """
    #     Recognize all aspect terms with their corresponding sentiment polarity in the given review delimited by triple quotes. The aspect terms are nouns or phrases appearing in the review that indicate specific aspects or features of the product/service. Determine the sentiment polarity from the options [\"positive\", \"negative\", \"neutral\"]. Answer in the format [\"aspect\", \"sentiment\"] without any explanation. If no aspect term exists, then only answer \"[]\"."
    #     ```{text}```
    # """
    return """
        Reconheça todos os termos de aspecto com sua polaridade de sentimento correspondente
        na revisão dada delimitada por aspas triplas. Os termos de aspecto são substantivos 
        ou frases que aparecem na revisão que indicam aspectos ou características específicas 
        do produto/serviço. Determine a polaridade de sentimento a partir das opções 
        [\"positiva\", \"negativa\", \"neutra\"]. 
        Responda no formato [\"aspecto\", \"sentimento\"] sem qualquer explicação. 
        Se nenhum termo de aspecto existir, então responda apenas "[]"."
        ```{text}```
    """

def _llm_chain():
    prompt = PromptTemplate(template=_template(), input_variables=['text'])
    return LLMChain(prompt=prompt, llm=_llm())

LLM_CHAIN = _llm_chain()


st.markdown("""
    # Como Você Está Se Sentindo Hoje
    ---
            
    Essa é uma demo que demonstra como o ***Zero Shot Classification*** funciona. Tentaremos 
    extrair os apspectios e o sentimento sobre ele.    
""")

st.session_state.texto = st.text_input('Diga-Me o que sente')

if st.session_state.texto:
    st.markdown("""
        ### Eis o que eu penso sobre você ...
        ---
    """)
    response = LLM_CHAIN.invoke(st.session_state.texto)
    st.markdown(response)
    