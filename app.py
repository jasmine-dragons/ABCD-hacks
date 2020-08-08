from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

'''def getValues():
    ClumpThickness = request.args.get('Clump Thickness')
    UniformityofCellSize = request.args.get('Uniformity of Cell Size')
    UniformityofCellShape = request.args.get('Uniformity of Cell Shape')
    MarginalAdhesion = request.args.get('Marginal Adhesion')
    SingleEpithelialCellSize = request.args.get('Single Epithelial Cell Size')
    BareNuclei = request.args.get('Bare Nuclei')
    BlandChromatin = request.args.get('Bland Chromatin')
    NormalNucleoli = request.args.get('Normal Nucleoli')
    Mitoses = request.args.get('Mitoses')'''
