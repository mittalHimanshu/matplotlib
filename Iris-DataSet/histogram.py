import csv
import matplotlib.pyplot as plt

input_file = 'iris.csv'
plt.figure(figsize=(7.5, 4.25))
plt.style.use('classic')
fig = plt.figure()

with open(input_file, 'r') as iris_data:
    irises = list(csv.reader(iris_data))

virginica_petal_length = []
num_bins = 5

for petal in range(0, len(irises)):
    if irises[petal][4] == 'Iris-virginica':
        virginica_petal_length.append(irises[petal][2])

plt.hist(virginica_petal_length, num_bins, facecolor='g', alpha=0.75)
plt.title('Iris-virginica Petal length', fontsize=12)
plt.xlabel('Petal length (cm)', fontsize=10)
plt.ylabel('Probablity', fontsize=10)
fig.savefig('histogram.png')
plt.show()