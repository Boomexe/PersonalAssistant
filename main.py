print("Loading packages")
import speech_recognition as sr

from gtts import gTTS
# import pyaudio
# from pydub import AudioSegment
# import wave

import playsound

import random
import json
import torch

from train.model import NeuralNet
from utils.preprocessing import bag_of_words
from utils.tokenization import tokenize

print("Loading modules")
import modules.modules as modules
modules.find_modules()

print("Loading model")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('data/intents.json', 'r') as f:
    intents = json.load(f)

FILE = 'models/data.pth'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()
print("Loaded.")

listener = sr.Recognizer()

CHUNK = 1024 # For audio

bot_name = 'Phantom'
print(f'Hi I\'m {bot_name}. Let\'s chat!')

while True:
    sentence = input('You: ')

    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # print(f"probability: {prob.item()}")
    if prob.item() > 0.85:
        for intent in intents['intents']:
            if tag == intent['tag']:
                response = random.choice(intent["responses"])
                if "{" in response and "}" in response:
                    response = modules.load_module(response.strip("{").strip("}"), sentence)
                                          
                print(f'{bot_name}: {response}')
                tts = gTTS(response)
                tts.save("out/out.mp3")

                # playsound.playsound("out.mp3")

                # audio = AudioSegment.from_mp3("D:\Python Documents\VoiceAssistant\out\out.mp3")
                # audio.export("out/out.wav", format="wav")
                
                # time.sleep(1)
                # with wave.open("out/out.wav", 'rb') as wf:
                #     p = pyaudio.PyAudio()
                #     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                #                     channels=wf.getnchannels(),
                #                     rate=wf.getframerate(),
                #                     output=True)
                
                #     while len(d := wf.readframes(CHUNK)):
                #         stream.write(d)
                    
                #     stream.stop_stream()
                #     stream.close()
                #     p.terminate()

    
    else:
        print(f'{bot_name}: I do not understand...')