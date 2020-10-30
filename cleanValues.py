import pandas as pd
import itertools
from count import countItems
from getUnique import getUnique

# df = pd.read_csv('dataset/Market_Basket_Optimisation_Clean.csv',sep=';',header=None)
# items = sorted(getUnique(df))
# for item in items:
#     print(item)

df = pd.read_csv('dataset/Market_Basket_Optimisation_Clean.csv',header=None)#,sep=';',header=None)
df_list = []
for i in range(0,df.shape[0]):
    df_list.append([str(df.values[i,j]) for j in range(0, 20) if str(df.values[i,j]) != 'nan'])

#print item frequencies
c1 = countItems(df, df_list)
#print(c1)

#print sorted unique values
set_unique = sorted(getUnique(df_list))
#print(set_unique)

set2item = list(itertools.combinations(set_unique, 2))
print(len(set2item))
