import os 
import pandas as pda
from pydub import AudioSegment
from gtts import gTTS

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios :
        combined += AudioSegment.from_mp3(audio)
    return combined

def textToSpeech(text, filename):
     mytext = str(text)
     language = 'en-in'
     myobj = gTTS(text = mytext, lang = language, slow = False)
     myobj.save(filename)


def generateSkeleton():
    audio = AudioSegment.from_mp3('Announcement.mp3')
    #1 may i have your attention please 
    start = 17000
    finish = 19000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_English.mp3", format = "mp3")
    #2 train no
    #3train name
    #4from
    start = 23200
    finish = 23700
    audioProcessed = audio[start:finish]
    audioProcessed.export("4_English.mp3", format = "mp3")
    #5varanasi jn

    #6via
    start = 25000
    finish = 25580
    audioProcessed = audio[start:finish]
    audioProcessed.export("6_English.mp3", format = "mp3")
    #7pratapgahr
    #8 lucknow

    # 9is arrving on platform no 
    start = 26800
    finish = 29495
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_English.mp3", format = "mp3")
    #10no

def generateAnnouncement(filename):
    ex = pda.read_excel(filename)
    print(ex)
    for index, item in ex.iterrows():
        #2train no
         textToSpeech(item['tain_no'], '2_English.mp3')
         #3train name
         textToSpeech(item['train_name'], '3_English.mp3')
         #5 Varanasi jn
         textToSpeech(item['from'], '5_English.mp3')
         #7 pratapgahr
         textToSpeech(item['via'], '7_English.mp3')
         #8lucknow
         textToSpeech(item['to'], '8_English.mp3')
         #10 platform no
         textToSpeech(item['platform'], '10_English.mp3')

         audios = [f"{i}_English.mp3" for i in range(1,11)]

         announcement = mergeAudios(audios)
         announcement.export(f"announcement_{item['tain_no']}_{index+1}.mp3",format = "mp3")


    

if __name__ == "__main__":
    print("Generating Skeleton.....")
    generateSkeleton()
    print("Now , generating skeleton.....")
    generateAnnouncement("train_annouce.xlsx")