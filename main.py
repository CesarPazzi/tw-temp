print("TRYING TO IMPORT LIBRARIES")
try:
    import bs4 as bs
    import requests
    import tweepy
    from datetime import datetime
    import os
    import pytz
    print("DONE")

except:
    print("ERROR! CANNOT NOT IMPORT LIBRARIES")

######### GLOBALS ######### 
print("SETTING GLOBALS")
try:
    yahoo_url = os.environ['YAHOO_URL']
    url = requests.get(yahoo_url).text
    page = bs.BeautifulSoup(url, "html5lib")
    fecha = datetime.now(pytz.timezone('US/Central'))
    print("DONE")

except:
    print("ERROR! CANNOT NOT SET GLOBALS")

print("----------------------------------")

######### FUNCTIONS ######### 

def GetTempC():
    a = page.find("span", {"Va(t) D(n) celsius celsius_D(b)"}).get_text()
    #Fahrenheit to Celsius
    #c = (int(a)-32)*5/9
    #return(round(float(c)))
    print(a)
    return(a)

def GetClima():
    a = page.find("p", {"Fz(1.40rem)--miw1024 Fz(1.12rem)"}).get_text()
    print(a)
    return(str(a))


######### TWYTHON CONFIG ######### 

# Github Secrets

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

twitter = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


######### MAIN ######### 

if __name__ == "__main__":

        temp = GetTempC()
        clima = GetClima()
        message = "El clima en #Reynosa #reynosafollow es '"+str(clima)+"' con una temperatura de: '"+str(temp)+"°C' ("+fecha.strftime("%H:%M")+"hrs.)"

        twitter.create_tweet(text=message)
        print("Se tuiteo: %s" % message)
        print(f"https://twitter.com/user/status/{twitter.data['id']}")
        # print("ERROR TRYING TO SEND THE TWEET!")

        # print("ERROR! GetTempC() or GetClima() Failed!")

