import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import scipy.fftpack


#########importing wav files and loading it as a function   #############
PATH='/home/saurabh/Signal-and-Systems/Atraining_normal/201101151127.wav'
spf = wave.open(PATH,'r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('PCG SIGNAL.')
plt.plot(Time,signal)
plt.show()


#######taking fourier transform #######



# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = signal
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.title("FOURIER TRANSFORM") 
plt.show()




