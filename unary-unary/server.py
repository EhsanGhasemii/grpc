import grpc
import first_pb2
import first_pb2_grpc


from concurrent import futures



class ConversationServicer():
    def Answer(self, request, context):
        print(request)

        words = request.text.split()
        is_index = words.index("am")

        output = words[is_index + 1]
        output = "Hello " + output + " How are you?"

        return first_pb2.AnswerMessage(text = output)


def serve():
    print("Server is ready.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    first_pb2_grpc.add_ConversationServicer_to_server(ConversationServicer(), server)

    server.add_insecure_port('[::]:10000')


    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    serve()
