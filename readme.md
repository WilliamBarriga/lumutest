# Prueba Tecnica Lumu

al momento de ejecucion del script se cargaran los logs al api y luego en la consola se mostraran las estadisticas de los logs 

## Configuracion
En caso de usar docker para la ejecucion del proyecto, se deben seguir los siguientes pasos:
- Ejecutar el comando `docker build -t lumu .` para construir la imagen

- Ejecutar el comando `docker run --name {container_name} lumu {path_to_file}` para construir la imagen. (container_name: nombre del contenedor, path_to_file ruta al archivo con los logs)
  - `docker run --name data lumu queries`

En caso de usar un entorno virtual, se deben seguir los siguientes pasos:
- Crear un entorno virtual con python 3.11 o superior, con el comando `python -m venv venv`
- Activar el entorno virtual con el comando `source venv/bin/activate` o `venv\Scripts\activate` en windows
- Instalar las dependencias con el comando `pip install -r requirements.txt`
- Ejecutar el script `python main.py {path_to_file}`
  - `python main.py queries`


