from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB
import warnings
warnings.filterwarnings("ignore")


emails = [
    "win free money",
    "hello friend, how are you?",
    "limited time offer, buy now",
    "meeting at 10am tomorrow",
    "congratulations, you have won a prize",
    "see you at lunch",
    "click here to claim prize",
    "how was your weekend?",
    "free gift waiting for you",
    "project meeting tomorrow"
]

labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]




vectorizer = CountVectorizer()
x = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(x,labels)

new_email = [
    "free money for you",
    "let's catch up over coffee",
    "exclusive offer just for you",
    "project deadline is next week",
]

x_new = vectorizer.transform(new_email)
predictions = model.predict(x_new)

for email, pred in zip(new_email, predictions):
    if pred ==1:
        print(email, "is likely spam.")
    else:
        print(email, "is likely not spam.")