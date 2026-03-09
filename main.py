from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"¡FastAPI funcionando en mi App2!"}


@app.get("/saludar/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}