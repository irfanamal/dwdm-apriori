import pandas as pd
import numpy as np
from getUnique import getUnique

def loadData(filename):
    return pd.read_csv(filename,sep=';',header=None)

def toOneHot(dataframe):
    columns = list(getUnique(dataframe))
    print(columns[0])
    df = pd.DataFrame(0, index=np.arange(dataframe.shape[0]), columns=columns)
    for idx, items in dataframe.iterrows():
        items = items[0].split(',')
        for item in items:
            df.at[idx, item] = 1
    return df