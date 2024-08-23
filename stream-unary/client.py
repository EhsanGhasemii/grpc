import grpc
import third_pb2
import third_pb2_grpc



remote_addr = 'localhost:10000'
data_addr = '../data/song.mp3'


def StreamTheMusic(data_addr):
    with open(data_addr, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            else:
                yield third_pb2.MusicRequest(audio=data)

def main():

    channel = grpc.insecure_channel(remote_addr)
    client = third_pb2_grpc.ListenTheMusicStub(channel)

    MusicRequest = StreamTheMusic(data_addr)
    MusicResponse = client.Listen(MusicRequest)

    print(MusicResponse)

if __name__ == '__main__':
    main()
