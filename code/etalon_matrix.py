import os
import audio_proc
import numpy


def features():
    path = 'C:/Verification/new_user'
    person = os.walk(path)
    for j in person:
        print(j)
        for file in j[2]:
            if file == 'filename1.wav':
                temp = audio_proc.mfcc(j[0] + '/' + file)
            else:
                temp = numpy.vstack((temp, audio_proc.mfcc(j[0] + '/' + file)))
        numpy.savetxt(j[0] + '/etalon.txt', temp)


features()
