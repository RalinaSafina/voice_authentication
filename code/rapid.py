import os
import numpy
import scipy.spatial

def countrapid():
    path_to_dir = 'C:/Verification/'
    folder = os.walk(path_to_dir)
    for i in folder:
        if i[1]:
            folders = i[1]
    best_rapid = 0
    best_accuracy = 0
    for rapid in range(0, 100):
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for i in range(0, len(folders)):
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

            for j in range(0, len(folders)):
                path = path_to_dir + folders[j]
                with open(path + '/etalon.txt') as fin:
                    flag = True
                    for line in fin:
                        if flag:
                            process = (line.rstrip('\n')).split(' ')
                            flag = False
                        else:
                            process = numpy.vstack((process, (line.rstrip('\n')).split(' ')))
                    process = process.astype(float)

                for k in range(data.shape[0]):
                    for curr in range(process.shape[0]):
                        dist = scipy.spatial.distance.correlation(data[k], process[curr])
                        if i == j and k != curr and dist < rapid*0.01:
                            TP += 1
                        elif i == j and k != curr and dist > rapid*0.01:
                            FN += 1
                        elif i != j and dist < rapid * 0.01:
                            FP += 1
                        elif i != j and dist > rapid*0.01:
                            TN += 1
        n = TP + TN + FP + FN
        if TP + FP == 0:
            Precision = 0
        else:
            Precision = TP / (TP + FP)
        if Precision > best_accuracy:
            best_accuracy = TP
            best_rapid = rapid
            Accuracy = (TP + TN) / n
            print("TP "+TP.__str__()+" TN "+TN.__str__()+" FP "+FP.__str__()+" FN "+FN.__str__()+" Accuracy "+ \
                  Accuracy.__str__()+" rapid "+rapid.__str__()+" Precision "+Precision.__str__())
    return best_accuracy, best_rapid


accuracy, rapid = countrapid()
print(accuracy)
print(rapid*0.01)
