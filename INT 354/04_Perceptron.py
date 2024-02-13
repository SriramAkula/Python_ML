# -*- coding: utf-8 -*-
"""Perceptron.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q9aZOwn_aCtPlfn0U33yf03tz8Lj9-Uq
"""



import numpy as np
class Perceptron(object):
  def __init__(self,eta=0.01,n_iter=50,random_state=1):
    self.eta=eta
    self.n_iter=n_iter  ##Epochs=50
    self.random_state=random_state  #supports shuffling of training data
  def fit(self,X,y):  #Gradient Descent to decrease the Error
    rgen = np.random.RandomState(self.random_state)
    self.w_=rgen.normal(loc=0.0,scale=0.01,size=1+X.shape[1])
    self.errors_=[] #stepwise determine the error value by gradient
    for _ in range(self.n_iter):
      errors=0
    for xi,target in zip(X,y): #Adjusting weights to reduce error
      update=self.eta * (target-self.predict(xi))
      self.w_[1:] += update*xi
      self.w_[0] += update
      errors += int(update!=0.0)
      self.errors_.append(errors)
    return self
  def net_input(self,X):
    return np.dot(X,self.w_[1:])+self.w_[0]
  def predict(self,X):
    return np.where(self.net_input(X) >= 0.0,1,-1)

from sklearn import datasets
import numpy as np
iris=datasets.load_iris()
X=iris.data[:,[2,3]]
y=iris.target
print('Class labels:',np.unique(y))

