import numpy as np
import pandas as pd
from sklearn import neighbors, preprocessing
from sklearn.model_selection import train_test_split
import pymongo
import dns
from app import getValues

def classify(data):
    accuracies = []
    for i in range(100):
        dframe = pd.read_csv('bcdata.csv')
        dframe.replace('?', -99999, inplace=True)
        dframe.drop(['id'], 1, inplace=True)

        X = np.array(dframe.drop(['class'],1))
        y = np.array(dframe['class'])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        clf = neighbors.KNeighborsClassifier()
        clf.fit(X_train, y_train)

        acc = clf.score(X_test, y_test)
        accuracies.append(acc)

    avg_acc = sum(accuracies)/len(accuracies)
    pred = clf.predict(data)
    return avg_acc, pred

def borm(num):
    return 'Benign Cancer' if num == 2 else 'Malignant Cancer'

def add_to_db(inputs):
    my_client = pymongo.MongoClient('mongodb+srv://xdhacks:applebanana@cluster0.s06sf.mongodb.net/xdhacks?retryWrites=true&w=majority')
    my_db = my_client['xdhacks']
    my_col = my_db['data']
    my_col.insert_one(inputs)

## This dict need to be added to the database
categories = ["Clump Thickness",
    "Uniformity of Cell Size",
    "Uniformity of Cell Shape",
    "Marginal Adhesion",
    "Single Epithelial Cell Size",
    "Bare Nuclei",
    "Bland Chromatin",
    "Normal Nucleoli",
    "Mitoses",
    ]
inputs = {}

x = input('| Enter the parameters: ').split(',')
y = [[int(i) for i in x]]

for i in range(len(y)):
    for item in categories:
        inputs[item] = y[0][i]
        i+=1

avg_acc, pred = classify(y)

inputs["Prediction"] = borm(pred.item())
inputs["Accuracy"] = avg_acc*100

print(f'| Prediction: {borm(pred.item())} \t|')
print(f'| Accuracy of dataset: {avg_acc*100:.3f}% \t|')

add_to_db(inputs)

