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



membuat isolated environment dengan menggunakan vagrant dan virtualbox

- install terlebih dahulu
  - vagrant : apt install vagrant
  - virtualbox : apt install virtualbox


- vagrant up
- vagrant ssh control



