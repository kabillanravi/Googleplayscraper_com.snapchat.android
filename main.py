import pandas as pd
from google_play_scraper import reviews, Sort
from datetime import datetime

# Fetch reviews from Google Play Store
result, _ = reviews(
    'com.snapchat.android',
    lang='en',  # Language
    country='us',  # Country
    sort=Sort.NEWEST,  # Sort by newest
    count=500,  # Number of reviews
    #filter_score_with= 5  # Only 5-star reviews
)

# Convert the fetched reviews into a DataFrame
reviews_df = pd.DataFrame(result)

# Save the DataFrame to an Excel file
reviews_df.to_excel("/Users/kabilanravi/Desktop/snapchat.xlsx", index=False)
print("Data saved successfully!")

# Perform analysis on the fetched data
# Convert 'at' column to datetime
reviews_df['at'] = pd.to_datetime(reviews_df['at'])

# 1. Distribution of Ratings
rating_distribution = reviews_df['score'].value_counts()
print("Distribution of Ratings:\n", rating_distribution)

# 2. Total Number of Upvotes
total_upvotes = reviews_df['thumbsUpCount'].sum()
print("Total Number of Upvotes:", total_upvotes)

# 3. Male-to-Female Distribution (Not possible without gender data)
print("Male-to-Female Distribution: Cannot be determined from the given data.")

# 4. Longest Review
reviews_df['content_length'] = reviews_df['content'].apply(len)
longest_review = reviews_df.loc[reviews_df['content_length'].idxmax()]
print("Longest Review:\n", longest_review['content'])

# 5. Frequency of Reviews
reviews_df['date'] = reviews_df['at'].dt.date
review_frequency = reviews_df['date'].value_counts().sort_index()
print("Frequency of Reviews:\n", review_frequency)

# 6. Most Common Time for Reviews
reviews_df['hour'] = reviews_df['at'].dt.hour
most_common_hour = reviews_df['hour'].mode()[0]
print("Most Common Time for Reviews (Hour):", most_common_hour)

# 7. Overall Sentiment of the App
overall_sentiment = "Positive" if reviews_df['score'].mean() >= 4 else "Negative"
print("Overall Sentiment of the App:", overall_sentiment)