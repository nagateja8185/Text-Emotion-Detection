import joblib
import re

# --- Load Model ---
pipe_lr = joblib.load("text_emotion.pkl")

# --- Clean Text ---
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()

# --- Predict Function ---
def predict_emotion(text):
    text_clean = clean_text(text)
    pred = pipe_lr.predict([text_clean])[0]
    return pred

# --- Run Interactive Input ---
while True:
    text = input("Enter text (or 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    print(f"Predicted Emotion: {predict_emotion(text)}\n")
