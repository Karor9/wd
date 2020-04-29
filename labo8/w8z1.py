import numpy as np
import pandas as pd
import xlrd
import openpyxl

data = pd.ExcelFile('labo8/dataset/imiona.xlsx')
df = pd.read_excel(data, 'Arkusz1')
print(df)