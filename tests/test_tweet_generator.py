import pytest
from ai.tweet_generator import generate_tweet

def test_generate_tweet():
    tweet = generate_tweet("Uzumaki", "Never give up!")
    assert "Uzumaki" in tweet
    assert "Never give up!" in tweet
    assert len(tweet) > 0  # Ensure tweet is not empty
