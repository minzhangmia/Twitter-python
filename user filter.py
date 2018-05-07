# df found from previous doc 
# twitter user filters

df = df.loc[df['lang'] == 'en'] # tweet only in English 


pd.set_option('float_format','{:f}'.format)
df.describe()

df = df[df['followers'] >= 25] # follow 25 or more other accounts 
df = df[df['friends'] >=50] # have at least 50 friends 
df = df[df['listed'] >= 3] # have sent more than 3 tweets