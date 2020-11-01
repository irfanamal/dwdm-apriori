import itertools
import pandas as pd

def generateSubset(list_kombinasi):
    lhs = []
    rhs = []
    for el in list_kombinasi:
      for i in range (1,len(el)):
        comb = list(itertools.combinations(el, i))
        for row in comb:
          lhs.append(list(row))
          rhs.append(list(set(el).difference(row)))

    list_of_tuples = list(zip(lhs, rhs))
    rules = pd.DataFrame(list_of_tuples, columns = ['lhs', 'rhs'])
    return rules

def countOccurence(dataframe,list_kombinasi):
    df = dataframe[list(list_kombinasi)]
    support = df[df.all(1)].shape[0]
    return support

def countSupportConfidence(rules, df):
    sup_x = []
    sup_xy = []
    for i in rules.index:
      r = rules['lhs'][i] + rules['rhs'][i]
      sup_x.append(countOccurence(df, rules['lhs'][i]))
      sup_xy.append(countOccurence(df, r))
    conf = [xy/x*100 for x, xy in zip(sup_x, sup_xy)]
    sup_x = [supx/df.shape[0]*100 for supx in sup_x]
    sup_xy = [supxy/df.shape[0]*100 for supxy in sup_xy]
    rules['support X'] = sup_x
    rules['support XY']= sup_xy
    rules['confidence'] = conf
    return rules

def findAssociation(rules,threshold_support,threshold_confidence):
  assoc_rules = rules.loc[(rules['confidence'] >= threshold_confidence) & (rules['support X'] >= threshold_support)]
  return assoc_rules