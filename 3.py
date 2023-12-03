import csv
import matplotlib.pyplot as plt

filename = 'passengers.csv'
all_passengers = []
yearly_passengers = {}

with open(filename, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        all_passengers.append(int(row['#Passengers']))
        year, month = row['Month'].split('-')
        if year in ['1951', '1952', '1953', '1954', '1955']:
            if year not in yearly_passengers:
                yearly_passengers[year] = []
            yearly_passengers[year].append(int(row['#Passengers']))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(all_passengers)
ax1.set_title('Пассажиропоток за все время')
ax1.set_xlabel('Месяц')
ax1.set_ylabel('Количество пассажиров')
ax1.grid(True)

for year in yearly_passengers:
    ax2.hist(yearly_passengers[year], bins=20, alpha=0.5, label=year)

ax2.set_title('Распределение пассажиров по месяцам (1951 - 1955)')
ax2.set_xlabel('Количество пассажиров')
ax2.set_ylabel('Частота')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
