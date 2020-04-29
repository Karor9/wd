import numpy as np
import pandas as pd
import xlrd
import openpyxl

def podpunkt1(df):
    print(df[df['Liczba']>1000])

def podpunkt2(df, imie):
    imie = imie.upper()
    print(df[df['Imie']==imie])
    
def podpunkt3(df):
    print("Suma urodzeń wynosi: " + str(df['Liczba'].sum()))

def podpunkt4(df):
    print(df[(df['Rok']<=2005) & (df['Rok']>=2000)])

def podpunkt5(df):
    print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

def podpunkt6(df):
    x = df.groupby(['Rok', 'Plec']).agg({'Liczba':[max]})

data = pd.ExcelFile('labo8/dataset/imiona.xlsx')
df = pd.read_excel(data, 'Arkusz1')

#podpunkt1(df)
#podpunkt2(df, "karol")
#podpunkt3(df)
#podpunkt4(df)
#podpunkt5(df)
podpunkt6(df)

#
#