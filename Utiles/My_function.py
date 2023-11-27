from bs4 import BeautifulSoup
import requests
import folium
def get_coordinates_of_(city:str)->list[float, float]: # nwm czy to ma byc
    # pobranie współ str

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text,'html.parser')


    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_latitude = float(response_html_latitude.replace(',','.'))

    response_html_longitude = response_html.select('.longitude')[1].text
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]
def get_map_one_user(user:str)->None:
    city =get_coordinates_of_(user["city"])
    map = folium.Map(
        location = city,
        tiles="OpenStreetMap",
        zoom_start=14
    )
    folium.Marker(
       location=city,
       popup=f"Tu rządzi_{user["name"]}"
             f"Liczba postów{user["posts"]}"
    ).add_to(map)
    map.save(f"mapka_{user["name"]}.html")
def get_map_of(users: list) ->None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetmap",
        zoom_start=7,
    )
    for user in users:
        folium.Marker(
            location=get_coordinates_of_(city=user["city"]),
            popup=f'Uzytkownik: {user["name"]}'
                f'Liczba postow {user['posts']}'
        ).add_to(map)
    map.save('mapka.html')
def add_user_to(users_list:list) ->None:
    """
    This is object to list
    :param users_list: list - user
    :return: None
    """
    name = input ("podaj imie? - ")
    posts = input (" Podaj liczbe postow")
    users_list.append({'name':name, "posts": posts })
def remove_user_from(users_list: list) -> None:
    tmp_list = []
    name = input("Podaj imie uzytkownika do usuniecia - ")
    for user in users_list:
        if user['name'] == name:
            print(f'Znaleziony uzytkownik {user}')
            tmp_list.append(user)
    print("Znaleziono nastepujaych usytkownikow: ")
    print("0 - usun wszystkich znalezionych uzytkownikow")
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek + 1}{user_to_be_removed}')
    numer = int(input(f'wybierz uzytkownika do usuniecia: '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])

def show_users_from(users_list:list) -> None:
    for user in users_list:
        print(f'Twoj znajomy {user["name"]} dodal nastepujaca liczbe postow -  {user["posts"]}')



def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('podaj nick uzytkownika do modyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono !!!')
            user['name'] = input('podaj nowe imie: ')
            user['nick'] = input('podaj nowa ksywe: ')
            user['posts'] = int(input('podaj liczbe postow: '))

def gui(users_list:list)->None:
    while True:
        print( f'Menu: \n' 
            f'0: Wyjdz \n'
            f'1: Wyświetl uztkowników \n'
            f'2: Dodaj uzytkownika \n'
            f'3: Usun uzytkownika \n'
            f'4: Modyfikuj uzytkownika \n'
            f'5: Wygeneruj mape z uzytkownikiem \n'
            f'6: Wygeneruj mape z uzytkownikami \n'
           )
        menu_option = input("Podaj funkcje do wywolania - ")
        print(f'Wybrano funkcje {menu_option}')

        match menu_option:
            case "0":
                print("Koncze prace")
                break
            case "1":
                print("Wyswietlam uzytkownika")
                show_users_from(users_list)
            case "2":
                print("Dodaje uzytkownika")
                add_user_to(users_list)
            case "3":
                print("Usuwam uzytkownika")
                remove_user_from(users_list)
            case "4":
                print("Modyfikuj uzytkownika")
                update_user(users_list)
            case '5':
                print('Rysuj mape z uzytkownikiem')
                user = input("podaj nazwe uzytkownika")
                for item in users_list:
                    if item['name'] ==user:
                        get_map_one_user(item)

            case '6':
                print("Rysuje mape z uzytkownikami")
                get_map_of(users_list)
