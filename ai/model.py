from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "สวัสดี",
    "ช่วยอะไรได้",
    "ขอบคุณ",
    "ลาก่อน"
]

labels = [
    "hello",
    "help",
    "thanks",
    "bye"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict(text):
    X_test = vectorizer.transform([text])
    result = model.predict(X_test)
    return result[0]