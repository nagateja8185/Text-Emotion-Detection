import http.server
import socketserver
import os
import json
from urllib.parse import urlparse, parse_qs
from joblib import load

# --- CONFIG ---
PORT = 8000
FRONTEND_DIR = "frontend"
MODEL_PATH = "model/text_emotion.pkl"

# --- Load your trained model ---
try:
    pipe_lr = load(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("⚠️ Model could not be loaded:", e)
    pipe_lr = None

# --- Custom Handler ---
class EmotionHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect root ("/") to frontend/index.html
        if self.path == "/":
            self.path = "/index.html"

        # Serve files from frontend folder
        if self.path.startswith("/"):
            self.path = FRONTEND_DIR + self.path

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/predict":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode("utf-8"))
            text = data.get("text", "")

            if not text:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "No text provided"}).encode())
                return

            # Default fallback (if model not loaded)
            if not pipe_lr:
                fake_response = {
                    "text": text,
                    "prediction": "neutral",
                    "confidence": 0.0,
                    "probabilities": {
                        "anger": 0.0,
                        "disgust": 0.0,
                        "fear": 0.0,
                        "joy": 0.0,
                        "neutral": 1.0,
                        "sadness": 0.0,
                        "shame": 0.0,
                        "surprise": 0.0
                    }
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(fake_response).encode())
                return

            # --- Prediction using model ---
            pred = pipe_lr.predict([text])[0]
            prob = pipe_lr.predict_proba([text])[0]
            emotions = pipe_lr.classes_
            probabilities = {emo: float(p) for emo, p in zip(emotions, prob)}
            confidence = float(max(prob))

            response = {
                "text": text,
                "prediction": pred,
                "confidence": confidence,
                "probabilities": probabilities
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404)

# --- Start Server ---
with socketserver.TCPServer(("", PORT), EmotionHandler) as httpd:
    print(f"🚀 Server running at: http://localhost:{PORT}")
    print(f"📂 Serving frontend from: /{FRONTEND_DIR}/index.html")
    httpd.serve_forever()
