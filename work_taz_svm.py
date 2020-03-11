import tarfile
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.datasets import load_svmlight_file
import numpy as np
from numpy import unique

uri = 'C:\\Users\\Tarar\\Downloads\\url_svmlight.tar.gz'
tar = tarfile.open(uri,"r:gz")
max_obs = 0
max_vars = 0
i=0
split = 5
classes = [-1, 1]
sgd = SGDClassifier(loss = "log")
n_features = 3231961
X = None

for tarinfo in tar:
    print('Extracting {}, file size {}'.format(tarinfo.name, tarinfo.size))
    if tarinfo.size == 212:
        break
    if tarinfo.isfile():
        f = tar.extractfile(tarinfo.name)
        X, y = load_svmlight_file(f, n_features = n_features)
    if X != None:
        sgd.partial_fit(X, y, classes = classes)
print(classification_report(sgd.predict(X),y))

# import glob
# from sklearn.datasets import load_svmlight_file
#
# path = 'C:\\Users\\Tarar\\Downloads\\url_svmlight\\url_svmlight\\url_svmlight\\*.svm'
# files = glob.glob(path)
# print('%d', len(files))
#
# X,y = load_svmlight_file(files[0], n_features = 3231961)
# non_zero = float((X.nnz)/(float(X.shape[0])*float(X.shape[1])))
# print(f'number of non zero entries {non_zero}' )
# # X.todense()
