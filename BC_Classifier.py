import numpy as np
import pandas as pd
from sklearn import neighbors, preprocessing
from sklearn.model_selection import train_test_split
import pymongo

def get_input(lst):
     return lst

def classify(data, idnum):
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
    pred = clf.predict(get_input(data))
    return avg_acc, pred, idnum

def borm(num):
    return 'Benign Cancer' if num == 2 else 'Malignant Cancer'

def add_to_db(inputs):
    my_client = pymongo.MongoClient('mongodb+srv://xdhacks:applebanana@cluster0.s06sf.mongodb.net/xdhacks?retryWrites=true&w=majority')
    my_db = my_client['xdhacks']
    my_db.insert_one(inputs)

## This dict need to be added to the database
p_id = {}
inputs = {
    "Clump Thickness" : None,
    "Uniformity of Cell Size" : None,
    "Uniformity of Cell Shape" : None,
    "Marginal Adhesion" : None,
    "Single Epithelial Cell Size" : None,
    "Bare Nuclei" : None,
    "Bland Chromatin" : None,
    "Normal Nucleoli" : None,
    "Mitoses" : None,
}
'''
We need the input as a comma separated string of 9 integers from 1-10
'''
x = input('| Enter the parameters: ').split(',')
y = [[int(i) for i in x]]

for i in range(len(y)):
    for item in inputs:
        inputs[item] = y[i]

avg_acc, pred, idnum = classify(y, 111111)

print(f'| Prediction: {borm(pred.item())} \t|')
print(f'| Accuracy of dataset: {avg_acc*100:.3f}% \t|')
print(p_id)

add_to_db(inputs)
