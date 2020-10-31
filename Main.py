import apriori
import preprocessing
from getUnique import getUnique
from associationRules import generateSubset, countSupportConfidence, findAssociation

df = preprocessing.loadData('Dataset/Market_Basket_Optimisation_Clean.csv')
list_items = getUnique(df)
df = preprocessing.toOneHot(df)

list_kombinasi = apriori.mainApriori(df, None, 1, list_items, 25)
print(len(list_kombinasi))
print(list_kombinasi)

df_rules = generateSubset(list_kombinasi)
df_rules = countSupportConfidence(df_rules, df)
rules = findAssociation(df_rules,0.3,50)
print(rules)