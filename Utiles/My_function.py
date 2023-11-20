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
def update_user(users_list: list[dict,dict]) -> None:
    nick_of_user = input('podaj nick uzytkownika do modyfikacji ')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono !!!')
            user['name'] = input('Podaj nowe imie:  ')
            user['nick'] = input('Podaj nowy nick:  ')
            user['posts'] = int(input('Podaj liczbe postow: '))
def show_users_from(users_list:list) -> None:
    for user in users_list:
        print(f'Twoj znajomy {user["name"]} dodal nastepujaca liczbe postow -  {user["posts"]}')

def gui(users_list:list)->None:
    while True:
        print( f'Menu: \n' 
            f'0: Wyjdz \n'
            f'1: Wyświetl uztkowników \n'
            f'2:Dodaj uzytkownika \n'
            f'3: Usun uzytkownika \n'
            f'4: Modyfikuj uzytkownika \n'
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
                print("Modyfikuje uzytkownika")
                update_user(users_list)