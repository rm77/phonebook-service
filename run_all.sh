#hanya untuk dijalankan di komputer yang sama
sudo docker rm -f myredis_db ; sudo docker run  --name myredis_db -p 0.0.0.0:6379:6379  -v $(pwd)/redisdata:/data -d redis
#0.0.0.0 akan membuat redis dibinding ke ip address local
#cek dengan ifconfig


#jika container image phonebook-docker-2:1.0 sudah tersedia
#maka banyak container bisa dijalankan di port yang berbeda beda
REDISADDR="10.151.62.58"
sudo docker rm -f p1 ; sudo docker run --name p1 -p 9991:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
sudo docker rm -f p2 ; sudo docker run --name p2 -p 9992:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
sudo docker rm -f p3 ; sudo docker run --name p3 -p 9993:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
sudo docker rm -f p4 ; sudo docker run --name p4 -p 9994:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0

# dan seterusnya
#cek dengan docker ps --all