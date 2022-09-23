from classes import *

def help():
    print("""Possible input choices:
    'Name of player' 'claim'
     Delete
     Claims
     Score
    'Winners' 'Names of players'""")
    pass


def get_player(player_name, list_players):
    player = list(filter(lambda x: x.name == player_name, list_players))[0]
    return player
