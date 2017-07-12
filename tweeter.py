import tweepy, time

#read in your twitter authentication variables for tweepy
authStrings = open("stringsEU.txt", "r")
authStringsList = authStrings.readlines()
CONSUMER_KEY = authStringsList[0].strip()
CONSUMER_SECRET = authStringsList[1].strip()
ACCESS_KEY = authStringsList[2].strip()
ACCESS_SECRET = authStringsList[3].strip()
authStrings.close()

#setup your tweepy app with your auth strings
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def incrementNum(tweetNum, lengthTweets):
    tweetNum += 1
    if tweetNum > lengthTweets:
        tweetNum = 0
    return tweetNum

def pushTweet(twNum, tweets):
    try:
        api.update_status(tweets[twNum])
    except tweepy.TweepError as e:
        print "Something went wrong in Tweepy..."
        print e.message
    except:
        print "Something else went wrong..."

timeInterval = 1800

#get the tweet cursor
with open("cursor.txt", "r") as g:
    tweetNum = int(g.read())

#get the tweets from file, put them in a list
f = open("tweets.txt", "r")
tweets = f.readlines()
lengthTweets = len(tweets) - 1

#push out first tweet
tweetNum = incrementNum(tweetNum, lengthTweets)
pushTweet(tweetNum, tweets)

#wait half an hour
time.sleep(timeInterval)

#push out second tweet
tweetNum = incrementNum(tweetNum, lengthTweets)
pushTweet(tweetNum, tweets)

f.close()

#record new cursor
h = open("outputEU.txt", "w")
h.write(str(tweetNum))
h.close()