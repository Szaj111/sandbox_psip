#print (f'Twoj znajomy facebook {zmienna_na_dane[0]["nick"]} opublikowal  {zmienna_na_dane[0]["posts"]}')

from dane import users_list

def add_user_to(users_list:list) ->None:
    """
    This is object to list
    :param users_list: list - user
    :return: None
    """
    name = input ("podaj imie? - ")
    posts = input (" Podaj liczbe postow")
    users_list.append({'name':name, "posts": posts })

#add_user_to(users_list)
def remove_user_from(users_list:list) ->None:
    tmp_list= []
    name = input("Podaj imie uzytkownika do usuniecia - ")
    for user in users_list:
        if user ['name'] == name:
            print (f'Znaleziony uzytkownik {user}')
            tmp_list.append(user)
    print("Znaleziono nastepujaych usytkownikow: ")
    print("0 - usun wszystkich znalezionych uzytkownikow")
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+ 1}{user_to_be_removed}')
    numer = int(input(f'wybierz uzytkownika do usuniecia: '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])


remove_user_from(users_list)
for user in users_list:
    print(f'Twoj znajomy {user["name"]} dodal nastepujaca liczbe postow -  {user["posts"]}')




