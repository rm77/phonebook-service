
1. melakukan autentikasi

curl -v http://127.0.0.1:5000/auth -X POST -d '{"username": "leomessi", "password": "kaoskakimerah123"}'

menghasilkan status dan token

{"status":"OK","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imxlb21lc3NpIiwicGFzc3dvcmQiOiJrYW9za2FraW1lcmFoMTIzIiwibmFtYSI6Ikxpb25lbCBNZXNzaSIsImV4cCI6MTU3MzUxNjcxOH0.0IjYzTVyllKXs2Gd6QNZDnZxCujqg2MKrJEPvMa_fOM"}



2. mengakses service dengan menggunakan token, dimasukkan di authorisation header
tanpa authorization header:
curl -v http://127.0.0.1:5000/phonebook/c339df66-04d1-11ea-a7f5-c9aa0ab4e96b
> GET /phonebook/c339df66-04d1-11ea-a7f5-c9aa0ab4e96b HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.65.3
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 35
< Server: Werkzeug/0.16.0 Python/3.7.5rc1
< Date: Mon, 11 Nov 2019 23:49:20 GMT
<
{"STATUS": "Error Authentication"}
* Closing connection 0

dengan authorization header
curl -v http://127.0.0.1:5000/phonebook/c339df66-04d1-11ea-a7f5-c9aa0ab4e96b -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imxlb21lc3NpIiwicGFzc3dvcmQiOiJrYW9za2FraW1lcmFoMTIzIiwibmFtYSI6Ikxpb25lbCBNZXNzaSIsImV4cCI6MTU3MzUxNjcxOH0.0IjYzTVyllKXs2Gd6QNZDnZxCujqg2MKrJEPvMa_fOM"