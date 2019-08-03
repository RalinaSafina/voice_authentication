import speech_recognition as sr
import os
import numpy
import audio_proc
import math
import scipy.spatial

def verify():
    #data = numpy.genfromtxt('C:/Verification/Karina/etalon.txt', delimiter='\n', dtype=numpy.float)
    #data = audio_proc.mfcc('C:/Verification/Karina/filename1.wav')
    #process = numpy.loadtxt('C:/Verification/Karina/etalon.txt', delimiter='\n', dtype=numpy.float)
    with open('C:/Verification/etalon/etalon.txt') as fin:
        i = True
        for line in fin:
            if i:
                data = (line.rstrip('\n')).split(' ')
                i = False
            else:
                data = numpy.vstack((data, (line.rstrip('\n')).split(' ')))
        data = data.astype(float)
    process = audio_proc.mfcc('C:/Verification/Kamilya/filename3.wav')
    mark = 0.0
    for i in range(data.shape[0]):
        dist = scipy.spatial.distance.euclidean(data[i], process)
        print(dist)
    '''CBD = 0  # city block distance
        for j in range(0, len(process)):
            CBD += math.fabs(data[i][j] - process[j])
        mark += CBD
    for i in range(data.shape[0]):
        mark = numpy.linalg.norm(data[i, ] - process)
    mark /= data.shape[0]
    print(mark)
    process = process - max(process)
    for i in range(data.shape[0]):
        data[i, ] = data[i, ] - max(data[i, ])
        mark = numpy.linalg.norm(data[i, ] - process)
    mark /= data.shape[0]
    print(mark)'''

verify()