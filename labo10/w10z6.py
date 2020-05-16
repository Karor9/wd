import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('imiona.xlsx')

g1 = df.groupby(['Plec'])['Liczba'].sum()
plt.subplot(1, 3, 1)
g1.plot.bar()

m  = df[df['Plec'] == 'M'].groupby(['Rok'])['Liczba'].sum()
k  = df[df['Plec'] == 'K'].groupby(['Rok'])['Liczba'].sum()
plt.subplot(1, 3, 2)
m.plot()
k.plot()

g3 = df.groupby(['Rok'])['Liczba'].sum()
plt.subplot(1, 3, 3)
g3.plot.bar()

plt.show()