import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = ""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class PrintListener(StreamListener):
    def on_status(self,status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                 status.created_at,
                status.source,
                '\n')
        def on_error(self,status_code):
            print("Error code: {}".format(status_code))
            return True
        def on_timeout(self):
            print('Listener timed out')
            return True


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth,listener)
    language = ('en',)
    stream.sample(languages=language)

def pull_down_tweets(screen_name):
    api = API(auth)
    tweets=api.user_timeline(screen_name=screen_name,count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json,indent=4))

if __name__=='__main__':
    pull_down_tweets(auth.username)

