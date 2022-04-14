import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use()

sexual_orientation = {
    'gay': 28.8,
    'straight': 10.1,
    'bisexual': 23.4,
    'pansexual': 16.5,
    'asexual': 10.5,
    'don\'t know': 5.8,
    'something else': 4.9
}
labels = list(sexual_orientation)
nums = []
for label in labels:
    nums.append(sexual_orientation[label])

colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(sexual_orientation)))

fig, ax = plt.subplots()
wedges, texts = ax.pie(nums, labels=labels, colors=colors, radius=3, center=(4, 4),
                                  textprops={'color': 'black'},
                                  wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

ax.legend(wedges, labels,
          title='Orientation',
          loc='upper right',
          bbox_to_anchor=(1, 0, 0.5, 1))

ax.set_title('Sexual Orientation in the Furry Fandom')

plt.show()