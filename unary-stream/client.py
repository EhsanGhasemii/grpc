import grpc
import second_pb2
import second_pb2_grpc
import io 
from pydub import AudioSegment
from pydub.playback import play

remote_add = 'localhost:10000'
data_add = '../data/song.mp3'

def main():
    channel = grpc.insecure_channel(remote_add)
    client = second_pb2_grpc.PlayMusicStub(channel)

    MusicRequest = second_pb2.MusicRequest(audio_name = data_add)
    MusicResponse = client.Play(MusicRequest)

    # Read the response stream and concatenate the data
    audio_data = io.BytesIO()
    for response in MusicResponse: 
        audio_data.write(response.audio_data)

    # Decode and play the audio
    audio_data.seek(0)
    audio_segment = AudioSegment.from_file(audio_data, format="mp3")
    play(audio_segment)
    

if __name__ == '__main__':
    main()
