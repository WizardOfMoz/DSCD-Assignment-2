import grpc 
import consistency_pb2
import consistency_pb2_grpc
from concurrent import futures
import pandas as pd
import sys
import uuid
from google.protobuf import wrappers_pb2
from google.protobuf import timestamp_pb2
import os
import time
import threading


REPLICAS = []
PRIMARY_SERVER = None
IS_PRIMARY = False
MEMORY_MAP = {}
DIRECTORY = ""


class RegServer_ServerService(consistency_pb2_grpc.RegServer_ServerServicer):

    def AddReplica(self,request,context):
        address = request.address
        print(f"Address : {address}")
        REPLICAS.append(address)
        print(f"REPLICAS : {REPLICAS}")
        return consistency_pb2.Void()
    
        

class Client_ServerService(consistency_pb2_grpc.Client_ServerServicer):
    
    def write_to_replicas(self,request):
        for replica in REPLICAS:
            with grpc.insecure_channel(replica) as channel:
                # time.sleep(2)
                stub = consistency_pb2_grpc.Client_ServerStub(channel)
                response = stub.Write(request)

        
    def delete_from_replicas(self,request):
        for replica in REPLICAS:
            with grpc.insecure_channel(replica) as channel:
                # time.sleep(2)
                stub = consistency_pb2_grpc.Client_ServerStub(channel)
                response = stub.Delete(request)



    def Write(self,request,context):
        name = request.name
        content = request.content
        uuid  = request.uuid
        seq = request.seq
        FILE_PATH = f"{DIRECTORY}/{name}"

        if seq==1:  #write to local replica
            if IS_PRIMARY==True:  #case where local replica is primary 
                seq=2
            
            else:
                with grpc.insecure_channel(PRIMARY_SERVER) as channel:
                    stub = consistency_pb2_grpc.Client_ServerStub(channel)
                    request.seq = 2
                    response = stub.Write(request)
                    return response
            
        if seq == 2:    #write passed to primary replica
            DIR_LIST = os.listdir(DIRECTORY)
            timestamp = pd.to_datetime('now',utc=True).value
            version = pd.to_datetime(timestamp).strftime('%d/%m/%Y %H:%M:%S')
            
            if (uuid not in MEMORY_MAP) and (name in DIR_LIST):   #File with same name already exists
                return consistency_pb2.WriteResponse(status="FILE WITH THE SAME NAME ALREADY EXISTS",uuid=uuid)
            
            
            elif (uuid in MEMORY_MAP) and (name not in DIR_LIST):  #Deleted File
                return consistency_pb2.WriteResponse(status="DELETED FILE CANNOT BE UPDATED",uuid=uuid)

            else:
                create = False
                
                if uuid not in MEMORY_MAP:
                    create = True
                MEMORY_MAP[uuid]=(name,timestamp)
                with open(FILE_PATH,"w") as f:
                    f.write(content)
                
                if create :
                    print(f"File {uuid} created - Version: {version}")
                
                else:
                    print(f"File {uuid} updated - Version: {version}")

                request.seq = 3
                request.timestamp = timestamp
                
                thread = threading.Thread(target=self.write_to_replicas,args=(request,))
                thread.start()
                

                return consistency_pb2.WriteResponse(status="SUCCESS",uuid=uuid,timestamp=timestamp)
             
        if seq == 3:    #File after passing checks in primary replica is written to all replicas
            timestamp = request.timestamp
            version = pd.to_datetime(timestamp).strftime('%d/%m/%Y %H:%M:%S')
            create = False
            
            if uuid not in MEMORY_MAP:
                create = True
            MEMORY_MAP[uuid]=(name,timestamp)    
            
            with open(FILE_PATH,"w") as f:
                f.write(content)

            if create :
                print(f"File {uuid} created - Version: {version}")
            
            else:
                print(f"File {uuid} updated - Version: {version}")

            return consistency_pb2.WriteResponse(status="SUCCESS",uuid=uuid)
        
            
            
    def Read(self,request,context):
        uuid = request.uuid
        if uuid not in MEMORY_MAP:  #File does not exist
            return consistency_pb2.ReadResponse(status="FILE DOES NOT EXIST")
        
        (name,timestamp) = MEMORY_MAP[uuid]
        if name not in os.listdir(DIRECTORY):   #File already deleted
            return consistency_pb2.ReadResponse(status="FILE ALREADY DELETED",timestamp=timestamp)
        
        FILE_PATH = f"{DIRECTORY}/{name}"   #Success
        with open(FILE_PATH,"r") as f:
            content = f.read()
        return consistency_pb2.ReadResponse(status="SUCCESS",name=name,content=content,timestamp=timestamp)
        
        
            

    def Delete(self,request,context):
        seq = request.seq
        if seq==1:  #delete to local replica
            if IS_PRIMARY==True:
                seq=2
            else:
                with grpc.insecure_channel(PRIMARY_SERVER) as channel:
                    stub = consistency_pb2_grpc.Client_ServerStub(channel)
                    request.seq = 2
                    response = stub.Delete(request)
                    return response
            
        if seq == 2:    #delete passed to primary replica
            uuid = request.uuid
            if uuid not in MEMORY_MAP:  #File does not exist
                return consistency_pb2.DeleteResponse(status="FILE DOES NOT EXIST")
            (name,timestamp) = MEMORY_MAP[uuid]
            if name not in os.listdir(DIRECTORY):   #File already deleted
                return consistency_pb2.DeleteResponse(status="FILE ALREADY DELETED")
            
            FILE_PATH = f"{DIRECTORY}/{name}"   #Success
            timestamp = pd.to_datetime('now',utc=True).value
            version = pd.to_datetime(timestamp).strftime('%d/%m/%Y %H:%M:%S')
            os.remove(FILE_PATH)
            MEMORY_MAP[uuid] = ("",timestamp)    
            
            print(f"File {uuid} deleted at {version}")

            request.seq = 3
            request.timestamp = timestamp

            thread = threading.Thread(target=self.delete_from_replicas,args=(request,))
            thread.start()
            
            return consistency_pb2.DeleteResponse(status="SUCCESS",timestamp=timestamp)
        
        if seq ==3: #delete passed to all replicas after passing checks in primary replica
            uuid = request.uuid
            version = pd.to_datetime(request.timestamp).strftime('%d/%m/%Y %H:%M:%S')
            (name,_) = MEMORY_MAP[uuid]
            FILE_PATH = f"{DIRECTORY}/{name}"   #Success
            os.remove(FILE_PATH)
            MEMORY_MAP[uuid] = ("",request.timestamp)

            print(f"File {uuid} deleted at {version}")

            return consistency_pb2.DeleteResponse(status="SUCCESS")
                
         


def run():
    global DIRECTORY
    global PRIMARY_SERVER
    global IS_PRIMARY


    if(len(sys.argv) != 2):
        print("Usage: python server.py <port>")
        exit(1)

    port = sys.argv[1]

    DIRECTORY = f"data/replica_{port}"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY,exist_ok=True)

    address  = f'localhost:{port}'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(f'[::]:{port}')

    channel = grpc.insecure_channel('localhost:8888')
    stub = consistency_pb2_grpc.Server_RegServerStub(channel)
    request = consistency_pb2.Server(address=f'localhost:{port}')
    response = stub.Register(request)
    PRIMARY_SERVER = response.primary_server
    IS_PRIMARY = (PRIMARY_SERVER == address)
    consistency_pb2_grpc.add_Client_ServerServicer_to_server(Client_ServerService(),server)
    if not IS_PRIMARY:
        print("I am a replica")
    
    else:
        print("I am the primary server")
        consistency_pb2_grpc.add_RegServer_ServerServicer_to_server(RegServer_ServerService(),server)
        

    server.start()
    server.wait_for_termination()

run()

