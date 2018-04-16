#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train = features_train[:len(features_train)//100]
#labels_train = labels_train[:len(labels_train)//100]

from sklearn import svm, metrics
clf = svm.SVC(kernel = 'rbf', C = 10000)
t0 = time()
clf.fit(features_train, labels_train)
print(time() - t0)
t0 = time()
predict = clf.predict(features_test)
print(time() - t0)
accuracy = metrics.accuracy_score(labels_test, predict)
print(accuracy)
print('10', predict[10])
print('26', predict[26])
print('50', predict[50])
print(sum(predict))


#########################################################
