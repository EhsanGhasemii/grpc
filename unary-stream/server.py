import grpc 
import second_pb2
import second_pb2_grpc

from concurrent import futures


class PlayMusicServicer():
    def Play(self, Request, context):

        with open(Request.audio_name, 'rb') as f:
            while True: 
                data = f.read(1024)
                print(data)
                if not data:
                    break
                print(data)
                print('-' * 30)
                yield second_pb2.MusicResponse(audio_data = data)

        #try:
        #    with open(Request.audio_name, 'rb') as f:
        #        while True:
        #            data = f.read(1024)  # Adjust buffer size as needed
        #            if not data:
        #                break
        #            yield second_pb2.MusicResponse(audio_data=data)
        #except FileNotFoundError:
        #    context.set_code(grpc.StatusCode.NOT_FOUND)
        #    context.set_details(f'ReadRequest: resource {request.resource_name} doesn\'t exist')
        #    return bytestream_pb2.ReadResponse()




def serve():
    print("Server is ready.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    second_pb2_grpc.add_PlayMusicServicer_to_server(PlayMusicServicer(), server)

    server.add_insecure_port('[::]:10000')

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':

    serve()
