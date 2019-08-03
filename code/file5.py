import speech_recognition as sr


def registration():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    path_to_write = 'C:/Verification/new_user/filename5.wav'
    with open(path_to_write, "wb") as f:
        f.write(audio.get_wav_data())

registration()