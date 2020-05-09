import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('labo9/dataset/iris.csv', header=None)
print(df.groupby([4]))
