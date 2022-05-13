"""
Description:
"""
# %%
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

#Load datasets
iris =datasets.load_iris()
X = iris.data
y= iris.target
# print(X.shape,y.shape)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

# %%
