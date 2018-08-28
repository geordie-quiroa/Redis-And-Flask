# Redis-And-Flask
Aplicacion Web con consultas a un container redis de docker con data persistente.
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
También puede crear una imagen a partir del dockerfile, en lugar de correr el comando anterior. Para esto es necesario linkear el container

```
docker run -v $(pwd)/data:/data --name redis-container -p 261:6379 -d redis redis-server --appendonly yes
docker run -it --link redis-container:redis --rm redis redis-cli -h redis -p 6379
```
