import numpy as np
import pandas as pd

def podpunkt1(df):
    print(df['Sprzedawca'][df['Sprzedawca'].duplicated() == False])

def podpunkt2(df):
    print(df.sort_values(by='Utarg', ascending=False).head(5))

def podpunkt3(df):
    print(df.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))

def podpunkt4(df):
    print(df.groupby('Kraj').agg({'Kraj':['count']}))

def podpunkt5(df):
    print(df[(df['Data zamowienia'].str.slice(0, 4, 1)=='2005') & (df['Kraj']=="Polska")].agg({'Kraj':['count']}))

def podpunkt6(df):
    print(df[(df['Data zamowienia'].str.slice(0, 4, 1)=='2004') & (df['Kraj']=="Polska")].agg({'Utarg':['mean']}))

def podpunkt7(df):
    x = df[(df['Data zamowienia'].str.slice(0, 4, 1)=='2004')]
    y = df[(df['Data zamowienia'].str.slice(0, 4, 1)=='2005')]
    x.to_csv('labo8/zamówienia_2004.csv', index = False)
    y.to_csv('labo8/zamówienia_2005.csv', index = False)


   
data = pd.read_csv('labo8/dataset/zamowienia.csv', header=0, sep=';')

#podpunkt1(data)
#podpunkt2(data)
#podpunkt3(data)
#podpunkt4(data)
#podpunkt5(data)
#podpunkt6(data)
podpunkt7(data)
#podpunkt1(data)
