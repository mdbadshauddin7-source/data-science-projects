import pandas as pd 
import warnings 
warnings.filterwarnings("ignore")
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("titanic/train.csv")

print(df.head())
print("total data:",len(df))

df = df[["Pclass","Sex","Age","Survived"]].dropna()
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

x = df [["Pclass","Sex","Age"]]
y = df["Survived"]

from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

print("Accuracy:",round(model.score(x_test, y_test)*100,2),"%")

new = [[1, 1,25]]
prediction = model.predict(new)

if prediction[0]==1:
    print("person: survived!")
else:
    print("person: did not survived!")

person1 = [[3,0,40]]
prediction = model.predict(person1)  
if prediction[0]==1:
    print("person 1 : survived!")
else:
    print("person 1 : did not survived!")

person2 = [[1,1,20]]      
prediction = model.predict(person2)
if prediction[0]==1:
    print("person 2 : survived!")
else:
    print("person 2 : did not survived!")