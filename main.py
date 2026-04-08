from fastapi import FastAPI 
from llm_gemini import geminiThinkingLow

#Crear una instancia de la aplicación FastAPI
app = FastAPI()

# print(response)
@app.get("/")
def read_root():
    return {"message": "API Skynet is running"}


#empoint para el asistente, recibe un prompt como parámetro y devuelve la respuesta del asistente con metodo get
@app.post("/entity")
def get_response_entity(request: dict):
    prompt = request["prompt"]
    response = geminiThinkingLow(prompt)
    return {response}