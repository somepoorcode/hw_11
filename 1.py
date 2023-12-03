import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

t = np.linspace(0, 1, 1000, endpoint=False)
frequency = 7
x = square(2 * np.pi * frequency * t)

plt.figure(figsize=(8, 4))
plt.plot(t, x)
plt.title('Прямоугольный сигнал')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()
