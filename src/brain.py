import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class FakeNewsBrain:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
        self.model = LogisticRegression()
        self.train_and_evaluate()

    def train_and_evaluate(self):
        # Update path to look into the 'data' folder
        df = pd.read_csv('data/cleaned_news_data.csv') 
        df.dropna(inplace=True)
        X_train, X_test, y_train, y_test = train_test_split(df['full_text'], df['label'], test_size=0.2, random_state=42)
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_train_tfidf, y_train)

    def predict(self, text):
        transformed_text = self.vectorizer.transform([text])
        prediction = self.model.predict(transformed_text)[0]
        probability = self.model.predict_proba(transformed_text)
        confidence = round(max(probability[0]) * 100, 2)
        return ("Fake" if prediction == 1 else "Real"), confidence

    def get_explaining_keywords(self, text):
        feature_names = self.vectorizer.get_feature_names_out()
        transformed_text = self.vectorizer.transform([text])
        coefficients = self.model.coef_[0]
        word_indices = transformed_text.nonzero()[1]
        words_in_article = [(feature_names[i], coefficients[i]) for i in word_indices]
        words_in_article.sort(key=lambda x: abs(x[1]), reverse=True)
        return [word for word, score in words_in_article[:5]]