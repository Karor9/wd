import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('labo9/dataset/zamowienia.csv', header=0, sep=';')
grupa = data.groupby('Sprzedawca').agg({'Sprzedawca':['count']})
wykres = grupa.plot.bar()
wykres.legend()
plt.show()