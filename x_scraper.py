import os
import pandas as pd
from ntscraper import Nitter

class TwitterScraper:
    def __init__(self, keyword, n_tweets=300):
        """
        Initialize the TwitterScraper instance.

        Parameters:
        - keyword (str): The search keyword for tweets.
        - n_tweets (int): The number of tweets to retrieve (default is 300).
        - since (str): The start date for retrieving tweets in the format 'YYYY-MM-DD'.
        """
        self.keyword = keyword
        self.n_tweets = n_tweets
        self.data = None

    def scrape_tweets(self):
        """
        Scrape tweets using the Nitter library based on the provided keywords and parameters.
        """
        try:
            scraper = Nitter(0)
            tweets = scraper.get_tweets(self.keyword, number=self.n_tweets)

            data = []
            for tweet in tweets['tweets']:
                data.append({
                    'link': tweet['link'],
                    'text': tweet['text'],
                    'name': tweet['user']['name'],
                    'username': tweet['user']['username'],
                    'date': tweet['date'],
                    'comments': tweet['stats']['comments'],
                    'retweets': tweet['stats']['retweets'],
                    'quotes': tweet['stats']['quotes'],
                    'likes': tweet['stats']['likes'],
                })

            self.data = pd.DataFrame(data)
        except Exception as e:
            print(f"Error while scraping tweets: {e}")

    def save_data(self):
        """
        Saves data to a CSV file within the 'data' folder.
        """
        try:
            # Check if the 'data' folder exists, and create it if not
            data_dir = './data'
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)

            # Save the DataFrame to a CSV file within the 'data' folder
            csv_path = os.path.join(data_dir, f'X_data_{self.keyword}.csv')
            self.data.to_csv(csv_path, index=False)
        except Exception as e:
            print(f"Error while saving data to CSV: {e}")