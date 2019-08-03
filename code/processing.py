import speech_recognition as sr
import os
import audio_proc
import numpy

def registration():
    how_to_say = ['НОРМАЛЬНО', 'БЫСТРО', 'МЕДЛЕННО', 'ТИХО', 'ГРОМКО']

    name = input("Введите имя: ")
    path = 'C:/Verification/' + name
    os.mkdir(path)

    for i in range(0, len(how_to_say)):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Произнесите фразу " + how_to_say[i] + ": ЗЕЛЕНАЯ ТРАВА")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        path_to_write = path + "/filename" + (i + 1).__str__() + ".wav"
        with open(path_to_write, "wb") as f:
            f.write(audio.get_wav_data())
        if i == 0:
            array = audio_proc.mfcc(path_to_write)
        else:
            array = numpy.vstack((array, audio_proc.mfcc(path_to_write)))

    numpy.savetxt(path + '/etalon.txt', array)

registration()

'''with sr.WavFile("filename2.wav") as source:
        audio = r.record(source)

with open("filename6.wav", "wb") as f:
    f.write(audio.get_wav_data())

phrase = r.recognize_google(audio, language="ru-RU")
print(phrase)'''


