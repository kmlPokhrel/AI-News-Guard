import mysql.connector

class DBManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="new_db"
        )
        self.cursor = self.conn.cursor()

    def save_to_db(self, article, result, score):
        sql = "INSERT INTO predictions (article_text, result, confidence) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (article[:500], result, float(score))) 
        self.conn.commit()

    def fetch_last_five(self):
        self.cursor.execute("SELECT result, confidence, timestamp FROM predictions ORDER BY id DESC LIMIT 5")
        return self.cursor.fetchall()