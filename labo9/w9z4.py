import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('labo9/dataset/iris.csv')


suma = df.groupby(['rodzaj'])['sepal width in cm'].mean()
print(suma)
mean =  df.groupby('rodzaj')['sepal length in cm'].mean()
print(mean)
print(df)

print(suma)
#scale = np.array([mean['sepal length in cm']])
colormap = np.array(['r','g','b'])
wykres = plt.scatter(suma, mean, c=colormap, s=400, cmap="Spectral")
plt.legend()
plt.ylabel("średnia sepal length")
plt.xlabel("Srednia sepal width ") #ach ten polishinglisz
plt.show()