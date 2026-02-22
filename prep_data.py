import pandas as pd
import os

def prepare_dataset():
    print("🚀 Starting Data Preparation...")
    
    # 1. Check if raw files exist in the /data folder
    if not os.path.exists('data/True.csv') or not os.path.exists('data/Fake.csv'):
        print("❌ Error: True.csv or Fake.csv not found in the /data folder!")
        print("👉 Please download them from: https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset")
        return

    # 2. Load the raw datasets
    true_df = pd.read_csv('data/True.csv')
    fake_df = pd.read_csv('data/Fake.csv')

    # 3. Add labels (0 for Real, 1 for Fake)
    true_df['label'] = 0
    fake_df['label'] = 1

    # 4. Combine and Shuffle
    df = pd.concat([true_df, fake_df], axis=0).reset_index(drop=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True) # Shuffle data

    # 5. Clean: Combine Title and Text into one feature
    df['full_text'] = df['title'] + " " + df['text']
    df = df[['full_text', 'label']]
    df.dropna(inplace=True)

    # 6. Save the final product
    df.to_csv('data/cleaned_news_data.csv', index=False)
    print("✅ Success! 'data/cleaned_news_data.csv' is ready for the AI.")

if __name__ == "__main__":
    prepare_dataset()