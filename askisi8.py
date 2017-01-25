
import tweepy
import time
key1="8glsyml5pJwdl9nT6DQ8mtT94"
key2="JBConWJ9QvpAYqXD98zSQVghwYaiF1ddO657bw1smHxINKhyd6"
key3="2698718785-mKiDBwqv5BY23TSxShl0YXzdRybG17G8bR8NK5I"
key4="W92tpDUsbQgqmUlfOUg2TPWz7cwDfFMcnDG8bYmNGQ03z"
auth = tweepy.OAuthHandler(key1, key2)
auth.set_access_token(key3, key4)
api = tweepy.API(auth)

def pare_followers(filoi, xristis):
    user = api.get_user(xristis)
    for follower in user.followers_ids(xristis):
        filoi.append(follower)
    return filoi
xristis1=raw_input("dose to onoma tou 1ou xristi : ")
filoi1=[]
filoi2=[]
filoi1 = pare_followers(filoi1, xristis1)
xristis2=raw_input("dose to onoma tou 2ou xristi : ")
filoi2 = pare_followers(filoi2, xristis2)
koinoi=[]
for i in filoi1:
    for j in filoi2:
        if (i==j):
            akolouthos = api.get_user(i).screen_name
            koinoi.append(akolouthos)
print "oi koinoi filoi einai: ", koinoi
