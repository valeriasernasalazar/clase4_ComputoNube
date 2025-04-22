# clase4_ComputoNube

## Requisitos previos
- GitHub CLI instalado
- Python y dependencias necesarias:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - joblib
  - requests
  - json
  - azureml-core
- Acceso al archivo `uri.json` (proporcionado en los comentarios de Canvas)
- Ancho de banda suficiente para la transferencia de datos y modelo a la nube (Para el despliegue inicial, que requiere subir el modelo y configurar el entorno, es recomendable contar con 10-20 Mbps para que el proceso no sea demasiado lento)

## Instrucciones de uso

### 1. Clonar el repositorio

```bash
gh fork valeriasernasalazar/clase4_ComputoNube
cd clase4_ComputoNube
```

### 2. Configuración del archivo de conexión

Mueve el archivo `uri.json` (localizado en el comentario de Canvas) al directorio del proyecto:

```bash
mv /ruta/al/uri.json .
```

### 3. Limpieza y creación del modelo

Para preparar y entrenar el modelo, ejecuta el notebook:

```bash
jupyter notebook model.ipynb
```

Este paso es esencial para la limpieza de datos y la creación del modelo que se utilizará posteriormente. El notebook se encarga de:
- Procesar los datos
- Codificar lasd variables categóricas
- Entrenar un modelo de regresión lineal
- Guardar el modelo en formato pickle

### 4. Despliegue del modelo

Para realizar el despliegue del modelo en la nube, ejecuta:

```bash
jupyter notebook deployer.ipynb
```

Este notebook utiliza el ID proporcionado en el archivo JSON para configurar el entorno de despliegue. El proceso incluye:
- Descargar el config.json y moverlo al cd utilizando

```bash
mv /ruta/al/config.json .
```

- Creación de un workspace en Azure ML
- Registro del modelo en la nube
- Despliegue del modelo como un servicio web
- Generación del archivo uri.json con la URL del servicio

### 5. Ejecución del API

Una vez completados los pasos anteriores, ejecuta:

```bash
python API2.py
```

Esto mostrará las predicciones para los primeros 5 registros de la base de datos.

## Estructura del proyecto

```
clase4_ComputoNube/
├── API2.py                # Script principal para ejecutar predicciones
├── model.ipynb            # Notebook para limpieza y creación del modelo
├── modelo.pkl             # Modelo serializado generado por model.ipynb
├── deployer.ipynb         # Notebook para despliegue del modelo
├── score.py               # Script de puntuación generado por deployer.ipynb
├── uri.json               # Archivo de configuración con credenciales (añadir manualmente)
└── README.md              # Documentación básica
```

