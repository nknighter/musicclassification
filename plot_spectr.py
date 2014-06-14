import scipy.io.wavfile as wv
import numpy as np
import matplotlib.pyplot as pl


def plotSpectrum(y, Fs):

    n = len(y)  # length signal
    window = np.hamming(n)
    k = np.arange(n)
    T = n / Fs
    frq = k / T  # two sides frequency range
    frq = frq[range(n / 2)]  # one side frequency range

    Y = np.fft.fft(y * window) / n  # fft computing and normalization
    Y = Y[range(n / 2)]
    pl.plot(frq, abs(Y), 'b')  # plotting the spectrum
    pl.xlabel('Frequency (Hz)')
    pl.ylabel('Magnitude')


rate, data = wv.read("test.wav")
data = data[:, 0]
print data

t = np.linspace(0, len(data[:441000]) / rate, num=len(data[:441000]))

#pl.plot(t, data[:441000], 'b')
#pl.xlabel('Time (second)')
#pl.ylabel('Amplitude')
# subplot(2, 1, 2)
plotSpectrum(data[1000000:1441000], rate)
pl.show()