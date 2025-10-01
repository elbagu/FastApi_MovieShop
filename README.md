# FastApi_MovieShop
Proyecto de API de películas y tiendas con FastAPI y tests automatizados con Pytest.
🎬 Movie Shop API + Testing

Este proyecto implementa una API REST en FastAPI para la gestión de películas y tiendas, junto con una suite de tests automatizados en Pytest que validan su correcto funcionamiento.

🚀 Tecnologías utilizadas

FastAPI → Framework backend para construir la API

Pydantic → Validación de datos y modelos

Requests → Cliente HTTP para consumir la API desde los tests

Pytest → Framework de testing automatizado

📂 Estructura del proyecto
.
├── movie_backend/       # Código de la API (endpoints, modelos, servicios)
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── api_routes/      # Definición de rutas de la API
│   ├── models/          # Modelos y validaciones (Pydantic)
│   ├── services/        # Lógica de negocio
│   └── ...
│
├── testing/             # Suite de tests automatizados
│   ├── conftest.py      # Configuración de Pytest
│   ├── tests/           # Casos de prueba organizados por recurso
│   └── ...
│
└── README.md            # Documentación del proyecto

⚡ Funcionalidades principales

CRUD de Películas (/movies)

CRUD de Tiendas (/shops)

Asociación de películas a tiendas

Validación de errores con ErrorResponse (modelo Pydantic)

Tests que validan:

Creación, lectura, actualización y borrado de entidades

Manejo de errores (404, inputs inválidos, etc.)

Integración entre endpoints

▶️ Cómo ejecutar la API

Clonar el repositorio:

git clone https://github.com/tu-usuario/movie-shop-api.git
cd movie-shop-api/movie_backend


Instalar dependencias:

pip install -r requirements.txt


Levantar el servidor:

uvicorn main:app --reload


Abrir la documentación interactiva en Swagger:
👉 http://127.0.0.1:8000/docs

🧪 Cómo ejecutar los tests

Desde la carpeta raíz del proyecto:

cd testing
pytest -v

💡 Ejemplo de uso
Crear una película
POST /movies
{
  "name": "Inception",
  "genre": "Sci-Fi",
  "year": 2010
}

Respuesta
{
  "id": 1,
  "name": "Inception",
  "genre": "Sci-Fi",
  "year": 2010
}

📌 Nota

Este proyecto forma parte de un trabajo académico, adaptado para ser publicado como proyecto personal en GitHub.
