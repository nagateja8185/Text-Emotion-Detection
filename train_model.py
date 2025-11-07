import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# --- Clean Text ---
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()

# --- Load Dataset ---
df = pd.read_csv("emotion_dataset.csv")
df['Clean_Text'] = df['Text'].apply(clean_text)

# --- Split Data ---
X = df['Clean_Text']
y = df['Emotion']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# --- Train Model ---
pipe_lr = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
    ('lr', LogisticRegression(max_iter=400))
])

pipe_lr.fit(x_train, y_train)
acc = pipe_lr.score(x_test, y_test)
print(f"✅ Model trained successfully! Accuracy: {acc:.3f}")

print("\nClassification Report:\n")
y_pred = pipe_lr.predict(x_test)
print(classification_report(y_test, y_pred))

joblib.dump(pipe_lr, "text_emotion.pkl")
print("💾 Model saved as text_emotion.pkl")
