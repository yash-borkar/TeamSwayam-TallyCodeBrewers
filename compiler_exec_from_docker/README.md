# compiler_exec_from_docker
docker container exec for multiple isolated compilers to execute in flask application

### check for running services in docker ( cmd utils )
```
docker ps # to check running process
```
#### before building container ensure to clear other services
```
docker-compose down
```
#### inside compiler_exec that is root folder exec following command
```
docker-compose up --build
```
### you can see the " 2 " server ( localhost / bridge network)
```
click  on those server links and try the 3 compilers and hit run :)
```
