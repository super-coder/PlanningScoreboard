from functions import *


def main():
    players_list = []
    help()
    while True:
        text = input()
        text_list = text.split()
        if len(text_list) == 0:
            continue
        player_names_list = [i.name for i in players_list]
        if any(i.isdigit() for i in text_list):
            player_name = text_list[0].capitalize()
            player_claim = int(text_list[1])

            if player_name not in player_names_list:
                player = Player(player_name)
                players_list.append(player)

            player = get_player(player_name, players_list)
            player.set_claim(player_claim)

        elif text_list[0].lower() == 'winners':
            if len(text_list) > 1:
                player_names = [i.capitalize() for i in text_list[1:]]
                if set(player_names).issubset(player_names_list):
                    for i in text_list[1:]:
                        player = get_player(i.capitalize(), players_list)
                        player.winner()
                else:
                    print('Enter valid name')
                    continue
            for i in players_list:
                i.set_claim(0)
                print(i.name, i.score)

        elif text_list[0].lower() == 'delete':
            if text_list[0].capitalize() in player_names_list:
                player = get_player(text_list[1].capitalize(), players_list)
                players_list.remove(player)

        elif text_list[0].lower() == 'score':
            for i in players_list:
                print(i.name, i.score)

        elif text_list[0].lower() == 'claims':
            for i in players_list:
                print(i.name, i.claim)

        elif text_list[0] == 'help':
            help()

        elif text.capitalize() == 'End':
            break

        else:
            print('Invalid argument')


if __name__ == '__main__':
    main()
