import pandas as pd 
import numpy as np 
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
data = pd.read_csv("student-mat.csv", sep = ';')
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[[predict]])

best_acc = 0
for j in range(500):
    x_train, x_test, y_train, y_test =sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
  
    if acc > best_acc:
        best_acc = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

pickle_int = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_int)

print("Best Accuracy = ", best_acc)
x_train, x_test, y_train, y_test =sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

print("Score = ",linear.score(x_test, y_test))

"""
predictions = linear.predict(x_test)

for i in range(len(predictions)):
    print("Predicción ",predictions[i]," Datos",  y_test[i],"\n")
"""