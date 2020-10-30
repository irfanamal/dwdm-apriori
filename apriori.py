import itertools
# import preprocessing
# from getUnique import getUnique

def generateCombination(list_items,banlist,level):
    list_kombinasi = list(itertools.combinations(list_items,level))
    if len(list_kombinasi) > 1:
        if banlist:
            for ban in banlist:
                remove_list = []
                for kombinasi in list_kombinasi:
                    if all(item in kombinasi for item in ban):
                        remove_list.append(kombinasi)
                remove_list = set(remove_list)
                for remove in remove_list:
                    list_kombinasi.remove(remove)
    return list_kombinasi

def countItems(dataframe,list_kombinasi):
    list_kemunculan = [0 for x in range(len(list_kombinasi))]         
    for i in range(len(list_kemunculan)):
        df = dataframe[list(list_kombinasi[i])]
        list_kemunculan[i] = df[df.all(1)].shape[0]
    return list_kemunculan

def scanInfrequent(list_kemunculan,threshold):
    list_index_infrequent = []
    for i in range(len(list_kemunculan)):
        if list_kemunculan[i] <= threshold:
            list_index_infrequent.append(i)
    return list_index_infrequent

def getInfrequent(list_kombinasi,list_index_infrequent):
    list_infrequent = [list_kombinasi[i] for i in list_index_infrequent]
    return list_infrequent

def dropItems(list_kombinasi,list_infrequent):
    return list(set(list_kombinasi)-set(list_infrequent))

def getUniqueItems(list_kombinasi):
    list_items = []
    for kombinasi in list_kombinasi:
        for item in kombinasi:
            list_items.append(item)
    return set(list_items)

def mainApriori(dataframe,banlist,level,list_items,threshold):
    if banlist == None:
        banlist = []
    list_kombinasi = generateCombination(list_items, banlist, level)
    if len(list_kombinasi) <= 1:
        return list_kombinasi
    else:
        list_kemunculan = countItems(dataframe, list_kombinasi)
        list_index_infrequent = scanInfrequent(list_kemunculan, threshold)
        if not list_index_infrequent:
            return list_kombinasi
        else:
            list_infrequent = getInfrequent(list_kombinasi, list_index_infrequent)
            list_kombinasi_2 = dropItems(list_kombinasi, list_infrequent)
            if len(list_kombinasi_2) <= 1:
                return list_kombinasi_2
            else:
                list_items = getUniqueItems(list_kombinasi_2)
                banlist = banlist + list_infrequent
                # print(len(banlist))
                # print(level, len(list_kombinasi), len(list_kombinasi_2), len(list_items))
                return mainApriori(dataframe, banlist, level+1, list_items, threshold)
        
# df = preprocessing.loadData('Dataset/Market_Basket_Optimisation_Clean.csv')
# list_items = getUnique(df)
# df = preprocessing.toOneHot(df)
#
# list_kombinasi = mainApriori(df, None, 1, list_items, 25)
# print(len(list_kombinasi))
# print(list_kombinasi)