import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = {
    "age": [40,20,26,35,28,45,18,55],
    "gender": [0,1,1,1,0,0,1,0],
    "class": [3,1,3,1,3,2,3,2],
    "survived": [0,1,1,1,0,1,0,0]
}

df = pd.DataFrame(data)

x = df[["age","gender","class"]]
y = df["survived"]

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

person1 = [[40, 0, 3]]
prediction1 = model.predict(person1)
if prediction1[0] == 1:
    print("person 1: survived!")
else:
    print("person 1: did not survive!")

person2 = [[20, 1, 1]]
prediction2 = model.predict(person2)
if prediction2[0] == 1:
    print("person 2: survived!")
else:
    print("person 2: did not survive!")