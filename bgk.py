import random


def get_choices():
    player1 = input("enter what you use :")
    object = ["batu", "gunting", "kertas"]
    player2 = random.choice(object)
    pemenang = {"player1" : player1, "player2" : player2}
    return (pemenang)

choices = get_choices()
print(choices)

def check_winner(player1, player2):
    print(f"kamu pilih : {player1}, player 2 milih : {player2}")
    if player1 == player2 :
        return "seri bro"
    elif player1 == "batu" :
        if player2 == "gunting" :
            return "batu lawan gunting, ya menang lah"
        else :
            return "batu dipeluk kertas, kalah bro"
    elif player1 == "kertas":
        if player2 == "batu":
            return "kertas meluk batu, ya menang lah"
        else:
            return " kertsd digunting gunting , kalah bro"
    elif player1 == "gunting":
        if player2 == "kertas":
            return "gunting motong kertas, ya menang lah"
        else:
            return " gunting digeprek batu, kalah bro"
choices = get_choices()
pemenang =check_winner(choices["player1"] , choices ["player2"])
print(pemenang)