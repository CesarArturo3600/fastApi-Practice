# LIST PRACTICE 001

## Convenciones de código y commit

Este proyecto utiliza herramientas para mantener la calidad del código y las convenciones de commit:

- [Git Hooks](./docs/git-hooks-setup.md): Automatización de tareas antes/después de commits
- [Commitlint](./docs/commitlint-config.md): Validación de mensajes de commit
- [Husky](./docs/husky-integration.md): Integración de git hooks con facilidad

## Entorno virtual

```
python -m venv [nombre de entorno virtual]
```

### linux

```
source nombre_del_entorno/bin/activate
```

### CMD

```
nombre_del_entorno\Scripts\activate
```

### powershell

```
.\nombre_del_entorno\Scripts\activate.ps1
```

### desactivar

```
deactivate
```

```
pip install -r requirements.txt

```

## REQUIREMENTS

```
annotated-types==0.7.0
anyio==4.9.0
certifi==2025.4.26
cffi==1.17.1
charset-normalizer==3.4.2
click==8.1.8
colorama==0.4.6
cryptography==44.0.3
docopt==0.6.2
dotenv==0.9.9
fastapi==0.115.12
greenlet==3.2.1
h11==0.16.0
idna==3.10
pipreqs==0.4.13
pycparser==2.22
pydantic==2.11.4
pydantic-settings==2.9.1
pydantic_core==2.33.2
PyMySQL==1.1.1
python-dotenv==1.1.0
requests==2.32.3
sniffio==1.3.1
SQLAlchemy==2.0.40
starlette==0.46.2
typing-inspection==0.4.0
typing_extensions==4.13.2
urllib3==2.4.0
uvicorn==0.34.2
yarg==0.1.10


```

## Esquema de proyecto

```
Cliente HTTP → Rutas → Servicios → Repositorios → Modelos → Base de datos
                 ↑                                    ↑
                 |                                    |
             database.py (get_db) ---------------→ database.py (Base)
                 |                                    |
                 ↓                                    ↓
           Esquemas ←-------------------------------- SQLAlchemy

```

## clase Connection

```py
# Este es un ejemplo conceptual, no código real de SQLAlchemy
class Engine:
    def __init__(self, url, **kwargs):
        # Analiza la URL para determinar el tipo de base de datos, host, usuario, etc.
        self.url = url
        self.driver_name, self.connection_params = parse_url(url)

        # Carga el driver adecuado (pymysql, psycopg2, etc.)
        self.driver = load_driver(self.driver_name)

        # Configura el pool según los parámetros
        self.pool = ConnectionPool(self, **kwargs)

    def connect(self):
        # Obtenemos una conexión del pool o creamos una nueva
        return self.pool.get_connection()

    def _create_raw_connection(self):
        # Crea una conexión de bajo nivel usando el driver
        raw_conn = self.driver.connect(
            host=self.connection_params.host,
            user=self.connection_params.user,
            password=self.connection_params.password,
            database=self.connection_params.database,
            port=self.connection_params.port
        )

        # Envuelve la conexión de bajo nivel en un objeto Connection de SQLAlchemy
        return Connection(self, raw_conn)

class Connection:
    def __init__(self, engine, raw_connection):
        self.engine = engine
        self.raw_connection = raw_connection  # El objeto de conexión real del driver
        self.transaction = None  # Inicialmente no hay transacción activa

    def execute(self, query, params=None):
        # Ejecuta una consulta SQL en la conexión
        cursor = self.raw_connection.cursor()
        cursor.execute(query, params)
        return cursor

    def close(self):
        # Cierra la conexión subyacente
        self.raw_connection.close()

```
