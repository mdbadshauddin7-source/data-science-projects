from sklearn.naive_bayes import GaussianNB
import numpy as np 

data = np.array([[1,0],[5,1],[2,0],[8,1],[1,0]])

labels = np.array([0,1,0,1,0])

model = GaussianNB()
model.fit(data, labels)

prediction = model.predict([[1,0]])

if prediction[0] == 1:
    print("this is spam")
else: 
      print("this is not spam")