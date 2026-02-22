# 🛡️ AI News Guard: Real-Time Misinformation Detector

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

### 🧐 Why This Matters
In an era of information overload, distinguishing between verified reporting and fabricated clickbait is a critical skill. This project utilizes **Machine Learning** to analyze linguistic patterns and provide users with a "Confidence Score" and a transparency-focused "Why" analysis.

---

## 📸 Visual Tour
*Place your screenshots here to show off the UI!*
> **[Insert GUI Main Dashboard Screenshot Here]**
> *The modern dark-themed interface with text input and real-time history.*

> **[Insert "Why is this Fake?" Popup Screenshot Here]**
> *Explainable AI (XAI) feature showing red-flag keywords.*

---

## ⚙️ How It Works (The NLP Pipeline)
This application follows a standard Data Science lifecycle:
1. **Data Preprocessing:** Cleaning 40,000+ articles using NLTK to remove noise (stopwords, punctuation).
2. **Vectorization:** Converting text to math using **TF-IDF** (Term Frequency-Inverse Document Frequency).
3. **Classification:** A **Logistic Regression** model trained on the ISOT dataset to identify patterns.
4. **Transparency:** Using model coefficients to provide **Explainable AI** keywords for every prediction.

---

## 🚀 Installation & Setup

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/yourusername/fake-news-detector.git](https://github.com/yourusername/fake-news-detector.git)
   cd fake-news-detector
