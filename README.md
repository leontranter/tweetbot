# tweetbot
A simple python bot for sending out tweets on autopilot

You need a twitter app first - go create one at dev.twitter.com
When you create your app, you will need your Consumer Key, Consumer Secret, Access Key and Access Secret.
Put them into the authstrings.txt file, one line at a time, with no other characters or lines. Then save it.

Then put your tweets into the tweets.txt file, as many as you like!
Leave the cursor.txt file, you should never need to touch it. It just keeps track of what tweet you have sent out.

This bot will send out a tweet, wait half an hour, then send out another.
If you write a schedule job to run it every hour, then you are good to go. It will tweet every half hour for ever and ever.
You can change the time interval between tweets very easily if you want.
Enjoy!~