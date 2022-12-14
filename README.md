# Reto Squadmarkers

_API Rest creada con el lenguaje Python, el Framework Flask Restful la cual es la encargada de retornar chistes desde el consumo de dos diferentes EndPoints, realiza acciones de crear un chiste en una base de datos de MongoDB, actualiza chistes en la base de datos de MongoDB, elimina chistes desde la base de datos de MongoDB y realiza c谩lculos matem谩ticos en base a el valor ingresado._

### Prerequisitos 馃搵

_Que se necesita para lanzar la API?_

- Cliente Git para clonar repositorio
- Python (current latest version: 3.11.0)
- Instalador de paquetes PIP (es recomendable habilitar la instalaci贸n de PIP al momento de instalar Python en el SO)
- Base de datos local MongoDB
- Instalar m贸dulos necesarios para la API (m贸dulos establecidos en documento [requirements.txt](requirements.txt))
- Cliente Postman para realizar pruebas de los EndPoints (Opcional)


### Como instalar 馃敡

_Clonar proyecto en un directorio_

- Clonar proyecto en un directorio
- Crear un entorno virtual para hacer la instalaci贸n de los m贸dulos necesarios

```
python -m venv venv
```
- Activar entorno virtual
```
venv\Scripts\activate
```
- Una vez activado el entorno virtual, instalar los m贸dulos necesarios con el siguiente comando:
```
pip install -r requirements.txt
```
- Es momento de lanzar la API con el siguiente comando
```
python -m flask run
```
- La url principal del proyecto por defecto es _http://localhost:5000/v1/_

### Documentaci贸n de API 馃柟

- La documentaci贸n de este proyecto se encuentra en el archivo [doc.yaml](doc.yaml)

### Unittest

_Las APIs fueron probadas bajo pruebas unitarias abarcando los casos que se solicitaba en el _Reto_. A continuaci贸n, se ejemplifica como utilizarla._

Para ejecutar la prueba unitaria seguir los siguientes pasos:

- Entrar al directorio [/unittest](/unittest) del proyecto
- Una vez dentro del directorio [/unittest](/unittest) ejecutar el siguiente comando:

```
python api_test.py
```

- Comenzar谩 el proceso de prueba unitaria para los EndPoints de la API

### 驴Qu茅 repositorio utilizar铆a para este proyecto? 鉂?

_An谩lisis del porque utilic茅 MongoDB_

- Para este caso de uso, donde los datos entregados por las APIs de chistes a consumir son del tipo JSON, la mejor opci贸n es utilizar un repositorio de MongoDB ya que al ser una base de datos NoSQL entrega un escalamiento horizontal y el soporte para data no estructurada.

- Las sentencias de creaci贸n de la base de datos RetoDB y la collection chistes_collection se encuentra en el siguiente archivo [create_mongodb_bbdd](create_mongodb_bbdd.txt)

### Author 鉁掞笍

* **脕lvaro Mu帽oz** - *Software Developer* - [AlvaroMrJack](https://github.com/AlvaroMrJack)

---
鈱笍 with 馃挭 by [AlvaroMrJack](https://github.com/AlvaroMrJack) 馃
