import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC(gamma = 0.001, C = 100) # gamma mide el 'paso' en el gradient descent.

print(len(digits.data))

x_train , y_train = digits.data[:-2] , digits.target[:-2] 


clf.fit(x_train,y_train)

print('Prediction = ', clf.predict(digits.data[[-2]]))

plt.imshow(digits.images[-2], cmap = plt.cm.gray_r, interpolation = "nearest")
plt.show()
