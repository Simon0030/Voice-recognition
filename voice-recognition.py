import soundfile
import numpy as np
from scipy.signal import decimate
import warnings
import sys


warnings.filterwarnings("ignore")

def reading():
    signal, sample_rate = soundfile.read(sys.argv[1], dtype='int16')
    if len(signal.shape) == 2:
        signal = [s[0] for s in signal]
    return signal

def signalling(signal):
    signal1 = signal.copy()
    signal1 = np.fft.fft(signal1)

    signal2 = signal1[1: int(len(signal1) / 2)]

    signal3 = signal2.copy()
    signal3 = abs(signal3) * 2 / len(signal)
    return signal3

def decimating(signal3):
    zmiana1 = signal3.copy()
    zmiana1 = decimate(zmiana1, 1)
    zmiana2 = signal3.copy()
    zmiana2 = decimate(zmiana2, 2)
    zmiana3 = signal3.copy()
    zmiana3 = decimate(zmiana3, 3)
    zmiana4 = signal3.copy()
    zmiana4 = decimate(zmiana4, 4)
    zmiana5 = signal3.copy()
    zmiana5 = decimate(zmiana5, 5)
    zakres = len(zmiana5)
    wynik = signal3[:zakres] * zmiana1[:zakres] * zmiana2[:zakres] * zmiana3[:zakres] * zmiana4[:zakres] * zmiana5[:zakres]
    wynik[0:500] = 0
    return wynik



def checking():
    signal = reading()
    signal_abs = signalling(signal)
    wynik = decimating(signal_abs)
    wartosc = 750
    maks = max(wynik)
    score = 0
    for i in range(len(wynik)):
        if wynik[i] == maks:
            score = i
            break
    if score > wartosc:
        print('K')
    else:
        print('M')



checking()





