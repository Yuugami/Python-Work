"""-------------------------------------------------------------------------"""
""" Creates a sample dataset """


def sampleDataset():
    l = [[1, 2, 3], [1, 2, 4], [1, 2, 3], [1, 2, 4]]
    return l

"""
Returns a list of candidates in a given dataset.
The sample dataset above will return a list with a length
of  four.

"""


def candidateList(dataset):
    c = []

    for transaction in dataset:
        for item in transaction:
            if not [item] in c:
                c.append([item])
    c.sort()
    return map(frozenset, c)

"""
Returns list of frequent items in a dataset, based on
the support threshold.

"""


def freqList(dataset, candidates, supportlvl):
    freqSet = {}
    for transaction in dataset:
        for key in candidates:
            if key.issubset(transaction):
                freqSet.setdefault(key, 0)
                freqSet[key] += 1
    print freqSet
    num_items = float(len(dataset))
    finallist = []
    support_data = {}

    for key in freqSet:
        support = freqSet[key] / num_items
        if support >= supportlvl:
            finallist.insert(0, key)
        support_data[key] = support
    return finallist, support_data
"""
This function finds and prints all frequent pairs of elements.
T = Transactional Database
st = Support Threshold/Rules

"""


def apriori(T, st):
    C1 = candidateList(T)  # Candidate Variable. Counts all items. Pass 1
    D = map(set, T)
    Lk, support_data = freqList(D, C1, st)
    print "\nCandidates: \n" + str(C1)
    print "\nThis is the dataset: \n" + str(D)

# Create a dataset and feed it to the apriori function
dataset = sampleDataset()
print "---------------------------------------------"
apriori(dataset, 0.6)
