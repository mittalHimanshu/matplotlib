import csv
import matplotlib.pyplot as plt

input_file = 'old_faithful.csv'
plt.style.use('classic')

fig = plt.figure()

with open (input_file, 'r') as old_data:
    eruptions = list(csv.reader(old_data))

eruptions.pop(0)

eruption_times = []
waiting_times = []

for event in range(0, len(eruptions)):
    eruption_times.append(float(eruptions[event][0]))
    waiting_times.append(float(eruptions[event][1]))

plt.subplot(2, 2, 1)
plt.boxplot(eruption_times)
plt.title('Old Eruptions')
plt.xticks([1], ['Eruptions'])
plt.xlabel('Length of Eruption (mins)')

plt.subplot(2, 2, 2)
plt.boxplot(waiting_times)
plt.title('Old Waiting')
plt.xticks([1], ['Waiting'])
plt.xlabel('Length of Waiting (mins)')

plt.subplot(2, 1, 2)
plt.scatter(eruption_times, waiting_times)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (mins)')
plt.ylabel('Time Between Eruptions (mins)')

plt.tight_layout()

fig.savefig('project.png')

plt.show()