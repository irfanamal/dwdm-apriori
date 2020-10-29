import itertools
import preprocessing
from getUnique import getUnique

def generateCombination(list_items,banlist,level):
    list_combination = list(itertools.combinations(list_items,level))
    if banlist != None:
        for ban in banlist:
            remove_list = []
            for combination in list_combination:
                if all(item in combination for item in ban):
                    remove_list.append(combination)
            for remove in remove_list:
                list_combination.remove(remove)
    return list_combination

def countItems(dataframe,list_kombinasi):
    list_kemunculan = [0 for x in range(len(list_kombinasi))]         
    for i in range(len(list_kemunculan)):
        df = dataframe[list(list_kombinasi[i])]
        list_kemunculan[i] = df[df.all(1)].shape[0]
    return list_kemunculan
        
df = preprocessing.loadData('Dataset/Market_Basket_Optimisation_Clean.csv')
list_items = getUnique(df)
df = preprocessing.toOneHot(df)

banlist = [['almonds'],['energy drink'],['salad'],['salmon'],['hot dogs'],['spinach'],['zucchini'],['antioxydant juice'],['asparagus'],['avocado'],['babies food']]

list_kombinasi = generateCombination(list_items, banlist, 2)
print(len(list_kombinasi))
# if countItems(df, list_kombinasi) == df.sum().values.tolist():
#     print('ahoy')
print(countItems(df, list_kombinasi))
# print(df.sum().values.tolist())

