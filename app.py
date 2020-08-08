from flask import Flask, render_template
import numpy as np
import pandas as pd
from sklearn import neighbors, preprocessing
from sklearn.model_selection import train_test_split
import pymongo
import dns

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def getValues():
    ClumpThickness = request.args.get('Clump Thickness')
    UniformityofCellSize = request.args.get('Uniformity of Cell Size')
    UniformityofCellShape = request.args.get('Uniformity of Cell Shape')
    MarginalAdhesion = request.args.get('Marginal Adhesion')
    SingleEpithelialCellSize = request.args.get('Single Epithelial Cell Size')
    BareNuclei = request.args.get('Bare Nuclei')
    BlandChromatin = request.args.get('Bland Chromatin')
    NormalNucleoli = request.args.get('Normal Nucleoli')
    Mitoses = request.args.get('Mitoses')
    values = [ClumpThickness, UniformityofCellSize, UniformityofCellSize, MarginalAdhesion, SingleEpithelialCellSize, BareNuclei, BlandChromatin, NormalNucleoli, Mitoses]
