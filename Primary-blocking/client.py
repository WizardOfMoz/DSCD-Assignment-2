import grpc
import consistency_pb2
import consistency_pb2_grpc
from concurrent import futures
import uuid
import pandas as pd
import random



channel = grpc.insecure_channel('localhost:8888')
stub = consistency_pb2_grpc.Client_RegServerStub(channel)
SERVER_LIST = list(stub.GetServerList(consistency_pb2.Void()))
# print("SERVER LIST:")
# for i,server in enumerate(SERVER_LIST):
#     print(f"{i+1}. {server.address}")

# i = int(input("Enter the server number: "))
# address = SERVER_LIST[i-1].address
address = random.choice(SERVER_LIST).address

print(f"Connected to {address}")
channel = grpc.insecure_channel(address)
stub = consistency_pb2_grpc.Client_ServerStub(channel)


while True:
    print("1. Write")
    print("2. Read")
    print("3. Delete")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_record = input("Do you want to create New Record?(Y/N): ")
        if new_record.lower()=='y':
            UUID = str(uuid.uuid4())
        else:
            UUID = input("Enter the UUID: ")
        
        name = input("Enter the name: ")
        content = input("Enter the content: ")

        request = consistency_pb2.WriteRequest(uuid=UUID,name=name,content=content,seq=1)
        response = stub.Write(request)
        if response.status == "SUCCESS":
            version = pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
            print(f"Status : {response.status}\nUUID : {response.uuid}\nVersion : {version}")
        else:
            print(f"Status : {response.status}")
    
    elif choice == 2:
        UUID = input("Enter the UUID: ")
        request = consistency_pb2.ReadRequest(uuid=UUID)
        response = stub.Read(request)
        if response.status == "FILE DOES NOT EXIST":
            print(f"Status : {response.status}")
        
        elif response.status == "FILE ALREADY DELETED":
            version = pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
            print(f"Status : {response.status}\nVersion : {version}")
        
        else:   #success
            version = pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
            print(f"Status : {response.status}\nName : {response.name}\nContent : {response.content}\nVersion : {version}")
        
    
    elif choice == 3:
        UUID = input("Enter the UUID: ")
        request = consistency_pb2.DeleteRequest(uuid=UUID,seq=1)
        response = stub.Delete(request)
        print(f"Status : {response.status}")
        if response.status == "SUCCESS":
            version = pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
            print(f"Version : {version}")
    
    else:
        break



