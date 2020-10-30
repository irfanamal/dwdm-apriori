def getUnique(df):
    # list_items = []
    # for idx, items in df.iterrows():
    #     items = items.values.tolist()[0].split(',')
    #     list_items += items
    # return set(list_items)
    set_unique = set()
    for lists in df:
        for el in lists:
            set_unique.add(el)
    return set_unique

