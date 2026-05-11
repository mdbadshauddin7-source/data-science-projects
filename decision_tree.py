from sklearn.tree import DecisionTreeClassifier
import numpy as np

data = np.array([[1,0],[1,1],[0,0],[0,1]])
labels = np.array([0,1,2,3])

model = DecisionTreeClassifier()
model.fit(data, labels)

fruits = ["apple", "banana", "orange", "grape"]

prediction = model.predict([[0,0]])
print("the fruit:", fruits[prediction[0]])
prediction = model.predict([[0,1]])
print("the fruit:", fruits[prediction[0]])