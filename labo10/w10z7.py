import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx')

m  = df[df['Plec'] == 'M'].groupby(['Rok'])['Liczba'].sum()
k  = df[df['Plec'] == 'K'].groupby(['Rok'])['Liczba'].sum()

m.plot.bar(color = 'lightblue')
k.plot.bar(color = 'pink', bottom = m)

plt.show()