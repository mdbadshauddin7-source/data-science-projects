import pandas as pd
import numpy as np

data = {
    "name": ["Afsu", "Badsha", "joy", None, "Afsu"],
    "age": [20, 999, 30, 22, 20],
    "salary": [50000, 60000, None, 45000, 50000]
}

df = pd.DataFrame(data)

print("=== আসল data ===")
print(df)


# খালি name ঠিক করো
df["name"] = df["name"].fillna("Unknown")

# খালি salary ঠিক করো
df["salary"] = df["salary"].fillna(df["salary"].mean())

print("=== খালি জায়গা ঠিক করার পর ===")
print(df)

# 100 এর বেশি বয়স ভুল — গড় দিয়ে বদলাও
df.loc[df["age"] > 100, "age"] = int(df["age"].mean())

print("=== ভুল বয়স ঠিক করার পর ===")
print(df)

df = df.drop_duplicates()

print("=== Duplicate বাদ দেওয়ার পর ===")
print(df)