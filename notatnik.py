from bs4 import BeautifulSoup
import requests
import  re
import folium


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
user = {"city":"Zamość","name":"Szymon","nick":"Spec","posts":533}
def get_map_of(user:str)->None:
    map = folium.Map(
        city = get_coordinates_of_(user["city"]),
        location=city,
        tiles="OpenStreetMap",
        zoom_start=14
    )
    folium.Marker(
       location=city,
       popup=f"Tu rządzi_{user["name"]}"
             f"Liczba postów{user["posts"]}"
    ).add_to(map)
    map.save(f"mapka_{user["name"]}.html")

# zwroc mape z wszystkimi uzytkownikami z danej listy (znajomymi)

def get_map_of(users: list) ->None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStretmap",
        zoom_start=7,
    )
    for user in users:
        folium.Marker(
            location=get_coordinates_of_(city=user["city"]),
            popup=f'Uzytkownik: {user["name"]}
                f'Liczba postow {user['posts']}'
        ).add_to(map)
    map.save('mapka.html')
from dane import users_list





city = location=get_coordinates_of_(city='Zamość')
map = folium.Map(city, tiles="OpenStreetMap", zoom_start=12)

#for item in nazwa_miejscowosci:

   # folium.Marker(
  #      location=get_coordinates_of_(city)
 #       popup= 'Geoinforamtyka').add_to(map)
 #   map.save('mapka.html')
print(map)
# Rysowanie mapy