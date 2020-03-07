import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from matplotlib import pylab as plt
from sklearn.model_selection._split import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

url =  'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(url, sep = ';')
X = data[[u'fixed acidity', u'volatile acidity', u'citric acid',
            u'residual sugar', u'chlorides', u'free sulfur dioxide',
            u'total sulfur dioxide', u'density', u'pH',  u'sulphates',
            u'alcohol']]
y = data.quality
X = preprocessing.StandardScaler().fit(X).transform(X)
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

gnb = GaussianNB()
fit = gnb.fit(X,y)
pred = fit.predict(X)
print(confusion_matrix(pred,y))
print(confusion_matrix(pred,y).trace())


predicted_correct = []
for i in range(1,10):
    model = PCA(n_components = i)
    results = model.fit(X)
    Z = results.transform(X)
    fit = gnb.fit(Z, y)
    pred = fit.predict(Z)
    predicted_correct.append(confusion_matrix(pred, y).trace())
plt.plot(predicted_correct)
plt.show()
