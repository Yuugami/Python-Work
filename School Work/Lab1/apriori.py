import time
import sys

""" Creates a sample dataset """


def sampleDataset():
    l = [[1, 2, 3, 4],
        [1, 2, 4],
        [1, 2],
        [2, 3, 4],
        [2, 3],
        [3, 4],
        [2, 4]]
    return l

"""
This function generates a list of pairs given a candidate list
and returns that list.

"""


def generatePairs(freqList, tupleLen):
    retList = []
    lenLk = len(freqList)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(freqList[i])[:tupleLen - 2]
            L2 = list(freqList[j])[:tupleLen - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(freqList[i] | freqList[j])
    return retList

"""
Returns list of frequent items in a dataset, based on
the support threshold.

"""


def freqList(dataset, candidates, supportlvl):
    freqSet = {}
    for transaction in dataset:
        #print transaction
        for key in candidates:
            if key.issubset(transaction):
                freqSet.setdefault(key, 0)
                freqSet[key] += 1

    #print "Candidate List + Occurences = " + str(freqSet)
    #num_basket = float(len(dataset))
    #print str(num_basket) + " baskets read."  # Still doing Pass 1

    finallist = []
    support_data = {}

    for key in freqSet:
        # print key
        # print freqSet[key]
        support = freqSet[key]
        if support >= supportlvl:
            #print str(key) + " occurs " + str(freqSet[key]) + " times."
            finallist.insert(0, key)
        support_data[key] = support
    return finallist, support_data

"""
CandidateList returns a list of candidates and the number of occurences in a
given dataset. The sample dataset above will return a list with a length
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
This function finds and prints all frequent pairs of elements.

T = Transactional Database
st = Support Threshold/Rules

"""


def apriori(T, st):  # T is Transactional dataset, st is the Support Threshold
    C1 = candidateList(T)  # Candidate Variable. Counts all items. Pass 1 Start
    D = map(set, T)  # Holds dataset
    Lk, support_data = freqList(D, C1, st)
    # print "\nThis is the dataset: \n" + str(D)
    # print "\nHere are the Candidates: \n" + str(C1)
    # print "\nEach candidate occured this many times: \n" + str(support_data)
    # print "\nThe following items are frequent: \n" + str(Lk)
    # Time for Pass 2
    # Generate a list of all pairs of frequent items. All distinct.
    L = [Lk]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = generatePairs(L[k - 2], k)
        Lk, supK = freqList(D, Ck, st)
        support_data.update(supK)
        L.append(Lk)
        k += 1

    return L, support_data


def main(database, supplvl):
# Create a dataset and feed it to the apriori function
    # dataset = sampleDataset()
    start = time.time()
    theFile = open(database, "r")
    dataset = []
    for line in theFile:
        line = line.split(" ")
        line.pop()
        dataset.append(line)

    print "---------------------------------------------"
    delist, support = apriori(dataset, int(supplvl))
    print "---------------------------------------------"
    print "Final Frequent List: "
    for key in range(len(delist)):
        print str(key+1) + "-tuple: " + str(delist[key])
        print
    end = time.time() - start
    #print start
    print
    print "Time Elapsed: " + str(end) + " seconds. || " + str(end/60) + \
        " minutes."

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
