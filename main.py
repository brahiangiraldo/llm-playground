from fastapi import FastAPI 
from llm_gemini import geminiThinkingLow
from fastapi.middleware.cors import CORSMiddleware 

#Crear una instancia de la aplicación FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

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