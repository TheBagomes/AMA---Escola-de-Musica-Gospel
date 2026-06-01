from fastapi import FastAPI

app = FastAPI(
    title="AMA Escola de Música Gospel API",
    description="API do sistema de gestão da AMA - Escola de Música Gospel",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "API da AMA Escola de Música Gospel funcionando!"}