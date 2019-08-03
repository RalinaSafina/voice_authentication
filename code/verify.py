import os
import numpy
import audio_proc
import scipy


def verify():
    process = audio_proc.mfcc('C:/Verification/verification_file.wav')
    path_to_dir = 'C:/Verification/'
    folder = os.walk(path_to_dir)

    for i in folder:
         if i[1]:
              folders = i[1]

    rapid = 0.4
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
            else:
                help = False
            if dist < temp:
                temp = dist
        if help and temp < compare:
            name = folders[i]
            compare = temp
            print(name + " " + temp.__str__())
            verified = True

    if verified:
        f = open('C:/Verification/verified.txt', 'w')
        f.write("True")
        f.close()
        f = open('C:/Verification/name.txt', 'w')
        f.write(name)
        f.close()
    else:
        f = open('C:/Verification/verified.txt', 'w')
        f.write("False")
        f.close()

verify()