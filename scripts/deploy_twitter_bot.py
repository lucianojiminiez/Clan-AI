import tweepy
from scripts.tweet_bot import auto_tweet

def deploy_bot():
    print("Deploying bot to Twitter...")
    auto_tweet()
