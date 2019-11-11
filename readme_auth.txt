
1. melakukan autentikasi

curl -v http://127.0.0.1:5000/auth -X POST -d '{"username": "leomessi", "password": "kaoskakimerah123"}'


2. mengakses service dengan menggunakan token, dimasukkan di authorisation header
curl -v http://127.0.0.1:5000/phonebook/c339df66-04d1-11ea-a7f5-c9aa0ab4e96b