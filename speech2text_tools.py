import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


from pydub import AudioSegment
from pydub.playback import play


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/alternator/Documents/programs/key.json"
client = speech.SpeechClient()


def mp3_to_wav():
    try:
        filepath = str(input("Enter Your File .mp3 Path.\n Ex. /home/alternator/Documents/programs/speech2text/ALCPT51.mp3\n:"))
        file_name = str(input("Enter File Name. \n Ex. test.wav\n:"))
        new_wav = AudioSegment.from_mp3(filepath)
        new_wav.set_channels(1)
        new_wav.export(file_name, format="wav")
        return ("Change mp3 to wav Success!!!!!!")
    except:
        return ("Please Enter Correct Forms. :(")
                                                         

def sliceaudio(filepath,time_start,time_stop):
 
    try:
        audio = AudioSegment.from_wav(str(filepath))
        audio =  audio[float(time_start)*1000:float(time_stop)*1000]
        audio.export("audio_sliced"+time_start+"_to_"+time_stop+".wav", format="wav")
        return ("Slice Audio Success!!!!")
    except:
        return ("Please Enter Correct Forms. :(")


def audio2text(file_name):
    
    file_name = str(file_name)
    try:
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=44100,
                language_code='en-US')
            try:
                response = client.recognize(config, audio)

                f = open(file_name+"_trans"+".txt", "w")
                for result in response.results:
                    f.write('{}\n'.format(result.alternatives[0].transcript))
                    
                f.close()
                f = open(file_name+"_trans"+".txt", "r")
                return (f.read())    

            except OSError as err:
                return err
    except:
        return ("Cannot OpenFile")


def play_audio(filepath):
    try:
        audio = AudioSegment.from_wav(str(filepath))
        play(audio)
    except:
        print("Cannot this audio!!!!")