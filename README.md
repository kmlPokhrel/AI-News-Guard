# AI News Guard 🛡️
<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=auto&height=200&section=header&text=AI%20News%20Guard&fontSize=90&animation=fadeIn&fontAlignY=38" />
</p>

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![NLP](https://img.shields.io/badge/NLP-NLTK%20%7C%20TF--IDF-green.svg) ![ML](https://img.shields.io/badge/Model-Logistic%20Regression-orange.svg)

**AI News Guard** is a machine learning tool designed to tackle information overload. By analyzing linguistic patterns, it distinguishes between verified reporting and fabricated clickbait.

---

## 🎥 App in Action
> **How it works:** Paste a news snippet, and the AI calculates a confidence score while highlighting suspicious "red-flag" keywords.

<p align="center">
  <img src="./demo.gif" alt="App Demo" width="800">
</p>

---

## ✨ Key Features
* **Real-Time Detection:** Instant classification of news articles as "Real" or "Fake".
* **Confidence Scoring:** Probability percentages to show model certainty.
* **Explainable AI (XAI):** Highlights specific words that triggered the "Fake" classification.
* **History Log:** Automatically saves your recent checks.

---

## ⚙️ How It Works (The NLP Pipeline)
The engine processes text through four critical stages:
1.  **Preprocessing:** `NLTK` cleans 40,000+ articles (removing stop-words and noise).
2.  **Vectorization:** Text is converted to math using **TF-IDF**.
3.  **Classification:** A **Logistic Regression** model trained on the ISOT dataset.
4.  **Transparency:** Model coefficients are mapped back to words to show you *why* a result was chosen.

---

## 📊 Dataset Setup
This project uses the **ISOT Fake News Dataset**. 
1.  **Download:** `True.csv` and `Fake.csv` from [Kaggle](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets).
2.  **Placement:** Save them in a `/data` folder.
3.  **Run Prep:** ```bash
    python prep_data.py
    ```

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone [https://github.com/yourusername/fake-news-detector.git](https://github.com/yourusername/fake-news-detector.git)
cd fake-news-detector
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
