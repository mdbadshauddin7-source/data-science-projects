import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("titanic/train.csv")

df = df[["Pclass", "Sex", "Age", "Survived"]].dropna()
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

X = df[["Pclass", "Sex", "Age"]]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=500)
model.fit(X_train, y_train)

print("Accuracy:", round(model.score(X_test, y_test) * 100, 2), "%")
importance = pd.DataFrame({
    "Feature": ["Pclass", "Sex", "Age"],
    "Importance": model.feature_importances_
})
print(importance.sort_values("Importance", ascending=False))