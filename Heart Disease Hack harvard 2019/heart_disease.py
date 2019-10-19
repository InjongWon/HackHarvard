# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 08:48:31 2019

@author: Sayak
"""

#Heart Disease Detection

#importing the libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
dataset = pd.read_csv("heart.csv")
dataset = dataset.drop('cp', 1)
dataset = dataset.drop('chol',1)
dataset = dataset.drop('fbs',1)
dataset = dataset.drop('restecg',1)
dataset = dataset.drop('ca',1)
dataset = dataset.drop('thal',1)
X = dataset.iloc[:, 0:7].values
y = dataset.iloc[:, 7].values

'''The Sex : Male is 1,Female is 0'''

#splitting into train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.12, random_state = 0)
 
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

#fitting the classifier
from sklearn.svm import SVC
classifier = SVC(kernel = "rbf", random_state = 0)
classifier.fit(X_train, y_train)

#predicting the results
y_pred = classifier.predict(X_test)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm  = confusion_matrix(y_test, y_pred)
