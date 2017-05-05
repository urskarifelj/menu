# -*- coding: utf-8 -*-
# --author-- = Urska Rifelj

menu_list = {"dish_1": 50,
             "dish_2": 10,
             "dish_3": 20,
             "dish_4": 36
             }


list_of_dishes = open("list_of_dishes.txt", "w+")

list_of_dishes.write("MENU\n")

for key, value in menu_list.iteritems():
    list_of_dishes.write('%s: %s eur\n' % (key, value))

list_of_dishes.close()

