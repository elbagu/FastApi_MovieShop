# Movie Backend & Testing Suite

Este proyecto es una implementación de una **API RESTful para gestión de películas y tiendas**, junto con una **suite de testing automatizado** desarrollada con `pytest`.  
Fue realizado como parte de un proyecto académico, pero está diseñado para ser fácilmente extensible como proyecto personal.

---

## 📂 Estructura del proyecto

```
├── movie_backend/        # Código de la API (FastAPI)
│   ├── src/              # Módulos principales
│   ├── models/           # Definiciones de requests/responses
│   ├── services/         # Lógica de negocio
│   └── main.py           # Punto de entrada de la API
│
├── testing/              # Tests con pytest
│   ├── tests/movies/     # Tests relacionados a películas
│   ├── tests/shops/      # Tests relacionados a tiendas
│   └── conftest.py       # Fixtures compartidas
│
└── README.md             # Documentación del proyecto
```

---

## 🚀 Funcionalidades principales

- CRUD de **Películas** (crear, listar, actualizar, eliminar).  
- CRUD de **Tiendas**.  
- Manejo de errores mediante un **modelo de respuesta estándar** (`ErrorResponse`).  
- Tests automatizados para validar **funcionalidad y errores comunes**.  

---

## ⚙️ Tecnologías utilizadas

- **Python 3.12**
- **FastAPI** (backend)
- **Pydantic** (validación de datos)
- **Requests** (cliente HTTP interno)
- **Pytest** (testing)
- **Uvicorn** (servidor ASGI para correr la API)

---

## ▶️ Cómo ejecutar la API

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/movie-backend.git
   cd movie-backend/movie_backend
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate    # En Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la API:
   ```bash
   uvicorn src.main:app --reload
   ```

La API estará disponible en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Cómo correr los tests

1. Ir a la carpeta `testing`:
   ```bash
   cd testing
   ```

2. Ejecutar pytest:
   ```bash
   pytest -v
   ```

---

## 📌 Ejemplo de uso (API)

- Crear una película:
  ```http
  POST /movies
  {
    "name": "Inception",
    "director": "Christopher Nolan",
    "gender": ["Sci-Fi"],
    "shop": 1
  }
  ```

- Respuesta exitosa:
  ```json
  {
    "id": 1,
    "name": "Inception",
    "director": "Christopher Nolan",
    "gender": ["Sci-Fi"],
    "shop": 1,
    "rent": false
  }
  ```

- Error (película no encontrada):
  ```json
  {
    "detail": ["Movie Not Found"]
  }
  ```

---

## 👨‍💻 Autor

Desarrollado por **Ismael Bazzino**
