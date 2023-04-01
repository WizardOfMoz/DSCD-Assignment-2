import grpc 
import consistency_pb2
import consistency_pb2_grpc
from concurrent import futures
import pandas as pd
import sys
import uuid

import os
import time


MEMORY_MAP = {}
DIRECTORY = ""

class Client_ServerService(consistency_pb2_grpc.Client_ServerServicer):
    
    def Write(self,request,context):
        name = request.name
        content = request.content
        uuid  = request.uuid
        FILE_PATH = f"{DIRECTORY}/{name}"
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

            if create:
                print(f"File {uuid} created - Version: {version}") 
            else:
                print(f"File {uuid} updated - Version: {version}")

            return consistency_pb2.WriteResponse(status="SUCCESS",uuid=uuid,timestamp=timestamp)
                    
        
            
            
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
        uuid = request.uuid
        timestamp = pd.to_datetime('now',utc=True).value
        version = pd.to_datetime(timestamp).strftime('%d/%m/%Y %H:%M:%S')
        if uuid not in MEMORY_MAP:  #File does not exist
            MEMORY_MAP[uuid] = ("",timestamp)
            print(f"File {uuid} deleted at {version}")
            return consistency_pb2.DeleteResponse(status="FILE DOES NOT EXIST",timestamp=timestamp)        
        
        (name,_) = MEMORY_MAP[uuid]
        if name not in os.listdir(DIRECTORY):   #File already deleted
            return consistency_pb2.DeleteResponse(status="FILE ALREADY DELETED")
        
        FILE_PATH = f"{DIRECTORY}/{name}"   #Success
        os.remove(FILE_PATH)
        MEMORY_MAP[uuid] = ("",timestamp)    
    
        print(f"File {uuid} deleted at {version}")
        

        return consistency_pb2.DeleteResponse(status="SUCCESS",timestamp=timestamp)
        
                
         


def run():
    global DIRECTORY
    if(len(sys.argv) != 2):
        print("Usage: python server.py <port>")
        exit(1)

    port = sys.argv[1]
    # print("Server running on port",port)
    DIRECTORY = f"data/replica_{port}"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY,exist_ok=True)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(f'[::]:{port}')

    channel = grpc.insecure_channel('localhost:8888')
    stub = consistency_pb2_grpc.Server_RegServerStub(channel)
    request = consistency_pb2.Server(address=f'localhost:{port}')
    stub.Register(request)
    
    consistency_pb2_grpc.add_Client_ServerServicer_to_server(Client_ServerService(),server)
    server.start()
    server.wait_for_termination()

run()

