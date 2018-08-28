# Redis-And-Flask
Aplicacion Web, desarrollada en Python, con consultas a un container redis de docker con data persistente.
### Para levantar Flask App

Levantar el container de redis en el puerto 261 con el volumen definido al directorio /data presente en el repositorio.
```
docker run -v $(pwd)/data:/data --name redis-container -p 261:6379 -d redis redis-server --appendonly yes
```
El programa se puede iniciar con el siguiente comando desde PowerShell
```
$env:FLASK_APP = "__init__.py"
flask run
```
También se puede inicar flask en un container para evitar correr la línea anterior.
(Dentro del directorio buscador) - Crear la imagen a partir del Dockerfile.
```
docker build -t nombre-imagen .
```
Para consultar las llaves guardadas en el volumen, correr el siguiente comando para ingresar al redis client.
```
docker run -it --link redis-container:redis --rm redis redis-cli -h redis -p 6379
```
