import speech_recognition as sr

def record():
    r = sr.Recognizer()
    verification_file = 'C:/Verification/verification_file.wav'
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3)
    k = open('C:/Verification/message.txt', 'w')
    g = open('C:/Verification/recognized.txt', 'w')
    f = open('C:/Verification/phrase.txt', 'r')
    phrase = f.read()
    f.close()
    try:
        phrase_recognition = r.recognize_google(audio, language="ru-RU")
        if phrase == phrase_recognition or phrase_recognition in phrase:
            with open(verification_file, "wb") as f:
                f.write(audio.get_wav_data())
            k.write('Фраза произнесена верно')
            g.write('True')
            k.close()
            g.close()
        else:
            k.write('Произнесенная фраза неверна!')
            g.write('False')
            k.close()
            g.close()

    # error occurs when google could not understand what was said
    except sr.UnknownValueError:
        k.write('Фраза не распознана Google Speech Recognition')
        g.write('False')
        k.close()
        g.close()
    except sr.RequestError as e:
        k.write('Невозможно получить ответ от сервиса Google Speech Recognition; Проверьте подключение к интернету')
        g.write('False')
        k.close()
        g.close()


record()
