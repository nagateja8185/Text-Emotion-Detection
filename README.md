# 🧠 Text Emotion Detection Web Application

## 📌 Project Title and Description
The **Text Emotion Detection Web Application** is a machine-learning–powered tool designed to analyze any user-provided text and determine the underlying emotion.  
It offers a clean, interactive, and modern UI with features like animated probability bars, emojis, prediction history, and a dark/light mode toggle.

### ✅ Key Features
- ML-powered emotion prediction (8 emotions)
- Beautiful UI with fully separated cards
- Emoji-enhanced results 😄😢😡😐
- Dark/Light mode toggle 🌗
- Animated probability bars 📊
- Collapsible history section 📜
- Clear history option 🧹
- Lightweight backend using Python’s `http.server`
- Fully laptop-friendly interface

---

## 📚 Table of Contents
1. [Project Title and Description](#-project-title-and-description)  
2. [Table of Contents](#-table-of-contents)  
3. [Installation Instructions](#-installation-instructions)  
4. [Usage Instructions](#-usage-instructions)  
5. [Contributing Guidelines](#-contributing-guidelines)  
6. [License](#-license)  
7. [Credits and Acknowledgments](#-credits-and-acknowledgments)  
8. [Contact Information](#-contact-information)  
9. [Project Status](#-project-status)  
10. [Known Issues or Limitations](#-known-issues-or-limitations)

---

# ⚙ Installation Instructions

## ✅ 1. Install Required Python Libraries
Make sure Python 3.8+ is installed.

Install dependencies:
```bash
pip install scikit-learn pandas numpy joblib
```

## ✅ 2. Ensure the Model is Available
Place your trained model file at:
```
model/text_emotion.pkl
```

## ✅ 3. Project Structure
```
Text_Emotion_Detection/
│
├── model/
│   └── text_emotion.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── emotion_dataset.csv
├── predict_emotion.py
├── train_model.py
├── Text_Emotion_Detection.ipynb 
└── server.py
```

## ✅ 4. Run the Server
From the project root directory:
```bash
python server.py
```

Expected server output:
```
🚀 Server running at http://localhost:8000
📂 Serving frontend from /frontend/index.html
```

## ✅ 5. Open in Your Browser
Visit:
```
http://localhost:8000/
```
Your Text Emotion Detection UI should now be live ✅

---

# 🧪 Usage Instructions

### ✅ Step 1: Enter Text
Type any sentence into the input field.

Example:
```
I am feeling so excited today!
```

### ✅ Step 2: Click “Submit” 🚀
The app will display:
- 🎯 Predicted emotion  
- 📈 Confidence score  
- 📊 Full emotion probability distribution  
- 😄 Emoji representing the emotion  
- 📜 Added entry in prediction history  

### ✅ Step 3: View Prediction History
Use the collapsible “Prediction History” section.

### ✅ Step 4: Clear History
Click the **🧹 Clear** button anytime.

---

# 🤝 Contributing Guidelines

We welcome contributions!

### ✅ How to Contribute
1. Fork this repository  
2. Create a new feature branch  
3. Commit your changes  
4. Submit a pull request  

### ✅ Code Style Guidelines
- Use meaningful variable names  
- Maintain consistent formatting  
- Comment where necessary  
- Test your code before submitting  

### ✅ Reporting Issues
Open a GitHub issue and provide:
- Description of the bug  
- Steps to reproduce  
- Screenshots (if applicable)

---

# 6. 📄 License
This project is distributed under the **MIT License**, which allows reuse, modification, and distribution with proper attribution.

---

# 7. 🙌 Credits and Acknowledgments
Developed by **Nagateja**.  
Special thanks to:
- Scikit-learn community  
- Open-source developers  
- UI/UX inspirations from modern dashboard apps  

---

# 8. 📞 Contact Information
For support or queries:
 
🌐 GitHub — https://[github.com/your-profile](https://github.com/nagateja8185)  
🧠 Project Maintainer — Nagateja  

---

# 9. 📌 Project Status
✅ **Actively Developed**  
New UI enhancements and ML upgrades planned.

---

# 10. ⚠ Known Issues or Limitations
- Works best with English text  
- May misinterpret sarcasm or slang  
- Currently supports local hosting only  
- No database integration for long-term history storage  

---

# ✅ Thank You for Using This Project!
Feel free to ⭐ star the repository if you found it useful!
