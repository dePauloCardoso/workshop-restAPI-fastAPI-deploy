from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/outro_recurso")
def pegar_recurso():
    return "message for testing my fastAPI"
