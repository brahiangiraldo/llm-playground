from dotenv import load_dotenv
from google import genai
from google.genai import types 

from PIL import Image
import os
from io import BytesIO 


load_dotenv()

# 1 Configuración de nivel de pensamiento normal
def geminiThink(content):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=content
    )
    return response.text

# resp = geminiThink("¿a como esta el dolar hoy?")
# print(resp)



# 2 Configuración de nivel de pensamiento bajo nivel
def geminiThinkingLow(content):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=content,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low"),
            system_instruction="responde con menos de 20 palabras en un contexto coherente"
        ),
    )     
    return response.text 

# resp2 = geminiThinkingLow("¿Cual es tu proposito en la vida ?")
# print(resp2)




# 3 Configuración de nivel de pensamiento alto nivel e imagen
# client = genai.Client()
# prompt = ("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme")
# response = client.models.generate_content(
#     model="gemini-2.0-flash-exp",
#     contents=[prompt],
# )

# for part in response.parts:
#     if part.text is not None:
#         print(part.text)
#     elif part.inline_data is not None:
#         image = part.as_image()
#         image.save("generated_image.png")

#         print("✅ Imagen guardada: generated_image.png")





 # 4 Resumir texto
# --- Ejemplo: Resumir un texto con Gemini ---
def resumir_texto(content):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=content
    )
    return response.text

# Prueba de resumen
texto = """
A veces nos pasa que dudamos, ¿verdad? Pero miren a Ana, la mamá de Samuel. No podía tener hijos y lloró amargamente ante Dios. Le dijo: "Si me das un hijo, te lo dedico". Dios le cumplió, le dio a Samuel, y Ana lo llevó al templo tal como prometió. Como respuesta, Dios le bendijo con más hijos. ¡Nos pasa que cuando somos fieles, Él nos bendice más!.
"""
prompt = f"Resume el siguiente texto en 3 frases:\n\n{texto}"
# print("--- Resumen generado por Gemini ---")
# print(resumir_texto(prompt))



# --- 5 Ejemplo: Traducción de idiomas con Gemini ---
def traducir(texto, idioma_destino):
    client = genai.Client()
    prompt = f"Traduce al {idioma_destino}: {texto}"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text

# Prueba de traducción
frase = "¿Cómo estás hoy?"
idioma = "inglés"
# print(f"--- Traducción al {idioma} ---")
# print(traducir(frase, idioma))


