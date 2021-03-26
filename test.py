import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_excel('Results-Bioethanol(charts).xlsx')

color_list = ['crimson', 'darkorange', 'darkgreen', 'darkblue']

fig1, ax = plt.subplots()

count = 0



for label, grp in data.groupby('Price'):
    grp.plot(x = 'year', y = 'fisher',ax = ax, label = label, color = color_list[count])
    ax.grid(True)
    plt.title('My Cool Plot')
    plt.xlabel("The Groovy X")
    plt.ylabel("The Super Cool Y")
    ax.legend()
    count += 1