from .models import *
from django.test import TestCase
from django.contrib.auth.models import User


class GamesTest(TestCase):
    print("The available Game posts are")
    game = Games.objects.all()
    for i in game:
        print(i.name, " ", i.date_updated, )
        print("By ", i.creator)
        print("----------------------------------------------------------------")

    def test_show(self):

        print("------------------------------------------")
        gname = input("Enter the name of the game you want \t")
        games_a = Games(name=gname, creator=User.objects.all().first())
        print("Games data test is working")

