#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tweepy, time, subprocess

#Twitter credentials
CONSUMER_KEY = 'X'
CONSUMER_SECRET = 'X'
ACCESS_KEY = 'X'
ACCESS_SECRET = 'X'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
  try:
    mentions = api.mentions_timeline(count=10)
    with open('./replies.txt','r') as f:
      replies = f.readlines()
    for i in range(len(replies)):
      replies[i] = replies[i].strip()
    for mention in mentions:
      if str(mention.id) not in replies:
        replies.append(str(mention.id))
        print(mention.text)
        text = ' '.join(mention.text.split('@kindgifs ')[1:])
        try:
          subprocess.call(['./kindgifs/kindgifs.py', text])
          if ' -p' in text:
            text = ' '.join(text.split(' -p')[:-1]) 
          fname = text.lower().replace(' ','_') + '.gif'
          print('@'+mention.user.screen_name)
          api.update_with_media(fname,status='@'+mention.user.screen_name,in_reply_to_status_id=mention.id)
          print('Reply successful! (^-^)')
          subprocess.call(['rm',fname])
        except:
          pass
    with open('replies.txt','w') as f:
      for reply in replies:
        f.write(reply + '\n')
    time.sleep(15) #Sleep for 15 seconds
  except:
    print("Something didn\'t work; trying again in 15 minutes")
    time.sleep(900)
