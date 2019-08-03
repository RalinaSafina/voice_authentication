import numpy


def generate_phrase():
    word_1 = [line.strip() for line in open('C:/Verification/1.txt', 'r')]
    word_2 = [line.strip() for line in open('C:/Verification/2.txt', 'r')]
    phrase = numpy.random.choice(word_1) + " " + numpy.random.choice(word_2)
    f = open('C:/Verification/phrase.txt', 'w')
    f.write(phrase)
    f.close()

generate_phrase()