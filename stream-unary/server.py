import grpc
import third_pb2
import third_pb2_grpc

from concurrent import futures

class ListenTheMusicServicer():
    def Listen(self, request, context):
        return third_pb2.MusicResponse(response="The music was fantastic.")


def serve():
    print('Server is Ready.')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    third_pb2_grpc.add_ListenTheMusicServicer_to_server(ListenTheMusicServicer(), server)

    server.add_insecure_port('[::]:10000')

    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    serve()
