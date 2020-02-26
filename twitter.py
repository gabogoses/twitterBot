import tweepy
import time

auth = tweepy.OAuthHandler('xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxx')
auth.set_access_token('xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxx')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'GatsbyJS'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
  try:
    print('tweet liked')
    tweet.favorite()
    time.sleep(10)
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break