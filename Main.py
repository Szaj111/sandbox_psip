#print (f'Twoj znajomy facebook {zmienna_na_dane[0]["nick"]} opublikowal  {zmienna_na_dane[0]["posts"]}')

from dane import users_list

def add_user_to(users_list:list) ->None:
    """
    This is object to list
    :param users_list: list - user
    :return: None
    """
    name = input ("podaj imie ?")
    posts = input (" Podaj liczbe postow")
    users_list.append({'name':name, "posts": posts })

add_user_to(users_list)
add_user_to(users_list)
add_user_to(users_list)

for user in users_list:
    print(f'Twoj znajomy {user["name"]} dodal nastepujaca liczbe postow -  {user["posts"]}')




