menjalankan program
------------------------
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python Phonebook_Service.py

#testing
-mendapatkan seluruh record
    curl -v http://localhost:5000/person
-cek id - c7799c94-d897-11e9-9f2a-6480995fff24
    curl -v http://localhost:5000/person/c7799c94-d897-11e9-9f2a-6480995fff24



#Membangun virtualized & isolated environment dengan docker
#install docker terlebih dahulu, di ubuntu hal ini bisa dilakukan dengan apt install docker.io
#phonebook_service telah diupdate untuk menyediakan info tentang service di /info yang nantinya mengeluarkan info tentang uname dari system

1. bukalah tab terminal
   sudo docker build -t phonebook-docker-1:1.0 .

   jangan lupa ada . untuk menandakan lokasi Dockerfile
   phonebook-docker-1 merupakan nama image yang nantinya akan dijalankan sebagai container dengan tag versi 1.0
   image dibangun dengan menggunakan file Dockerfile yang berisikan urutan perintah mulai instalasi sampai mengcopy file-file yang dibutuhkan.

2. lihatlah daftar images yang ada dan pastikan phonebook-docker-1:1.0 ada dalam daftar tersebut
   sudo docker images

3. jalankan images tersebut untuk menjadi container
   a. jalankan di port 7777 dengan nama phonebook-container-7777
   sudo docker run -d -p 7777:5000 --name phonebook-container-7777 phonebook-docker-1:1.0
   b. jalankan di port 7772
   sudo docker run -d -p 7772:5000 --name phonebook-container-7772 phonebook-docker-1:1.0

   masing-masing container yang berjalan adalah sebuah proses, akseslah service pada container yang relevan dengan nomor portnya
   curl -v http://localhost:7777/person  --> mengakses service person yang ada di phonebook-container-7777
   curl -v http://localhost:7772/person  --> mengakses service person yang ada di phonebook-container-7772
   curl -v http://localhost:7777/info  --> mengakses service info yang ada di phonebook-container-7777
   curl -v http://localhost:7772/info  --> mengakses service info yang ada di phonebook-container-7772

   cobalah untuk menjalankan service phonebook di port 7770,7771,7772,7773,7774,7775,7776,7777,7778,7779,7780


4. untuk menstop sebuah container
   sudo docker rm -f <containerid>
   contoh: untuk menghentikan container phonebook-container-7777
   sudo docker rm -f phonebook-container-7777

5. untuk menghapus image dari docker images
   sudo docker rmi -f <imageid>
   contoh: menghapus image phonebook-docker-1:1.0
   sudo docker rmi -f phonebook-docker-1:1.0




