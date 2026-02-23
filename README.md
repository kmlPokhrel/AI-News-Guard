# AI News Guard 🛡️
<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=auto&height=200&section=header&text=AI%20News%20Guard&fontSize=80&animation=fadeIn&fontAlignY=38" />
</p>

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

**AI News Guard** is a professional-grade machine learning tool designed to tackle information overload. By analyzing linguistic patterns, it distinguishes between verified reporting and fabricated clickbait, providing a "Confidence Score" and Explainable AI (XAI) insights.

---

## 📌 Table of Contents
* [🧐 Why This Matters](#-why-this-matters)
* [📸 Visual Tour](#-visual-tour)
* [⚙️ How It Works](#-how-it-works)
* [📊 Dataset & Setup](#-dataset--setup)
* [🚀 Installation & Running](#-installation--running)
* [📜 License](#-license)

---

## 🧐 Why This Matters
In an era of information overload, distinguishing between verified reporting and fabricated clickbait is a critical skill. This project utilizes **Machine Learning** to analyze linguistic patterns and provide users with a "Confidence Score" and a transparency-focused "Why" analysis.

---

## 📸 Visual Tour

### 🎥 App Demo
> *Watch the AI process news in real-time and provide instant results.*

<p align="center">
  <img src="./demo.gif" alt="App working demo" width="800">
</p>

### 🔍 Explainable AI (XAI)
> *The AI doesn't just give a result; it shows you the "Red-Flag" words it found suspicious.*

<p align="center">
  <img src="./why-explanation.png" alt="XAI Popup Screenshot" width="500">
</p>

---

## ⚙️ How It Works (The NLP Pipeline)
This application follows a standard Data Science lifecycle:

1. **Data Preprocessing:** Cleaning 40,000+ articles using `NLTK` to remove noise (stopwords, punctuation).
2. **Vectorization:** Converting text to math using **TF-IDF** (Term Frequency-Inverse Document Frequency).
3. **Classification:** A **Logistic Regression** model trained on the ISOT dataset to identify patterns.
4. **Transparency:** Using model coefficients to provide **Explainable AI** keywords for every prediction.

---

## 📊 Dataset & Setup
This project uses the **ISOT Fake News Dataset** (approx. 44,000 articles). 

1. **Download:** Get `True.csv` and `Fake.csv` from Kaggle.
2. **Placement:** Move both files into the `/data` folder.
3. **Automated Preparation:** Run the script to merge and clean the data:
   ```bash
   python prep_data.py

## 🚀 Installation & Running

### 1. Prerequisites
* **Python 3.11+**
* **XAMPP** (to manage the MySQL Database)

### 2. Clone the Repo
```bash```
# Clone the repository
git clone [https://github.com/yourusername/fake-news-detector.git](https://github.com/kmlPokhrel/fake-news-detector.git)

# Move into the project directory
cd fake-news-detector

### 3. Install Dependencies
# Install the required Python libraries

pip install -r requirements.txt

###4. Launch the app
# Run the main application
python app.py

## License
This project is licensed under the MIT License.

<p align="center">
Developed with ❤️
</p>
