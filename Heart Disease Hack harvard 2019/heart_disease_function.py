# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:59:52 2019

@author: Sayak
"""



#Heart Disease Detection Rest-API

#importing the libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

def predict():
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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)
     
    #Feature Scaling
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.fit_transform(X_test)
    
    #fitting the classifier
    classifier = SVC(kernel = "rbf", random_state = 0)
    classifier.fit(X_train, y_train)
    
    if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
        
    if my_prediction == 0:
        print ("Everything is Normal. No need to consult any doctor")
    elif my_prediction == 1:
        print ("Safety Concern raised. You need to consult a doctor")
        
	return render_template('result.html',prediction = my_prediction)