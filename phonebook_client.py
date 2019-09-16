import grpc
import phonebook_pb2
import phonebook_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = phonebook_pb2_grpc.PhonebookStub(channel)
        for x in stub.GetDataAll(phonebook_pb2.Request(key='')):
            print(x)
        print(stub.GetDataById(phonebook_pb2.Request(key='456')))



if __name__ == "__main__":
    run()
