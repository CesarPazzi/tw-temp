print("TRYING TO IMPORT LIBRARIES")
from bs4 import BeautifulSoup
import requests
import tweepy
from datetime import datetime
import os
from pytz import timezone
import sqlite3
print("DONE")
print("")
######### GLOBALS ######### 
print("SETTING GLOBALS")
yahoo_url = os.environ['YAHOO_URL']


url = requests.get(yahoo_url)
page = BeautifulSoup(url.content, "html5lib")

fecha = datetime.now(timezone('US/Central'))
print("DONE")
print("")

print("----------------------------------")
print("SETTING VARIABLES")
print("")
######### VARIABLES ######### 
temp_celsius = page.select_one("span.Va\(t\).D\(n\).celsius.celsius_D\(b\)").text
weather = page.find('p', {'class': 'Fz(1.40rem)--miw1024 Fz(1.12rem)'}).text.strip()
now = datetime.now(timezone('US/Central'))
today = datetime.now(timezone('US/Central')).date()
temp_sens = page.find("dd", class_="D(n) celsius_D(b)").text.replace("°","")
humidity = page.find_all("div",class_="D(f) Py(8px) Bdb Bdbs(d) Bdbw(1px) Bdbc($weatherBorderColor) Jc(sb)")[1].find("dd").text.replace("%","")
visibility = page.find_all("div",class_="D(f) Py(8px) Bdb Bdbs(d) Bdbw(1px) Bdbc($weatherBorderColor) Jc(sb)")[2].find("dd", class_="D(n) kilometers_D(b)").text.replace(" km","")
time = now.strftime("%I:%M %p")
print("PRINTING VARIABLES")
print("")
print(temp_celsius)
print(weather)
print(f'{today}')
print(time)
print(temp_sens)
print(humidity)
print(visibility)
print("")
print("DONE")
print("----------------------------------")
print("")

print("SETTING TWEEPY")

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

twitter = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
print("DONE")
print("")
print("----------------------------------")
######### INSERTING IN DATABASE ######### 
conn = sqlite3.connect('ReyWea23.db') #connecting to the database named "Reynosa Weather 2023" in this case.
c = conn.cursor() #creating a cursor that can execute SQL commands, which is also part of the connection object.
c.execute("CREATE TABLE IF NOT EXISTS Weather(id INTEGER PRIMARY KEY AUTOINCREMENT, temp_celsius INTEGER, weather TEXT, today DATE, time TIMESTAMP, temp_sens INTEGER, humidity INTEGER, visibility REAL)")
#creating a table named "Weather" with columns "id", "temp_celsius", "weather", "today" and "time" respectively. 
    
try:
    c.execute("INSERT INTO Weather(temp_celsius, weather, today, time, temp_sens, humidity, visibility) VALUES (?, ?, ?, ?, ?, ?, ?)", (temp_celsius, weather, today, time, temp_sens, humidity, visibility)) #inserting the variables into the table.
except sqlite3.IntegrityError:
    print('A record with this primary key already exists.') #if the values in the SQL command and the columns are not compatible, this error message is displayed.
else:
    conn.commit() #saving all changes made to the database.
conn.close() #closing the connection.
    
print("")
print("DATA INSERTED SUCCESSFULLY!")
print("----------------------------------")
print("")
print("SENDING TWEET...")

message = "El clima en #Reynosa #reynosafollow es "+weather+" con una temperatura de: "+temp_celsius+" °C ("+str(today)+" "+str(time)+")."
response = twitter.create_tweet(text=message)
print("Se tuiteo: %s" % message)
print(f"https://twitter.com/user/status/{response.data['id']}")

print("TWEET SENT!")

