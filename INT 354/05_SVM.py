import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

#Generating synthetic data for illustration
np.random.seed(42)
X=np.random.randn(20,2) #2o data points with 2 features
y=np.where(X[:,0]+X[:,1]>0,1,-1)

#Fit SVM model with a linear kernel and a large C Value for hard-margin
C_value=1e6 #Use a large value to appoximate a hard-margin
clf=svm.SVC(kernel='linear',C=C_value)

# Plotting decision boundary and support vectors
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Paired)
ax=plt.gca()

#plot decisison boundary
xlim=ax.get_xlim()
ylim=ax.get_ylim()

#Create grid to evaluate model
xx,yy=np.meshgrid(np.linspace(xlim[0],xlim[1],50))
xx,yy=np.meshgrid(np.linspace(ylim[0],ylim[1],50))

#Plot decision fun for each datapoint in grid
Z=clf.decision_function(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)

#plot decision boundary and margins
ax.contour
