import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv', sep=";")

ilosc = df.groupby('Sprzedawca')['idZamowienia'].count()
sprzed = set(df['Sprzedawca'])
explode = ([0 for i in range(len(sprzed))])
explode[3] = 0.2


w = ilosc.plot.pie(labels = df['Sprzedawca'], autopct=lambda pct: "{:.1f}%".format(pct), textprops = dict(color="black"), shadow = True, explode = explode)
plt.legend()

plt.show()
