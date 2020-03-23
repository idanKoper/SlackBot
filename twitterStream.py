import datetime
import privateKeys
import time
import tweepy

auth = tweepy.OAuthHandler(privateKeys.TWITTER_APP_KEY, privateKeys.TWITTER_APP_SECRET)
auth.set_access_token(privateKeys.TWITTER_KEY, privateKeys.TWITTER_SECRET)
api = tweepy.API(auth)


def get_tweets(api, username):
    page = 1
    deadend = False
    tweets_before_one_hour = []
    while True:
        tweets = api.user_timeline(username, page=page)

        for tweet in tweets:
            if ((
                        datetime.datetime.now() - tweet.created_at).seconds - 7200) < 3600:  # Subtraction by 7200 to timezone 0
                tweets_before_one_hour.append(tweet.text.encode("UTF-8"))
            else:
                deadend = True
                return tweets_before_one_hour
        if not deadend:
            page + 1
            time.sleep(500)
print(get_tweets(api,"ExhibitsUSA"))
