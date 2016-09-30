"""
Kaggle Project - Windjy Jean

1. Access CSV files [X]

---

2. Separate CSV files accordingly.
Training data CSV into the training list.
Test data CSV into the test list. [X]

2.1. Every row represents a user.
Every column represents either User ID (Column 1), Features (Column 2-3674) or
Category (3675)

---

3. Create an algorithm.... K good luck! LOL anywho...

Test lacks column 3675. That's what we are trying to find.

Y (Category) = w0 + w1X1(e) + wnXn(e)

"""

import csv

trainingData = "kaggle_AI_training_data.csv"
testData = "kaggle_AI_test_data.csv"

training = []
test = []

total = 0

with open(trainingData, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    training = list(reader)

with open(testData, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    test = list(reader)

print "In the training center..."
for user in training:
    for cell in user:
        if (int(cell) < 2):
            total += int(cell)
    total -= int(user[-1])
    print "User #" + str(user[0]) + " scored a " + str(total)
    if (int(user[-1]) == 1):
        print "Accepted!"
    else:
        print "Denied..."
    print "----------------"
    total = 0

# print "In the testing center..."
# for user in test:
#     for cell in user:
#         if (int(cell) < 2):
#             total += int(cell)
#     print "User #" + str(user[0]) + " scored a " + str(total)
#     total = 0
