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

    def __init__(self):
        self.block = False

    def block_replicas(self):
        for replica in REPLICAS:
            with grpc.insecure_channel(replica) as channel:
                stub = consistency_pb2_grpc.Client_ServerStub(channel)
                stub.Block(consistency_pb2.Void())
    
    def unblock_replicas(self):
        for replica in REPLICAS:
            with grpc.insecure_channel(replica) as channel:
                stub = consistency_pb2_grpc.Client_ServerStub(channel)
                stub.Unblock(consistency_pb2.Void())

    
    def Write(self,request,context):
        name = request.name
        content = request.content
        uuid  = request.uuid
        seq = request.seq
        FILE_PATH = f"{DIRECTORY}/{name}"

        if seq==1:  #write to local replica
            if self.block:
                return consistency_pb2.WriteResponse(status="BLOCKED")
            
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
            
            if (uuid not in MEMORY_MAP) and (name in DIR_LIST):   #File with same name already exists
                return consistency_pb2.WriteResponse(status="FILE WITH THE SAME NAME ALREADY EXISTS",uuid=uuid)
            
            
            elif (uuid in MEMORY_MAP) and (name not in DIR_LIST):  #Deleted File
                return consistency_pb2.WriteResponse(status="DELETED FILE CANNOT BE UPDATED",uuid=uuid)

            else:
                self.block=True
                if uuid not in MEMORY_MAP:
                    MEMORY_MAP[uuid]=(name,timestamp)
                with open(FILE_PATH,"w") as f:
                    f.write(content)
                request.seq = 3
                request.timestamp = timestamp
                self.block_replicas()
                for replica in REPLICAS:
                    with grpc.insecure_channel(replica) as channel:
                        stub = consistency_pb2_grpc.Client_ServerStub(channel)
                        response = stub.Write(request)
                time.sleep(20)
                self.unblock_replicas()
                self.block=False

                return consistency_pb2.WriteResponse(status="SUCCESS",uuid=uuid,timestamp=timestamp)
             
        if seq == 3:    #File after passing checks in primary replica is written to all replicas
            timestamp = request.timestamp
            if uuid not in MEMORY_MAP:
                MEMORY_MAP[uuid]=(name,timestamp)
            
            with open(FILE_PATH,"w") as f:
                f.write(content)
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
            if self.block:
                return consistency_pb2.DeleteResponse(status="BLOCKED")
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
            
            self.block=True   
            FILE_PATH = f"{DIRECTORY}/{name}"   #Success
            timestamp = pd.to_datetime('now',utc=True).value
            os.remove(FILE_PATH)
            MEMORY_MAP[uuid] = ("",timestamp)    
            self.block_replicas()
            
            for replica in REPLICAS:
                with grpc.insecure_channel(replica) as channel:
                    stub = consistency_pb2_grpc.Client_ServerStub(channel)
                    request.seq = 3
                    request.timestamp = timestamp
                    response = stub.Delete(request)
            time.sleep(20)
            self.unblock_replicas()
            self.block=False
            
            return consistency_pb2.DeleteResponse(status="SUCCESS",timestamp=timestamp)
        
        if seq ==3: #delete passed to all replicas after passing checks in primary replica
            uuid = request.uuid
            (name,_) = MEMORY_MAP[uuid]
            FILE_PATH = f"{DIRECTORY}/{name}"   #Success
            os.remove(FILE_PATH)
            MEMORY_MAP[uuid] = ("",request.timestamp)
            return consistency_pb2.DeleteResponse(status="SUCCESS")

    def Block(self,request,context):
        self.block=True
        return consistency_pb2.Void()
    
    def Unblock(self,request,context):
        self.block=False
        return consistency_pb2.Void()


        
        
                


         


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

