import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=20, density=True, alpha=0.5)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-(x - mean) ** 2 / (2 * std_dev ** 2))
plt.plot(x, p, linewidth=2)
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота появления')
plt.legend(['Нормальное распределение', 'Гистограмма'])
plt.grid(True)
plt.show()
