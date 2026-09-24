# API-DE-REST

API RESTful desarrollada con FastAPI con CRUD para dos entidades: Usuario y Producto.

---

## Estructura del proyecto

```
API-DE-REST/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   └── producto.py
│   └── routes/
│       ├── __init__.py
│       ├── usuarios.py
│       └── productos.py
├── .venv/
├── venv/
├── .gitignore
├── README.md
├── requirements.txt
└── test.db
```

### Descripcion de cada archivo

- **app/__init__.py**: marca la carpeta app como paquete de Python.
- **app/main.py**: punto de entrada. Crea la instancia de FastAPI, registra los routers y crea las tablas al iniciar.
- **app/config.py**: configuracion del proyecto (variables, rutas, parametros generales).
- **app/db.py**: conexion a la base de datos y sesion por peticion.
- **app/models/__init__.py**: marca la carpeta models como paquete.
- **app/models/usuario.py**: modelo de la entidad Usuario.
- **app/models/producto.py**: modelo de la entidad Producto.
- **app/routes/__init__.py**: marca la carpeta routes como paquete.
- **app/routes/usuarios.py**: endpoints CRUD para Usuario.
- **app/routes/productos.py**: endpoints CRUD para Producto.
- **.venv/**: entorno virtual de Python.
- **venv/**: entorno virtual de Python.
- **.gitignore**: archivos que no se suben al repositorio.
- **README.md**: documentacion del proyecto.
- **requirements.txt**: dependencias del proyecto.
- **test.db**: base de datos SQLite local.

---

## Requisitos

- Python 3.12 (recomendado).
- pip y venv.

---

## Instalacion y ejecucion local

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd API-DE-REST
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

```bash
uvicorn app.main:app --reload --port 8000
```

La API estara disponible en:

- API raiz: http://localhost:8000/
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Entidades

### Usuario

Definido en app/models/usuario.py.

### Producto

Definido en app/models/producto.py.

---

## Endpoints

### Usuarios

Definidos en app/routes/usuarios.py.

| Metodo | Ruta             | Descripcion                  |
|--------|------------------|------------------------------|
| POST   | /usuarios/       | Crear usuario                |
| GET    | /usuarios/       | Listar todos los usuarios    |
| GET    | /usuarios/{id}   | Obtener un usuario por ID    |
| PATCH  | /usuarios/{id}   | Actualizar un usuario        |
| DELETE | /usuarios/{id}   | Eliminar un usuario          |

### Productos

Definidos en app/routes/productos.py.

| Metodo | Ruta              | Descripcion                  |
|--------|-------------------|------------------------------|
| POST   | /productos/       | Crear producto               |
| GET    | /productos/       | Listar todos los productos   |
| GET    | /productos/{id}   | Obtener un producto por ID   |
| PATCH  | /productos/{id}   | Actualizar un producto       |
| DELETE | /productos/{id}   | Eliminar un producto         |

---

## Documentacion interactiva

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

---

## Base de datos

- Motor: SQLite.
- Archivo: test.db.
- Se crea automaticamente al arrancar el servidor.
- No se sube a Git (esta en .gitignore).

---

## Comandos utiles

```bash
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
uvicorn app.main:app --host 0.0.0.0 --port 8000
pip freeze > requirements.txt
```

---

## Autor

Josue Camian

Proyecto academico. API RESTful con FastAPI.
