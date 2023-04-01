import grpc
import consistency_pb2
import consistency_pb2_grpc
from concurrent import futures
import uuid
import pandas as pd



channel = grpc.insecure_channel('localhost:8888')
reg_stub = consistency_pb2_grpc.Client_RegServerStub(channel)

while True:
    print("1. Write")
    print("2. Read")
    print("3. Delete")
    print("4. Get Replica List")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_record = input("Do you want to create New Record?(Y/N): ")
        if new_record.lower()=='y':
            UUID = str(uuid.uuid4())
        else:
            UUID = input("Enter the UUID: ")
        
        name = input("Enter the name: ")
        content = input("Enter the content: ")
        response = reg_stub.GetNWServerList(consistency_pb2.Void())
        server_list = [server.address for server in response]

        for server in server_list:
            channel = grpc.insecure_channel(server)
            stub = consistency_pb2_grpc.Client_ServerStub(channel)
            request = consistency_pb2.WriteRequest(uuid=UUID,name=name,content=content)
            response = stub.Write(request)
            print(f"SERVER: {server}")
            if response.status == "SUCCESS":
                version = pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
                print(f"Status : {response.status}\nUUID : {response.uuid}\nVersion : {version}")
            
            else:
                print(f"Status : {response.status}")
        

    
    if choice == 2:
        UUID = input("Enter the UUID: ")
        response = reg_stub.GetNRServerList(consistency_pb2.Void())
        server_list = [server.address for server in response]

        latest_response = None
        for server in server_list:
            channel = grpc.insecure_channel(server)
            stub = consistency_pb2_grpc.Client_ServerStub(channel)
            response = stub.Read(consistency_pb2.ReadRequest(uuid=UUID))
            print(f"server:{server}, status:{response.status}, version : {pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')}")
            if response.status == "FILE DOES NOT EXIST":
                continue
            if not latest_response:
                latest_response = response

            elif response.timestamp > latest_response.timestamp:
                latest_response = response
        
        if latest_response:
            version = pd.to_datetime(latest_response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
            if latest_response.status == "FILE ALREADY DELETED":
                print(f"Status : {latest_response.status}\nVersion : {version}")
            else:
                print(f"Status : {latest_response.status}\nName : {latest_response.name}\nContent : {latest_response.content}\nVersion : {version}")
        
        else:
            print("FILE DOES NOT EXIST")
        
            
    if choice == 3:
        UUID = input("Enter the UUID: ")
        response = reg_stub.GetNWServerList(consistency_pb2.Void())
        server_list = [server.address for server in response]

        latest_response = None
        for server in server_list:
            channel = grpc.insecure_channel(server)
            stub = consistency_pb2_grpc.Client_ServerStub(channel)
            response = stub.Delete(consistency_pb2.DeleteRequest(uuid=UUID))
            print(f"SERVER: {server}")
            print(f"Status : {response.status}")
            if response.status == "SUCCESS":
                version = pd.to_datetime(response.timestamp).strftime('%Y/%m/%d %H:%M:%S')
                print(f"Version : {version}")
        
    
    if choice == 4:
        print()
        print("Replica List: ")
        response = reg_stub.GetServerList(consistency_pb2.Void())
        for i,server in enumerate(response):
            print(f"{i+1}. {server.address}")
        
        print()
    
    if choice == 5:
        break


    



