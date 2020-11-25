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

The YAHOO_URL must be a Yahoo Weather URL like this one: https://es-us.noticias.yahoo.com/clima/m%C3%A9xico/tamaulipas/reynosa-24552987/ in order to work.

