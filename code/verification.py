import speech_recognition as sr
import os
import numpy
import audio_proc
import scipy


def verify():
    r = sr.Recognizer()
    verification_file = 'C:/Verification/verification_file.wav'
    word_1 = [line.strip() for line in open('C:/Verification/1.txt', 'r')]
    word_2 = [line.strip() for line in open('C:/Verification/2.txt', 'r')]
    phrase = numpy.random.choice(word_1) + " " + numpy.random.choice(word_2)
    with sr.Microphone() as source:
        print("Произнесите фразу: " + phrase)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=5)
    print("Запись остановлена")
    try:
        phrase_recognition = r.recognize_google(audio, language="ru-RU")

        if phrase == phrase_recognition:
            with open(verification_file, "wb") as f:
                f.write(audio.get_wav_data())


            process = audio_proc.mfcc(verification_file)
            path_to_dir = 'C:/Verification/'
            folder = os.walk(path_to_dir)

            for i in folder:
                if i[1]:
                    folders = i[1]

            rapid = 0.5
            name = ''
            verified = False
            compare = float(numpy.inf)
            temp = 1
            for i in range(0, len(folders)):
                help = False
                path = path_to_dir + folders[i]
                with open(path + '/etalon.txt') as fin:
                    flag = True
                    for line in fin:
                        if flag:
                            data = (line.rstrip('\n')).split(' ')
                            flag = False
                        else:
                            data = numpy.vstack((data, (line.rstrip('\n')).split(' ')))
                    data = data.astype(float)

                for k in range(data.shape[0]):
                    dist = scipy.spatial.distance.correlation(data[k], process)
                    #print(folders[i] + " " + dist.__str__())
                    if dist < rapid:
                        help = True
                    if dist < temp:
                        temp = dist
                if help and temp < compare:
                    name = folders[i]
                    compare = temp
                    print(name + " " + temp.__str__())
                    verified = True

            if verified:
                print('Привет, ' + name)
            else:
                print('Вы не были распознаны!')
        else:
            print('Произнесенная фраза неверна либо не распознана!')

    # error occurs when google could not understand what was said
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

verify()