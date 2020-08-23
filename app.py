from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/inputs')
def inputs():
    return render_template("inputs.html")

@app.route('/lookup')
def lookup():
    return render_template("lookup.html")



'''
Receives data from inputs page
Runs the training loop and then predicts what cancer the inputs are correlated to
Returns the render of the result page and makes the prediction and confidence accessible to the html page
'''
@app.route('/results')
def getValues():
    import numpy as np
    import pandas as pd
    from sklearn import neighbors, preprocessing
    from sklearn.model_selection import train_test_split
    import pymongo
    import dns

    ClumpThickness = request.args.get('Clump Thickness')
    UniformityofCellSize = request.args.get('Uniformity of Cell Size')
    UniformityofCellShape = request.args.get('Uniformity of Cell Shape')
    MarginalAdhesion = request.args.get('Marginal Adhesion')
    SingleEpithelialCellSize = request.args.get('Single Epithelial Cell Size')
    BareNuclei = request.args.get('Bare Nuclei')
    BlandChromatin = request.args.get('Bland Chromatin')
    NormalNucleoli = request.args.get('Normal Nucleoli')
    Mitoses = request.args.get('Mitoses')
    
    values = [
        ClumpThickness, 
        UniformityofCellSize, 
        UniformityofCellShape, 
        MarginalAdhesion, 
        SingleEpithelialCellSize, 
        BareNuclei, 
        BlandChromatin, 
        NormalNucleoli, 
        Mitoses
    ]

    def classify(data):
        accuracies = []
        for _ in range(100):
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

    categories = [
        "Clump Thickness",
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

    x = values
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

    return render_template("results.html", values = values, prediction = borm(pred.item()), accuracy = f'{avg_acc*100:0.4f}')

'''
Receives ID from lookup page
Runs the parser to search from the id in the mongodb
Returns the render of lookupresults.hmtl with all the attributes of the patient accessible to lookupresults.html
'''
@app.route('/lookupresults')
def lookupresults():
    import pymongo
    import json
    from bson.objectid import ObjectId

    patientID = request.args.get('patientID')

    def get_from_db(id):
        my_client = pymongo.MongoClient('mongodb+srv://xdhacks:applebanana@cluster0.s06sf.mongodb.net/xdhacks?retryWrites=true&w=majority')
        my_db = my_client['xdhacks']
        my_col = my_db['data']
        patient = my_col.find_one({'_id': ObjectId(str(id))})
        return(patient)

    patient = get_from_db(patientID)
    iden = patient["_id"]
    ct = patient["Clump Thickness"]
    ucsi = patient["Uniformity of Cell Size"]
    ucsh = patient["Uniformity of Cell Shape"]
    ma = patient["Marginal Adhesion"]
    secs = patient["Single Epithelial Cell Size"]
    bn = patient["Bare Nuclei"]
    bc = patient["Bland Chromatin"]
    nn = patient["Normal Nucleoli"]
    m = patient["Mitoses"]
    p = patient["Prediction"]
    a = patient["Accuracy"]


    return render_template("lookupresults.html", iden = iden, ct = ct, ucsi = ucsi, ucsh = ucsh, ma = ma, secs = secs, bn = bn, bc = bc, nn = nn, m = m, p=p, a=a)