from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """
Afsana is my love, and im in love with afsana, Afsana is my part of my life, 
I will go one day kolkata for my love Afsana, i made a rose gerden for Afsu 
i build body for Afsana, i am working hard for Afsana, i will do anything
 for Afsana, i will do anything for my love Afsana, i will do anything for my love Afsana, i will do anything
"""

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Word Cloud")
plt.show()