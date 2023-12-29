import argparse
import pandas as pd
from utils import merge_csv_files
from x_scraper import TwitterScraper

def parse_arguments():
    """
    Parses command-line arguments.

    Returns:
    - argparse.Namespace: Object containing parsed arguments
    """
    parser = argparse.ArgumentParser(description='Twitter Scraper')
    parser.add_argument('--keywords', type=str, help='Search keywords for tweets')
    parser.add_argument('--n_tweets', type=int, default=300, help='Number of tweets to retrieve (default: 300)')

    return parser.parse_args()


if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()
    # Split keywords into a list if it's provided
    keywords = args.keywords.split(',') if args.keywords else []
    # Create an instance of the TwitterScraper class
    for k in keywords:
        twitter_scraper = TwitterScraper(k, args.n_tweets)
        # Scrape tweets
        twitter_scraper.scrape_tweets() 
        twitter_scraper.save_data()

    merge_csv_files('./data', 'X_data.csv')
