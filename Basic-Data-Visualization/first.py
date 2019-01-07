import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='green', linestyle='dashed', label='dashed')
plt.plot([2, 3, 4, 5], [1, 2, 3, 4], color='red', linestyle='dashdot', label='dashdot')
plt.ylabel('Important Figures')
plt.legend()
fig.savefig('first.png')
plt.show()