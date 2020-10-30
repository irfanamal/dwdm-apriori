import pandas as pd
from getUnique import getUnique

df = pd.read_csv('dataset/Market_Basket_Optimisation_Clean.csv',sep=';',header=None)
items = sorted(getUnique(df))
for item in items:
    print(item)