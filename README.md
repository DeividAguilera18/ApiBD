# ApiBD
Desarrollo de API conectado a una BD desplegado en Docker 

primero para que ambos contenedores se pudieran hablar entré sí cree mi red de docker 
docker network create mi_red   

Para crear la imagen del api en docker usé:
docker build -t apitarea .

Despues para correrlo
 docker run --name miapi --network mi_red -p 8000:8000 -d apitarea:latest

 Para crear la imagen del mysql solo hice primero el pull
 docker pull mysql

 despues para correr la imagen y crear el contenedor usé
 docker run --name mysqlta --network mi_red -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -d mysql:latest

 en caso que el contenedor del mysql jale pero no te puedas conectar, me funcionó meterme al bash del contenedor y conectarme desde ahí,
 según el log del contenedor no estaba iniciado el servidor y solo me loguee con el usuario root y el password que puse en el docker run
  docker exec -it mysqlta bash  
 mysql -h localhost -u root -p

 
