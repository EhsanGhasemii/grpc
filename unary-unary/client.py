import grpc
import first_pb2
import first_pb2_grpc


remote_add = "localhost:10000"


def main():
    channel = grpc.insecure_channel(remote_add)
    client = first_pb2_grpc.ConversationStub(channel)
    
    AskMessage = first_pb2.AskMessage(text = "Hello, I am Ehsan.")
    AnswerMessage = client.Answer(AskMessage)

    print("AskMessage: ", AskMessage)
    print("AnswerMessage: ", AnswerMessage)




if __name__ == '__main__':
    main()
