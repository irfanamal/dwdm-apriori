from collections import Counter
import pandas as pd

def countSupport(dataframe, list_support):
    return list_support['count'] / dataframe.shape[0] * 100

def countItems(dataframe, list_kombinasi):
    count = Counter(x for xs in list_kombinasi for x in set(xs))
    df_count = pd.DataFrame.from_dict(count, orient='index',  columns=['count']).reset_index()
    df_count['support %'] = countSupport(dataframe, df_count)
    return df_count