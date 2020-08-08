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


@app.route('/results')
def results():
    request.args.get("
