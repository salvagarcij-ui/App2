# App2

API RESTful construida con FastAPI.

## Descripción

App2 es una API simple desarrollada con FastAPI que proporciona endpoints básicos para interacciones simples.

## Instalación

### Requisitos previos

- Python 3.8 o superior

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el servidor de desarrollo con uvicorn:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en: `http://localhost:8000`

## Endpoints

### GET `/`

Retorna un mensaje de bienvenida confirmando que la API está funcionando.

**Respuesta:**
```json
{
  "¡FastAPI funcionando en mi App2!": true
}
```

### GET `/saludar/{nombre}`

Retorna un saludo personalizado con el nombre proporcionado en la URL.

**Parámetros:**
- `nombre` (str): Nombre de la persona a saludar

**Ejemplo:**
```
GET /saludar/Maria
```

**Respuesta:**
```json
{
  "mensaje": "¡Hola, Maria!"
}
```

## Documentación

- Documentación interactiva (Swagger UI): `http://localhost:8000/docs`
- Documentación alternativa (ReDoc): `http://localhost:8000/redoc`