# 📬 Spam Filter Classifier

This project is a simple and effective **spam message classifier** built using **Python**, **CountVectorizer**, and **Multinomial Naive Bayes**. It analyzes SMS messages and predicts whether a message is **spam** or **ham (not spam)**.

## 🧠 How It Works

1. Loads a dataset of SMS messages (labeled as spam or ham)
2. Transforms text into numeric features using `CountVectorizer`
3. Trains a `MultinomialNB` (Naive Bayes) classifier
4. Evaluates model accuracy and prints classification report

## 🚀 Technologies Used

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- MultinomialNB

## 🗂️ File Overview

| File             | Description                                |
|------------------|--------------------------------------------|
| `spam_filter.py` | Main Python script with training/testing   |
| `requirements.txt` | (optional) List of required libraries    |

## 📊 Sample Output

```
Accuracy: 0.987
📊 Classification Report:
            precision    recall  f1-score   support

      0       0.99      1.00      0.99       965
      1       0.98      0.93      0.96       150

accuracy                           0.99      1115
macro avg       0.98      0.96      0.97      1115
weighted avg    0.99      0.99      0.99      1115
```


## ✅ How to Run
python spam_filter.py
Make sure you have the required libraries installed.

📌 Future Improvements
Deploy the model using Flask or FastAPI (coming soon!)

Add live prediction API

Clean and expand the dataset

🙋‍♂️ Author
Made with 💻 by Yorman Kennedy Gómez Quintero
