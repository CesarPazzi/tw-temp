print("TRYING TO IMPORT LIBRARIES")
try:
    import bs4 as bs
    import urllib.request
    from twython import Twython
    from datetime import datetime
    import os
    import pytz

except:
    print("ERROR! COULD NOT IMPORT LIBRARIES")

######### GLOBALS ######### 

try:
    yahoo_url = os.environ['YAHOO_URL']
    url = urllib.request.urlopen(yahoo_url).read()
    page = bs.BeautifulSoup(url, "html5lib")
    fecha = datetime.now(pytz.timezone('US/Central'))

except:
    print("ERROR! COULD NOT SET GLOBALS")

print("----------------------------------")

######### FUNCTIONS ######### 

def GetTempC():
    a = page.find("span", {"data-reactid": "37"}).get_text()
    c = (int(a)-32)*5/9

    return(round(float(c)))

def GetClima():
    a = page.find("span", {"data-reactid": "26"}).get_text()

    return(str(a))


######### TWYTHON CONFIG ######### 

# Github Secrets
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

######### MAIN ######### 

if __name__ == "__main__":
    try:
        temp = GetTempC()
        clima = GetClima()
    except:
        print("ERROR! GetTempC() or GetClima() Failed!")

    message = "El clima en #Reynosa #reynosafollow es '"+str(clima)+"' con una temperatura de: '"+str(temp)+"°C' ("+fecha.strftime("%H:%M")+"hrs.)"
    twitter.update_status(status=message)
    print("Se tuiteo: %s" % message)

    pass
