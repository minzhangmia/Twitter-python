import os 
import json
import pandas as pd
import numpy as np 
os.chdir('\\\\file\\UsersM$\\mwa150\\Home\\python')
import twitter
from twitter import *

data = []
with open("atirish.json") as f:
    for line in f:
        try:
            tweet = json.loads(line)
            if tweet['text'].find('RT @')!=-1:
            # drop Retweeted tweet
                continue
            data.append(tweet)
        except:
            continue

with open('natirish.json','w') as fp:
    json.dump(data,fp)

tweets_data_path=('natirish.json')
tweets_data = []
tweets_file = open(tweets_data_path,'r')
tweets_data = json.load(tweets_file)
type(tweets_data)

df = pd.DataFrame(tweets_data)
