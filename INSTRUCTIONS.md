To run the application:

docker-compose up

(or) 

docker build --tag python-docker .

pass the secret key,access key & table name as env variable to docker run command as follows docker run -p 5000:5000 -e aws_access_key_id='' -e aws_secret_access_key='' -e USERS_TABLE='' -d python-docker
