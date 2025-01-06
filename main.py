import cohere
import tweepy
import os
import time
import schedule
from dotenv import load_dotenv

load_dotenv()

# API Keys
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Initialize Tweepy client using the old API keys and access tokens
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Function to generate tweet using Cohere
def generate_tweet(prompt, max_length=280):
    try:
        response = co.generate(
            model='command',
            prompt=f"Write an engaging tweet about: {prompt}. Keep it under {max_length} characters.",
            max_tokens=50,
            temperature=0.7,
            stop_sequences=["."],
            return_likelihoods='NONE'
        )
        return response.generations[0].text.strip()[:max_length]
    except Exception as e:
        print(f"Error generating tweet: {e}")
        return None

# Function to post tweet on Twitter
def post_tweet(content):
    try:
        response = client.create_tweet(text=content)
        print(f"Successfully posted: {content}")
        return response
    except Exception as e:
        print(f"Error posting tweet: {e}")
        print(f"Error details: {str(e)}")
        return None

# Function to generate and post daily tweets
def generate_and_post_daily_tweets():
    topics = ["tech trends", "AI insights", "coding tips", "motivation", "daily thoughts"]
    for topic in topics:
        tweet = generate_tweet(topic)
        if tweet:
            post_tweet(tweet)
        time.sleep(10)

# Schedule the tweet generation and posting
def schedule_tweets():
    schedule.every().day.at("00:35").do(generate_and_post_daily_tweets)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main function
if __name__ == "__main__":
    print("Testing authentication...")
    try:
        client.get_me()  # This checks if the authentication is successful
        print("Authentication successful!")
        schedule_tweets()
    except Exception as e:
        print(f"Authentication failed: {e}")
