### Preamble

Hello this is my own little project for learning and practicing on Python. I choose to build a weather data acquisition app because I consider them to be a easy challenge but they also have the potential to scale in a big way.

I'm using Twitter for displaying the weather data because I previously used IFTTT service to get the weather data and tweet this in like a "service" using the hashtag of my current city, and because of that I grow a small following user base. 

By now, IFTTT limit the tweets you can send per day to 24 and that capped me by not tweeting the weather at every hour, (because I had a message that thank every one for following at a given time in the day), that's also a reason to build this and to have the potential to scale and do something else with the Twitter account and weather data.

# Tw-temp

Tw-temp is a Twitter bot that uses Beautiful Soup to gather temperature data from Yahoo Weather page (not using Yahoo API) from a specific city. Then using Twitter's API, tweets the temperature in Celcius with Twython module at every hour using Github Actions.


## Requirements

Tw-temp needs some dependencies for proper functionality:

- Beautiful Soup 4 - Web Scrapper.
- Twython - Client for Twitter's API.
- html5lib - HTML Parser.

## Usage

First sign up for Twitter Developer access using https://developer.twitter.com/

After forking this repo, you have to create some Github Secrets which are:

- CONSUMER_KEY
- CONSUMER_SECRET
- ACCESS_TOKEN
- ACCESS_TOKEN_SECRET
- YAHOO_URL

Each Secret must have the proper key generated at the Twitter's Developer page excepting the YAHOO_URL secret.

The YAHOO_URL must be a Yahoo Weather URL like this one in order to work: 

```
https://es-us.noticias.yahoo.com/clima/méxico/tamaulipas/reynosa-24552987/
```

