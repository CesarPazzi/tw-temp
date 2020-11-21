# importamos Beautiful Soup, urllib y Twython
import bs4 as bs
import urllib.request
from twython import Twython
import datetime
import os

######### GLOBALES ######### 

yahoo_url = os.environ['YAHOO_URL']

# definimos la URL que queremos Scrapear con la variable 'url'
url = urllib.request.urlopen(yahoo_url).read()

# Se crea un objeto global con la URL y el tipo de Parser, en este caso es html y por eso usamos el parser llamado 'html5lib'
pagina = bs.BeautifulSoup(url, "html5lib")

# Creamos una variable para almacenar la hora actual
hora = datetime.datetime.now()
hora_local = int(hora.hour)-6


######### FUNCIONES ######### 

# Creamos una funcion para obtener la temperatura en Celsius llamada GetTemp
def GetTempC():
    # Se usa el metodo 'find' para buscar la etiqueta <span> con el atributo 'data-reactid' con valor '37'
    a = pagina.find("span", {"data-reactid": "37"}).get_text()

    # Se declara la variable c para que se almacene la conversion de Fahrenheit a Celsius
    c = (int(a)-32)*5/9

    # Lo que se regresa es el redondeo del numero flotante c. 'round()' es para redondear y 'float(c)' es para hacer flotante a 'c'
    return(round(float(c)))


# Creamos una funcion para obtener el texto referente al clima (mayormente nublado, despejado, lluvioso, etc.)
def GetClima():
    # Se usa el metodo 'find' para buscar la etiqueta <span> con el atributo 'data-reactid' con valor '26'
    a = pagina.find("span", {"data-reactid": "26"}).get_text()

    # Se regresa el texto encontrado con el metodo 'find'
    return(str(a))


######### TWYTHON CONFIG ######### 

# Github Secrets
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']


# Se crea un objeto Twython
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


######### MAIN ######### 

if __name__ == "__main__":

    #Se define 'temp' como la variable que tendra el dato de la temperatura
    temp = GetTempC()
    clima = GetClima()

    # Cambiar 'message' para adaptarlo a tu situacion
    message = "El clima en #Reynosa #reynosafollow es '"+str(clima)+"' con una temperatura de: '"+str(temp)+"°C' ("+str(hora_local)+":"+str(hora.minute)+"hrs.)"

    # Se manda el tuit con la informacion
    twitter.update_status(status=message)

    # Y se imprime en pantalla
    print("Se tuiteo: %s" % message)

    pass







