import tweepy
import time
key1="8glsyml5pJwdl9nT6DQ8mtT94"
key2="JBConWJ9QvpAYqXD98zSQVghwYaiF1ddO657bw1smHxINKhyd6"
key3="2698718785-mKiDBwqv5BY23TSxShl0YXzdRybG17G8bR8NK5I"
key4="W92tpDUsbQgqmUlfOUg2TPWz7cwDfFMcnDG8bYmNGQ03z"
auth = tweepy.OAuthHandler(key1, key2)
auth.set_access_token(key3, key4)
api = tweepy.API(auth)

def pare_tweets(xristis, tweets):
    user = api.get_user(xristis)
    for i in range(10):
        tweet = api.user_timeline(id = user.id, count = 100, include_rts = False)[i]
        tweets.append(tweet.text.encode('utf8'))
    return tweets
xristis1=raw_input("dose to onoma tou 1ou xristi : ")
print "please wait..."
tweetsx1=[]
pare_tweets(xristis1, tweetsx1)
xristis2=raw_input("dose to onoma tou 2ou xristi : ")
print "please wait..."
tweetsx2=[]
pare_tweets(xristis2, tweetsx2)
words1=1 +  str(tweetsx1).count(" ")
words2=1 +  str(tweetsx2).count(" ")
if (words1 < words2):
    print "perisoteres lekseis exei o xristis : ",xristis2
elif (words1 > words2):
    print "perisoteres lekseis exei o xristis : ",xristis1
else:
    print "isos arithmos lekseon"
