import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data ={
    "name": ["Badsha ", "afsu", "sarwer", "arif", "sabbir"],
    "marks": [54,65,47,34,78]
}

df = pd.DataFrame(data)

print("=== student Results ===")
print(df)
print()
print("mean marks: ", np.mean(df["marks"]))
print("max:", np.max(df["marks"]))
print("min:", np.min(df["marks"]))

df["result"] = df["marks"].apply(lambda x: "pass" if x >= 48 else "fail")
print(df)
plt.bar(df["name"],df["marks"],color=["green", "green", "red","red","green"])
plt.title("student results")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()