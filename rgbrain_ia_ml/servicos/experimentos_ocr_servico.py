
from pytesseract import image_to_string
from PIL import Image
from io import BytesIO
from easyocr import Reader
from langchain.document_loaders.image import UnstructuredImageLoader


def extrai_texto_com_pytesseract(imagem):
    stream_imagem = Image.open(imagem)
    return str(image_to_string(stream_imagem))

def extrai_texto_com_easyocr(imagem):
    leitor = Reader(["en"])
    texto = leitor.readtext(imagem.read())
    texto = "\n".join([res[1] for res in texto])

    return texto

def extrai_texto_com_langchain_image(imagem):
    leitor = UnstructuredImageLoader(imagem)
    texto = leitor.load()

    return texto.page_content