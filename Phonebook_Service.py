from flask import Flask,request,jsonify,make_response
from flask_restful import Resource, Api, reqparse
import json
import os

from Phonebook_Model import *
phonebook_model = Phonebook_Model()

#from Phonebook_Model_redis import *
#redis_addr = os.getenv("REDISADDR") or "localhost"
#waktu jalan dalam container akan menggunakan environemtn variable REDISADDR sebagai parameter lokasi redis server
#phonebook_model = Phonebook_Model(address=redis_addr)

application = Flask(__name__)
api = Api(application)



from Auth_Model import *
class Auth(Resource):
	def post(self):
		data = request.get_json(force=True)
		username = data['username']
		password = data['password']
		a_model = Auth_Model()
		auth_result = a_model.login(username,password)
		if (auth_result is not None):
			return jsonify(status='OK',token=auth_result.decode())
		else:
			return jsonify(status='ERROR',token=None)
	def get(self,token=''):
		if (token==''):
			return jsonify(status='ERROR')
		a_model = Auth_Model()
		auth_result = a_model.cek_token(token)
		if (auth_result is not None):
			return jsonify(status='OK',token=auth_result)
		else:
			return jsonify(status='ERROR')

class Phonebook_Service(Resource):
    def auth_cek(self):
        token = request.headers.get('Authorization') or ''
        cek = Auth_Model().cek_token(token)
        if (cek is None):
            return {'STATUS': 'Error Authentication'}
        return None


    def get_resp(self,pb_data):
        status = 'ERROR' if pb_data == False else 'OK'
        http_code = 404 if pb_data == False else 200
        return status,http_code
    #read -->
    def get(self,id=''):
        if (self.auth_cek() is not None):
            return self.auth_cek(),404

        if (id==''):
            #jika parameter id tidak ada, diasumsikan retrieve semua
            pb_data = phonebook_model.list()
        else:
            #jika ada parameter id, ambil data secara spesifik pada id tersebut
            pb_data = phonebook_model.get(id)

        status, http_code = self.get_resp(pb_data)
        return dict(status=status,data=pb_data),http_code
    def post(self):
        self.auth_cek()

        args = request.get_json(force=True)
        pb_data = phonebook_model.add(args)
        status, http_code = self.get_resp(pb_data)
        return dict(status=status,data=pb_data),http_code
    def delete(self,id=''):
        self.auth_cek()

        if (id==''):
            pb_data=False
        else:
            pb_data = phonebook_model.remove(id)
        status, http_code = self.get_resp(pb_data)
        return dict(status=status,data=pb_data),http_code



api.add_resource(Phonebook_Service,'/phonebook','/phonebook/<id>')
api.add_resource(Auth,'/auth')


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('',5000),application)
    http_server.serve_forever()


