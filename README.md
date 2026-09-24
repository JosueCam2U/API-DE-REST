# Hello-API

API RESTful desarrollada con FastAPI que incluye:

- Endpoints basicos de bienvenida (/, /hola, /gif, /health).
- CRUD completo para dos entidades: Productos y Pedidos.
- Persistencia con SQLModel + SQLite.
- Documentacion automatica con Swagger UI (/docs) y ReDoc (/redoc).

---

## Estructura del proyecto

```
Hello-API/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada, monta routers y crea BD
│   ├── database.py          # Engine, sesion y creacion de tablas
│   ├── models.py            # Modelos SQLModel (Producto, Pedido)
│   └── routers/
│       ├── __init__.py
│       ├── home.py          # Endpoints basicos (/, /hola, /gif, /health)
│       ├── productos.py     # CRUD de Productos
│       └── pedidos.py       # CRUD de Pedidos
├── requirements.txt
├── ecosystem.config.js
├── .gitignore
└── README.md
```

### Descripcion de cada archivo

- **app/__init__.py**: marca la carpeta app como un paquete de Python.
- **app/main.py**: punto de entrada de la aplicacion. Crea la instancia de FastAPI, registra los routers y ejecuta la creacion de las tablas al iniciar el servidor usando lifespan.
- **app/database.py**: define el engine de SQLModel, la URL de conexion a SQLite, la funcion create_db_and_tables() y la dependencia get_session() que provee una sesion por cada peticion.
- **app/models.py**: contiene los modelos de datos. Define Producto y Pedido como tablas, junto con sus esquemas de creacion y actualizacion (ProductoCreate, ProductoUpdate, PedidoCreate, PedidoUpdate).
- **app/routers/__init__.py**: marca la carpeta routers como un paquete.
- **app/routers/home.py**: agrupa los endpoints basicos: /, /hola, /gif y /health.
- **app/routers/productos.py**: implementa el CRUD de Productos (crear, listar, obtener por ID, actualizar y eliminar).
- **app/routers/pedidos.py**: implementa el CRUD de Pedidos y aplica las reglas de negocio relacionadas con el stock del producto.
- **requirements.txt**: lista de dependencias del proyecto.
- **ecosystem.config.js**: archivo de configuracion de pm2 para desplegar la API en la instancia EC2 como un servicio.
- **.gitignore**: archivos y carpetas que no se suben al repositorio (entorno virtual, base de datos local, cache, etc.).

---

## Requisitos

- Python 3.12 (recomendado). Python 3.14 puede dar problemas de compatibilidad con Pydantic/SQLModel.
- pip y venv.
- Opcional: mise para gestionar versiones de Python.

---

## Instalacion y ejecucion local

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd Hello-API
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
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

## Dependencias

```txt
fastapi==0.115.0
uvicorn[standard]==0.32.0
sqlmodel>=0.0.27
```

- **FastAPI**: framework web.
- **Uvicorn**: servidor ASGI.
- **SQLModel**: ORM que combina SQLAlchemy + Pydantic.

Nota: la version de SQLModel se fija en >=0.0.27 para garantizar compatibilidad con Python 3.14.

---

## Modelos de datos

### Producto

| Campo    | Tipo   | Reglas                          |
|----------|--------|---------------------------------|
| id       | int    | Autogenerado (PK)               |
| nombre   | str    | Requerido, 1-100 caracteres     |
| precio   | float  | Requerido, > 0                  |
| stock    | int    | >= 0, por defecto 0             |

### Pedido

| Campo         | Tipo     | Reglas                                          |
|---------------|----------|-------------------------------------------------|
| id            | int      | Autogenerado (PK)                               |
| producto_id   | int      | Requerido, FK a producto.id                     |
| cantidad      | int      | Requerido, > 0                                  |
| total         | float    | Calculado automaticamente (precio x cantidad)   |
| fecha         | datetime | Autogenerado (UTC)                              |

---

## Endpoints

### Home

| Metodo | Ruta       | Descripcion                          |
|--------|------------|--------------------------------------|
| GET    | /          | Mensaje de bienvenida (JSON)         |
| GET    | /hola      | Saludo personalizado (?nombre=)      |
| GET    | /gif       | Pagina HTML con GIF animado          |
| GET    | /health    | Estado del servicio                  |

Ejemplos:

```bash
curl http://localhost:8000/

curl "http://localhost:8000/hola?nombre=Josue"

curl http://localhost:8000/health
```

---

### Productos - /productos

| Metodo | Ruta               | Descripcion                          |
|--------|--------------------|--------------------------------------|
| POST   | /productos/        | Crear producto                       |
| GET    | /productos/        | Listar todos los productos           |
| GET    | /productos/{id}    | Obtener un producto por ID           |
| PATCH  | /productos/{id}    | Actualizar parcialmente un producto  |
| DELETE | /productos/{id}    | Eliminar un producto                 |

Ejemplos:

Crear producto:

```bash
curl -X POST http://localhost:8000/productos/ \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Cafe","precio":4.5,"stock":10}'
```

