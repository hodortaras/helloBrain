import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from matplotlib import pylab as plt

url =  'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(url, sep = ';')
X = data[[u'fixed acidity', u'volatile acidity', u'citric acid',
            u'residual sugar', u'chlorides', u'free sulfur dioxide',
            u'total sulfur dioxide', u'density', u'pH',  u'sulphates',
            u'alcohol']]
print(X)
y = data.quality
X = preprocessing.StandardScaler().fit(X).transform(X)
print(X)
model = PCA()
results = model.fit(X)
print(results)
Z = results.transform(X)
print(Z)
plt.plot(results.explained_variance_)
plt.show()

print(pd.DataFrame(results.components_, columns=list([u'fixed acidity', u'volatile acidity', u'citric acid',
                                                u'residual sugar', u'chlorides', u'free sulfur dioxide',
                                                u'total sulfur dioxide', u'density', u'pH',  u'sulphates',
                                                u'alcohol'])))
