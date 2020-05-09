import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

data = pd.ExcelFile('labo9/dataset/imiona.xlsx')
df = pd.read_excel(data, 'Arkusz1')
grupa = df.groupby(['Rok', 'Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar()
wykres.legend()
plt.show()