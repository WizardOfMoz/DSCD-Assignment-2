import grpc
import consistency_pb2
import consistency_pb2_grpc
from concurrent import futures
import sys
import random


SERVERS = []
N,Nw,Nr = 0,0,0


class Server_RegServerService(consistency_pb2_grpc.Server_RegServerServicer):    
    def Register(self,request,context):
        address = request.address
        print(f"Address : {address}")
        SERVERS.append(address)
        return consistency_pb2.ServerRegResponse(success=True)



class Client_RegServerService(consistency_pb2_grpc.Client_RegServerServicer):
    def GetServerList(self, request, context):
        for address in SERVERS:
            yield consistency_pb2.Server(address=address)

    def GetNWServerList(self, request, context):
        server_list = random.sample(SERVERS,Nw)
        for address in server_list:
            yield consistency_pb2.Server(address=address)
    
    def GetNRServerList(self, request, context):
        server_list = random.sample(SERVERS,Nr)
        for address in server_list:
            yield consistency_pb2.Server(address=address)


def run():
    global N,Nw,Nr
    print("Staring Registry Server ...")
    try:
        N,Nw,Nr = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
    except:
        print("Usage: python3 regserver.py <N> <Nw> <Nr>")
        sys.exit(1)
    
    if Nw<=N/2 or (Nw+Nr)<=N or Nw>N or Nr>N:
        print("Invalid Nw and Nr")
        sys.exit(1)
    

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    consistency_pb2_grpc.add_Server_RegServerServicer_to_server(Server_RegServerService(),server)
    consistency_pb2_grpc.add_Client_RegServerServicer_to_server(Client_RegServerService(),server)
    server.add_insecure_port('[::]:8888')
    server.start()
    server.wait_for_termination()

run()
