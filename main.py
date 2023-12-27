import argparse
import pandas as pd
from x_scraper import TwitterScraper

def parse_arguments():
    """
    Parses command-line arguments.

    Returns:
    - argparse.Namespace: Object containing parsed arguments
    """
    parser = argparse.ArgumentParser(description='Twitter Scraper')
    parser.add_argument('--keywords', type=str, help='Search keywords for tweets')
    parser.add_argument('--n_tweets', type=int, default=4, help='Number of tweets to retrieve (default: 4)')
    parser.add_argument('--start_date', type=str, help='Start date for retrieving tweets (YYYY-MM-DD)')

    return parser.parse_args()


if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()
    # Create an instance of the TwitterScraper class
    twitter_scraper = TwitterScraper(args.keywords, args.n_tweets, args.start_date)

    # Scrape tweets
    twitter_scraper.scrape_tweets() 
    twitter_scraper.save_data()
