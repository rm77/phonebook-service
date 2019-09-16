menjalankan program
------------------------
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

1. definisikan dahulu service di phonebook.proto
2. generate code rpc sbb:
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. phonebook.proto
