#!/usr/bin/python2.7
import tweepy
from pyowm import OWM

#Twitter API Keys
consumer_key = "twitter-consumer-key"
consumer_secret = "twitter-consumer-secret-key"
access_token = "twitter-access-token"
access_token_secret = "twitter-access-token-secret"

#Twitter Authentication
auth = tweepy.OAuthHandler(owmconsumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Open Weather Map API 
API_key = 'owm-api-key'
owm = OWM(API_key)

#quick variables to check weather in London
obs = owm.weather_at_place('London,uk')
w = obs.get_weather()
weather = w.get_status()

# Weather Emoji
Clouds = u'\U00002601'
Clear = u'\U00002600'
Rain =  u'\U00002614'
Extreme =  u'\U0001F300'
Snow = u'\U00002744'
Thunderstorm = u'\U000026A1'
Mist = u'\U0001F32B'
Haze = u'\U0001F324'
notsure = u'\U0001F648'


#Check Weather and return relevant Emoji
if weather == "Clouds":
    api.update_profile("chiubaca_bot "+ Clouds,"chiubaca.github.io","London",bio + counter +"/100")
elif weather == "Clear":
    api.update_profile("chiubaca_bot "+ Clear,"chiubaca.github.io","London",bio + counter+"/100")
elif weather == "Rain":
    api.update_profile("chiubaca_bot "+ Rain,"chiubaca.github.io","London",bio + counter+"/100")
elif weather == "Extreme":
    api.update_profile("chiubaca_bot "+ Extreme,"chiubaca.github.io","London",bio + counter+"/100")
elif weather == "Snow":
    api.update_profile("chiubaca_bot "+ Snow,"chiubaca.github.io","London",bio + counter+"/100")
elif weather == "Thunderstorm":
    api.update_profile("chiubaca_bot "+ Thunderstorm,"chiubaca.github.io","London",bio + counter+"/100")
elif weather == "Haze":
    api.update_profile("chiubaca_bot "+ Haze,"chiubaca.github.io","London",bio + counter+"/100")
elif weather == "Mist":
    api.update_profile("chiubaca_bot "+ Mist,"chiubaca.github.io","London",bio + counter+"/100")
else:
    api.update_profile("chiubaca_bot "+ notsure,"chiubaca.github.io","London",bio + counter+"/100")

print Clear+Rain+Extreme+Clouds+Snow+Thunderstorm+Haze+Mist+notsure
print("updated!")