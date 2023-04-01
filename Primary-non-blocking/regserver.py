import grpc
import consistency_pb2
import consistency_pb2_grpc
from concurrent import futures


SERVERS = []



class Server_RegServerService(consistency_pb2_grpc.Server_RegServerServicer):
    def __init__(self):
        self.PRIMARY_SERVER = None


    def Register(self,request,context):
        address = request.address
        print(f"Address : {address}")
        SERVERS.append(address)
        if self.PRIMARY_SERVER:
            # print("PRIMARY SERVER EXISTS")
            with grpc.insecure_channel(self.PRIMARY_SERVER) as channel:
                stub = consistency_pb2_grpc.RegServer_ServerStub(channel)
                stub.AddReplica(consistency_pb2.Server(address=address))
        else:
            # print("PRIMARY SERVER REGISTERED")
            self.PRIMARY_SERVER = address
        return consistency_pb2.ServerRegResponse(success=True,primary_server=self.PRIMARY_SERVER)



class Client_RegServerService(consistency_pb2_grpc.Client_RegServerServicer):
    def GetServerList(self, request, context):
        for address in SERVERS:
            yield consistency_pb2.Server(address=address)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    consistency_pb2_grpc.add_Server_RegServerServicer_to_server(Server_RegServerService(),server)
    consistency_pb2_grpc.add_Client_RegServerServicer_to_server(Client_RegServerService(),server)
    server.add_insecure_port('[::]:8888')
    server.start()
    server.wait_for_termination()

run()
