# X_scraper

This script is designed to scrape Twitter data based on provided keywords using ntscraper.

## Usage

1. Create and activate a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate   # For Windows

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the script with the desired parameters
   ```bash
    --keywords: Search keywords for tweets.
    --n_post: Number of tweets to retrieve.
    --delay: Start date for retrieving tweets in the format 'YYYY-MM-DD'.
4. Example
   ```bash
    python main.py --keywords 'morocco,maroc,المغرب' --n_tweets 300 
