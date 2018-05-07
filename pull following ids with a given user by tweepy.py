import twitter
from twitter import *
import time
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

twitter = Twitter(
                                auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

auth = tweepy.OAuthHandler('*', '*')
auth.set_access_token('8', '*')

api = tweepy.API(auth)

# Twitter IDs relevant to Irish rugby 
# @irishrugby => 90430970, @independent_ie => 91334232, @ireland_rugby => 19682969, @irelandrl => 186064140
# @indorugby => 960502116, @kearneyrob => 240663429, @seanobrien1987 => 385340015, @andrew_trimble => 74224730
# @rorybest2 => 186134940, @seancronin2 => 182456993, @keithearls87 => 1425280544, @tadhgfurlong => 47357818
# @henshawrob => 875852118, @kearneyrob => 240663429, @iankeatley => 283690548, @davidkilcoyne1 => 634121910
# @kieranmarmion => 282062309, @jordimurphy => 216349556, @cjstander => 241093180, @devintoner4 => 182470142
# @treadz5 => 1499215891, @ringrose_g => 342363634, @conormurray_9 => 412490976, @fergmcfadden => 561976148, @properchurch => 208490036

irish_list = [90430970,91334232,19682969,186064140,960502116,240663429,385340015,74224730,
186134940,182456993,1425280544,47357818,875852118,240663429,283690548,634121910,282062309,
216349556,241093180,182470142,1499215891,342363634,412490976,561976148,208490036]

screen_name = '*'

ids = []

for page in tweepy.Cursor(api.friends_ids, screen_name=screen_name).pages():
    ids.extend(page)

print(ids)

