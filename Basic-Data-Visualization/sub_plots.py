import matplotlib.pyplot as plt

# create first panel
panel_1 = plt.subplot(2, 1, 1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='green', linestyle='dashed')
panel_1.set_xlim([0, 6])
panel_1.set_ylim([0, 20])

# create second panel
panel_2 = plt.subplot(2, 1, 2)
plt.plot([2, 3, 4, 5], [1, 2, 3, 4], color='blue', linestyle='dashdot')
panel_2.set_xlim([0, 6])
panel_2.set_ylim([0, 20])

plt.show()