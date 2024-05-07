
from pytesseract import image_to_string
from PIL import Image
from easyocr import Reader
#import keras_ocr


def extrai_texto_com_pytesseract(imagem):
    # stream_imagem = Image.open(imagem)
    # return str(image_to_string(stream_imagem))
    ...

def extrai_texto_com_easyocr(imagem):
    leitor = Reader(["en"])
    texto = leitor.readtext(imagem.read())
    texto = "\n".join([res[1] for res in texto])

    return texto

def _keras_model_load():
#         pipeline = keras_ocr.pipeline.Pipeline()
#         return pipeline
    ...

def extrai_texto_com_keras_ocr(imagem):  
#     pipeline = _keras_model_load()  
#     prediction_groups = pipeline.recognize(imagem)
    
#     return prediction_groups
    # if visualization:
    #     fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
    #     for ax, image, predictions in zip(axs, images, prediction_groups):
    #         #print(predictions)
    #         keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
    ...