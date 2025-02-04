📱 Google Play Store Reviews Scraper & Analyzer
📌 Overview
This Python script fetches and analyzes user reviews for any Android app from the Google Play Store using the google-play-scraper library. It retrieves 500 reviews, saves them in an Excel file, and performs various analyses, such as rating distribution, review frequency, and sentiment analysis.

🛠 Features
✅ Scrapes reviews from the Google Play Store
✅ Saves data in an Excel file for easy access
✅ Performs data analysis, including:

Rating distribution
Total upvotes
Longest review
Review frequency by date
Most common review time
Overall sentiment analysis
🔧 Installation
1️⃣ Clone this repository

sh
Copy
Edit
git clone https://github.com/your-username/repository-name.git
cd repository-name
2️⃣ Install dependencies

sh
Copy
Edit
pip install pandas google-play-scraper openpyxl
🚀 Usage
Run the script by executing:

sh
Copy
Edit
python script_name.py
The script will:
✅ Fetch reviews for Snapchat (or any app of your choice)
✅ Save them to an Excel file (snapchat.xlsx)
✅ Print key insights in the console

📊 Output Example
mathematica
Copy
Edit
Data saved successfully!
Distribution of Ratings:
5    320
4     90
3     50
2     20
1     20
Total Number of Upvotes: 1345
Longest Review:
"This is a great app, but it sometimes crashes..."
Most Common Time for Reviews (Hour): 18
Overall Sentiment of the App: Positive
🔍 Customization
Change App: Modify the package_name in the reviews() function.
Adjust Review Count: Change count=500 to any number.
Filter Reviews by Score: Uncomment filter_score_with=5 to fetch only 5-star reviews.
📜 License
This project is licensed under the MIT License. Feel free to modify and share!

