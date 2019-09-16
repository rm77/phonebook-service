from concurrent import futures
import grpc
import time
from Phonebook_Model import *
import phonebook_pb2
import phonebook_pb2_grpc
import json


phonebook_model = Phonebook_Model()

class Phonebook_Service(phonebook_pb2_grpc.PhonebookServicer):
    def __init__(self):
        pass
    def GetDataById(self, request, context):
        id = request.key
        pbdata = phonebook_model.get(id)
        hasil = dict(data=pbdata)
        print(id,pbdata)
        return phonebook_pb2.Response(value=json.dumps(hasil))
    def GetDataAll(self, request, context):
        pbdata = phonebook_model.list()
        for d in pbdata:
            hasil = dict(id=d,data=pbdata[d])
            yield phonebook_pb2.Response(value=json.dumps(hasil))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    phonebook_pb2_grpc.add_PhonebookServicer_to_server(Phonebook_Service(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    serve()

