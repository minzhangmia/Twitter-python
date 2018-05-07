# df from previous doc

df = pd.DataFrame(tweets_data) 

# keep certain columns & create new values 
col_to_keep = ['created_at','user','lang','text','extended_tweet']
df = df[col_to_keep]
add_followers = []
add_friends = []
add_location = []
add_listed = []
add_geo = []
add_id = []
add_name = []
add_screename = []

# extract elements from dataframe series 
for index, row in df.iterrows():
    fo = (row['user']['followers_count'])
    fr = (row['user']['friends_count'])
    lo = (row['user']['location'])
    li = (row['user']['listed_count'])
    ge = (row['user']['geo_enabled'])
    id = (row['user']['id'])
    na = (row['user']['name'])
    sc = (row['user']['screen_name'])
    
    add_followers.append(fo)
    add_friends.append(fr)
    add_location.append(lo)
    add_listed.append(li)
    add_geo.append(ge)
    add_id.append(id)
    add_name.append(na)
    add_screename.append(sc)

    
df['followers'] = add_followers
df['friends'] = add_friends
df['location'] = add_location
df['listed'] = add_listed
df['geo'] = add_geo
df['id'] = add_id
df['name'] = add_name
df['screen_name'] = add_screename
df['ideology_pre'] = ''
