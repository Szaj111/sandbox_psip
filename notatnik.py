from bs4 import BeautifulSoup
import requests
import  re

nazwa_miejscowosci = 'Warszawa'
#pobranie strony
def get_coordinates_of_(city:str)->list[float, float]:
    # pobranie współ str

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text,'html.parser')


    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_latitude = float(response_html_latitude.replace(',','.'))

    response_html_longitude = response_html.select('.longitude')[1].text
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]

print(get_coordinates_of_(nazwa_miejscowosci))