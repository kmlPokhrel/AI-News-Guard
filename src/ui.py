import customtkinter as ctk
from tkinter import messagebox
from src.database import DBManager # Import your classes
from src.brain import FakeNewsBrain

class NewsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI News Guard Pro v2.0")
        self.geometry("600x700")
        
        # Splash Screen Label
        self.loading_label = ctk.CTkLabel(self, text="AI is reading 40,000 articles...\nPlease wait.", font=("Arial", 20, "bold"))
        self.loading_label.pack(expand=True)
        self.update() 

        # Init components
        self.db = DBManager()
        self.brain = FakeNewsBrain()

        self.loading_label.destroy()
        self.setup_ui()
        self.refresh_history()

    def setup_ui(self):
        ctk.CTkLabel(self, text="Fake News Detector", font=("Arial", 24, "bold")).pack(pady=20)
        self.textbox = ctk.CTkTextbox(self, width=500, height=200)
        self.textbox.pack(pady=10)

        # Main Analyze Button
        self.btn = ctk.CTkButton(self, text="Analyze & Save", command=self.process_news, fg_color="#1f538d")
        self.btn.pack(pady=15)

        # Version 2.0 Feature: Explanation Button
        self.explain_btn = ctk.CTkButton(self, text="Show Why (AI Logic)", command=self.show_explanation, fg_color="gray", state="disabled")
        self.explain_btn.pack(pady=5)

        self.result_label = ctk.CTkLabel(self, text="Status: Ready", font=("Arial", 16))
        self.result_label.pack(pady=5)

        self.history_frame = ctk.CTkScrollableFrame(self, width=500, height=150, label_text="Database History")
        self.history_frame.pack(pady=20)

    def process_news(self):
        text = self.textbox.get("1.0", "end-1c")
        if not text.strip(): return

        verdict, score = self.brain.predict(text)
        color = "#ff4d4d" if verdict == "Fake" else "#2ecc71"
        self.result_label.configure(text=f"Result: {verdict} ({score}%)", text_color=color)
        
        # Enable the Explanation button now that we have a result
        self.explain_btn.configure(state="normal")

        self.db.save_to_db(text, verdict, score)
        self.refresh_history()

    def show_explanation(self):
        """Displays a popup explaining the AI's keywords."""
        text = self.textbox.get("1.0", "end-1c")
        keywords = self.brain.get_explaining_keywords(text)
        
        msg = "The AI looked at these specific words to make its decision:\n\n"
        for word in keywords:
            msg += f"• {word}\n"
        
        messagebox.showinfo("Explainable AI Logic", msg)

    def refresh_history(self):
        for widget in self.history_frame.winfo_children(): widget.destroy()
        data = self.db.fetch_last_five()
        for row in data:
            time_str = row[2].strftime("%H:%M")
            display_text = f"[{time_str}] {row[0]} - {row[1]}% confidence"
            ctk.CTkLabel(self.history_frame, text=display_text).pack(anchor="w", padx=10)