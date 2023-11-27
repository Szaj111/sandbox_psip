from bs4 import BeautifulSoup
import requests
import  re
import folium

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

#print(get_coordinates_of_(nazwa_miejscowosci))
# zrwoc mape z pinezka odnoszacego sie do uzytkownika podanego z klawiaturtny
# zwroc mape z wszystkimi uzytkownikami z danej listy (znajomymi)

city = location=get_coordinates_of_(city='Zamość')
map = folium.Map(city, tiles="OpenStreetMap", zoom_start=12)

folium.Marker(
    location=city,
    popup= 'Geoinforamtyka').add_to(map)
map.save('mapka.html')
print(map)
# Rysowanie mapy