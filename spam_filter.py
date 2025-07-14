import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
data = pd.read_csv(url, sep="\t", names=["label", "message"])

data['label'] = data['label'].map({'ham': 0, 'spam': 1})

X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_counts, y_train)

y_pred = model.predict(X_test_counts)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

samples = ["Congratulations! You've won a free ticket!", "Can we reschedule our meeting?"]
sample_counts = vectorizer.transform(samples)
predictions = model.predict(sample_counts)

for msg, pred in zip(samples, predictions):
    print(f"\n🔍 Message: {msg}")
    print("Prediction", "Spam" if pred == 1 else "Ham")

