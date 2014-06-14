from scipy import fft, arange, ifft, stats as st
from numpy import sin, linspace, pi, std, mean, median, hamming, amax, amin
import scipy.io.wavfile as wv
import glob

def analyze(filename):
    chunk_length = 50000

    rate, data = wv.read(filename)
    signal_len, channels_num = data.shape
    chunks_num = signal_len / chunk_length
    # if stereo, getting the mean value
    if channels_num != 1:
        data = mean(data, 1)

    info = []
    for i in range(chunks_num):
        window = hamming(chunk_length)
        chunk_data = data[i*chunk_length:(i+1)*chunk_length]
        #time = float(chunk_length)/rate
        #frq = arange(chunk_length)/time
        #frq = frq[range(chunkLength / 2)]

        #FFT = fft(chunk_data) / chunk_length
        FFT = fft(chunk_data * window) / chunk_length
        #power_spectrum = abs(FFT)**2
        #FFT = FFT[:chunk_length]

        absFFT = abs(FFT[:chunk_length/2])
        info.append([absFFT[i] for i in range(0, len(absFFT), 1000)])

    stats = []
    for i in range(chunk_length / 2000):
        temp = []
        for j in range(chunks_num):
            temp.append(info[j][i])
        stats.append(round(mean(temp), 3))
        stats.append(round(median(temp), 3))
        stats.append(round(std(temp), 3))
        #stats.append(round(st.kurtosis(temp), 3))
        #stats.append(round(st.skew(temp),3))

    return stats

dataFile = open('data.txt', 'w')

fileNames = glob.glob('./src_wav/*.wav')
for fileName in fileNames:
    print fileName
    stats = analyze(fileName)
    print amax(stats)
    print amin(stats)
    dataFile.write(' '.join(str(x) for x in stats) + '\n')

dataFile.close()

