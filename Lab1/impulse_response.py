import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

imp = signal.unit_impulse(100, 'mid')
b, a = signal.butter(4, 0.2)
response = signal.lfilter(b, a, imp)


plt.plot(np.arange(-50, 50), imp)
plt.plot(np.arange(-50, 50), response)
plt.margins(0.1, 0.1)
plt.xlabel('Time [samples]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
