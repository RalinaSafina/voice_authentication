import numpy
import scipy.io.wavfile
from scipy.fftpack import dct #discrete cosine transform
import math
import os

def mfcc(path_to_file):
    pre_emphasis = 0.97 #can be equal to 0.95
    frame_size = 0.025
    frame_stride = 0.01
    NFFT = 512
    nfilt = 40
    num_ceps = 12
    cep_lifter = 1+(23/2)*math.sin(12*math.pi/23)

    sample_rate, data = scipy.io.wavfile.read(path_to_file)
    data = data[int(0.3 * sample_rate): int(0.6 * sample_rate)]

    #Pre-Emphasis
    emphasized_signal = numpy.append(data[0], data[1:] - pre_emphasis * data[:-1])
    if(len(emphasized_signal) > sample_rate):
        emphasized_signal = emphasized_signal[:sample_rate]


    #Framing
    frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate  # Convert from seconds to samples
    signal_length = len(emphasized_signal)
    frame_length = int(round(frame_length))
    frame_step = int(round(frame_step))
    num_frames = int(numpy.ceil(float(numpy.abs(signal_length - frame_length)) / frame_step))  # Make sure that we have at least 1 frame

    pad_signal_length = num_frames * frame_step + frame_length
    z = numpy.zeros((pad_signal_length - signal_length))
    pad_signal = numpy.append(emphasized_signal, z) # Pad Signal to make sure that all frames have equal number of samples without truncating any samples from the original signal

    indices = numpy.tile(numpy.arange(0, frame_length), (num_frames, 1)) + numpy.tile(numpy.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
    frames = pad_signal[indices.astype(numpy.int32, copy=False)]

    #Window
    frames *= numpy.hamming(frame_length)
    # frames *= 0.54 - 0.46 * numpy.cos((2 * numpy.pi * n) / (frame_length - 1))  # Explicit Implementation

    #Fourier Transform and Power Spectrum
    mag_frames = numpy.absolute(numpy.fft.rfft(frames, NFFT))  # Magnitude of the FFT
    pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2))  # Power Spectrum

    #Filter Banks
    low_freq_mel = 0
    high_freq_mel = (2595 * numpy.log10(1 + (sample_rate / 2) / 700))  # Convert Hz to Mel
    mel_points = numpy.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  # Equally spaced in Mel scale
    hz_points = (700 * (10**(mel_points / 2595) - 1))  # Convert Mel to Hz
    bin = numpy.floor((NFFT + 1) * hz_points / sample_rate)

    fbank = numpy.zeros((nfilt, int(numpy.floor(NFFT / 2 + 1))))
    for m in range(1, nfilt + 1):
        f_m_minus = int(bin[m - 1])   # left
        f_m = int(bin[m])             # center
        f_m_plus = int(bin[m + 1])    # right

        for k in range(f_m_minus, f_m):
            fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
        for k in range(f_m, f_m_plus):
            fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
    filter_banks = numpy.dot(pow_frames, fbank.T)
    filter_banks = numpy.where(filter_banks == 0, numpy.finfo(float).eps, filter_banks)  # Numerical Stability
    filter_banks = 20 * numpy.log10(filter_banks)  # dB

    #MFCC
    mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1: (num_ceps + 1)]    # Keep 2-13
    nframes, ncoeff = mfcc.shape
    n = numpy.arange(ncoeff)
    lift = 1 + (cep_lifter / 2) * numpy.sin(numpy.pi * n / cep_lifter)
    mfcc *= lift

    mfcc = numpy.ravel(mfcc)
    return mfcc

'''
path_to_dir = 'C:/Verification/'
folder = os.walk(path_to_dir)

for i in folder:
    if i[1]:
        folders = i[1]

for i in range(0, len(folders)):
    path = path_to_dir + '/' + folders[i]
    person = os.walk(path)
    for j in person:
        for file in j[2]:
            if file == 'filename1.wav':
                temp = mfcc(j[0] + '/' + file)
            else:
                temp = numpy.vstack((temp, mfcc(j[0] + '/' + file)))
        numpy.savetxt(j[0] + '/etalon.txt', temp)
'''


