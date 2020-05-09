import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

data = pd.ExcelFile('labo9/dataset/imiona.xlsx')
df = pd.read_excel(data, 'Arkusz1')
grupa = df[df['Rok']>=2013].groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=14, figsize=(12, 12))
plt.show()