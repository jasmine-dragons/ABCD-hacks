import numpy as np
import pandas as pd
from sklearn import neighbors, preprocessing
from sklearn.model_selection import train_test_split

def get_input(lst):
     return lst

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
    pred = clf.predict(get_input(data))
    return avg_acc, pred

def borm(num):
    return 'Benign' if num == 2 else 'Malignant'

example_measures = [
    [4,2,1,1,1,2,3,2,1],
    [4,2,1,2,2,2,3,2,1],
    [4,2,1,2,2,2,3,2,1],
    [4,2,1,2,2,2,3,2,1],
    [8,11,9,6,9,2,5,6,1]
]

avg_acc, pred = classify(example_measures)
print('Prediction:',pred)


'''
We need the input as a comma separated string of 9 integers from 1-10
'''
x = input('| Enter the parameters: ').split(',')
y = [[int(i) for i in x]]
avg_acc, pred = classify(y)

print(f'| Prediction: {pred.item()} => {borm(pred.item())} \t|')
print(f'| Accuracy of dataset: {avg_acc:.4f} \t|')