Listar productos:

```bash
curl http://localhost:8000/productos/
```

Obtener uno:

```bash
curl http://localhost:8000/productos/1
```

Actualizar (PATCH):

```bash
curl -X PATCH http://localhost:8000/productos/1 \
  -H "Content-Type: application/json" \
  -d '{"precio":5.0,"stock":20}'
```

Eliminar:

```bash
curl -X DELETE http://localhost:8000/productos/1
```

---

### Pedidos - /pedidos

| Metodo | Ruta             | Descripcion                       |
|--------|------------------|-----------------------------------|
| POST   | /pedidos/        | Crear pedido                      |
| GET    | /pedidos/        | Listar todos los pedidos          |
| GET    | /pedidos/{id}    | Obtener un pedido por ID          |
| PATCH  | /pedidos/{id}    | Actualizar cantidad de un pedido  |
| DELETE | /pedidos/{id}    | Eliminar pedido                   |

Ejemplos:

Crear pedido:

```bash
curl -X POST http://localhost:8000/pedidos/ \
  -H "Content-Type: application/json" \
  -d '{"producto_id":1,"cantidad":2}'
```

Listar pedidos:

```bash
curl http://localhost:8000/pedidos/
```

Actualizar cantidad:

```bash
curl -X PATCH http://localhost:8000/pedidos/1 \
  -H "Content-Type: application/json" \
  -d '{"cantidad":5}'
```

Eliminar pedido:

```bash
curl -X DELETE http://localhost:8000/pedidos/1
```

---

## Reglas de negocio

Al crear un pedido:

- Se valida que el producto exista.
- Se valida que haya stock suficiente.
- Se descuenta el stock del producto.
- Se calcula total = precio x cantidad.

Al actualizar la cantidad de un pedido:

- Se ajusta el stock del producto segun la diferencia.
- Se recalcula el total.
- Se valida que no quede stock negativo.

Al eliminar un pedido:

- Se devuelve el stock al producto.

Errores controlados:

- 404: producto o pedido no encontrado.
- 400: stock insuficiente.
- 422: datos invalidos (validacion automatica de Pydantic).

---

## Documentacion interactiva

FastAPI genera documentacion automatica a partir de los modelos y tipos:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

Desde /docs se pueden probar todos los endpoints sin necesidad de curl.

---

## Base de datos

- Motor: SQLite (archivo local database.db).
- Se crea automaticamente al arrancar el servidor (via lifespan en app/main.py).
- No requiere configuracion adicional.

El archivo database.db no se sube a Git (esta en .gitignore).

Para reiniciar la BD en local:

```bash
rm database.db
uvicorn app.main:app --reload --port 8000
```

---

## Ejemplo de flujo completo

```bash
# 1. Crear un producto
curl -X POST http://localhost:8000/productos/ \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Cafe","precio":4.5,"stock":10}'

# 2. Crear un pedido de 2 unidades
curl -X POST http://localhost:8000/pedidos/ \
  -H "Content-Type: application/json" \
  -d '{"producto_id":1,"cantidad":2}'

# 3. Verificar que el stock bajo a 8
curl http://localhost:8000/productos/1

# 4. Eliminar el pedido, el stock vuelve a 10
curl -X DELETE http://localhost:8000/pedidos/1

# 5. Confirmar
curl http://localhost:8000/productos/1
```

---

## Despliegue en AWS EC2

Pasos generales utilizados para el despliegue:

1. Crear instancia EC2 (Amazon Linux 2023 o Ubuntu 22.04).

2. Configurar Security Group:
   - Permitir SSH (22) desde tu IP.
   - Permitir TCP 8000 desde 0.0.0.0/0.

3. Conectarse por SSH:

```bash
chmod 400 hello-api-key.pem
ssh -i hello-api-key.pem ubuntu@<IP_PUBLICA>
```

4. Instalar dependencias del sistema:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git
```

5. Clonar el repo:

```bash
git clone <URL_DEL_REPO>
cd Hello-API
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Correr con pm2 usando el archivo ecosystem.config.js:

```bash
sudo apt install -y nodejs npm
sudo npm install -g pm2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

7. Probar desde fuera:

```
http://<IP_PUBLICA>:8000/docs
```

Nota: usar --host 0.0.0.0 es obligatorio en EC2 para que Uvicorn escuche en todas las interfaces.

---

## Comandos utiles

```bash
# Activar entorno
source venv/bin/activate

# Correr servidor en modo desarrollo
uvicorn app.main:app --reload --port 8000

# Correr servidor accesible desde la red (EC2)
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Congelar dependencias actuales
pip freeze > requirements.txt

# Ver version de Python
python --version

# Gestionar el proceso en EC2 con pm2
pm2 status
pm2 logs hello-api
pm2 restart hello-api
pm2 stop hello-api
pm2 delete hello-api
```

---

## Autor

Josue Camian

Proyecto academico. Desarrollo de una API RESTful con FastAPI y despliegue en AWS EC2.
