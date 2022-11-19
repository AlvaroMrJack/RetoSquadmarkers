# Reto Squadmarkers

_API Rest creada con el lenguaje Python, el Framework Flask Restful la cual es la encargada de retornar chistes desde el consumo de dos diferentes EndPoints, realiza acciones de crear un chiste en una base de datos de MongoDB, actualiza chistes en la base de datos de MongoDB, elimina chistes desde la base de datos de MongoDB y realiza cálculos matemáticos en base a el valor ingresado._

### Prerequisitos 📋

_Que se necesita para lanzar la API?_

- Cliente Git para clonar repositorio
- Python (current latest version: 3.11.0)
- Instalador de paquetes PIP (es recomendable habilitar la instalación de PIP al momento de instalar Python en el SO)
- Base de datos local MongoDB
- Instalar módulos necesarios para la API (módulos establecidos en documento [requirements.txt](requirements.txt))
- Cliente Postman para realizar pruebas de los EndPoints (Opcional)


### Como instalar 🔧

_Clonar proyecto en un directorio_

- Clonar proyecto en un directorio
- Crear un entorno virtual para hacer la instalación de los módulos necesarios

```
python -m venv venv
```
- Activar entorno virtual
```
venv\Scripts\activate
```
- Una vez activado el entorno virtual, instalar los módulos necesarios con el siguiente comando:
```
pip install -r requirements.txt
```
- Es momento de lanzar la API con el siguiente comando
```
python -m flask run
```
- La url principal del proyecto por defecto es _http://localhost:5000/v1/_

### Documentación de API 🖹

- La documentación de este proyecto se encuentra en el archivo [doc.yaml](doc.yaml)

### Unittest

_Las APIs fueron probadas bajo pruebas unitarias abarcando los casos que se solicitaba en el _Reto_. A continuación, se ejemplifica como utilizarla._

Para ejecutar la prueba unitaria seguir los siguientes pasos:

- Entrar al directorio [/unittest](/unittest) del proyecto
- Una vez dentro del directorio [/unittest](/unittest) ejecutar el siguiente comando:

```
python api_test.py
```

- Comenzará el proceso de prueba unitaria para los EndPoints de la API

### ¿Qué repositorio utilizaría para este proyecto? ❓

_Análisis del porque utilicé MongoDB_

- Para este caso de uso, donde los datos entregados por las APIs de chistes a consumir son del tipo JSON, la mejor opción es utilizar un repositorio de MongoDB ya que al ser una base de datos NoSQL entrega un escalamiento horizontal y el soporte para data no estructurada.

- Las sentencias de creación de la base de datos RetoDB y la collection chistes_collection se encuentra en el siguiente archivo [create_mongodb_bbdd](create_mongodb_bbdd.txt)

### Author ✒️

* **Álvaro Muñoz** - *Software Developer* - [AlvaroMrJack](https://github.com/AlvaroMrJack)

---
⌨️ with 💪 by [AlvaroMrJack](https://github.com/AlvaroMrJack) 🦅
