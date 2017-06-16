import pandas as pd, csv
from crisp_dm.crisp_dm_processor import CRISPDMProcessor
from ex1_data_understanding_helper import Ex1DataUnderstandingHelper

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# Read Data

data, be_titles = [], True
with open('db/HR_comma_sep.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        fields = row[0].split(',')
        if not be_titles:
            fields = [float(fields[0]), float(fields[1]), int(fields[2]), int(fields[3]),
                      int(fields[4]), int(fields[5]), int(fields[6]), int(fields[7]), fields[8], fields[9]]
        else:
            be_titles = False
        data.append(fields)

df = pd.DataFrame(data[1:], columns=data[0])

# Setting Up CRISP-DM Processor

processor = CRISPDMProcessor()
processor.set_data_understanding_helper(Ex1DataUnderstandingHelper())

# define parser
def parse_X(dt):
    columns = list(dt.columns)
    columns.remove('left')
    return dt[columns]

processor.draw_data = df
processor.parse_X = parse_X
processor.parse_y = lambda dt: dt['left']

# collection of classifiers
classifiers = [
    ('KNeighborsClassifier', KNeighborsClassifier(3)),
    ('SVC_1', SVC(kernel="linear", C=0.025)),
    ('SVC_2', SVC(gamma=2, C=1)),
    # ('GaussianProcessClassifier', GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True)),
    ('DecisionTreeClassifier', DecisionTreeClassifier(max_depth=5)),
    ('RandomForestClassifier', RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)),
    ('MLPClassifier', MLPClassifier(alpha=1)),
    ('AdaBoostClassifier', AdaBoostClassifier()),
    ('GaussianNB', GaussianNB()),
    ('QuadraticDiscriminantAnalysis', QuadraticDiscriminantAnalysis())]

# Process
for classifier in classifiers:
    print 'Model :', classifier[0]
    processor.model = classifier[1]
    processor.process()
    print '====================================='