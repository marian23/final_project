import random
import  itertools
from flask import Flask, session, request, render_template
import json
import pprint

from collections import defaultdict
import database as db
app = Flask(__name__, static_folder='static', static_url_path='/static')
#Flask.secret_key = '12345OKJJDAHHD'
#deal all the cards in deck two player
# play card same time and don't chose the card they play
#game checks higher card and cards on the field go to player who play higher card
#if the cards match then war happpens
#the war is two card are in field each player play three card face down
#after they play three card face down then they play one card face up and who play higher card wins takes cards
#add flipper to flip the cards
# if it again match  continues to war
#make sure the win pile card to shuffle
#if you run out cards you can play the cards you win
#if someone give up or surrenders then lost game


@app.route('/game', methods=['GET', 'POST'])
def game():

    # print(sessions)
    #session['player'] = card
    error = []
    r=''

    if request.method== "POST":
        try:
            r = request.form.get('name')
            print(r)
        except:
            error.append("unable to get url")
    # Make the players
    compPlayer=player('Computer')
    humanPlayer=player(r)
    players=[compPlayer,humanPlayer]

    # make the deck
    deck_of_cards=deck()
    gm = game_methods(deck_of_cards)

    # while there are cards in the deck deal to players
    while len(deck_of_cards.card_deck)!=0:
        for p in players:
            p.hand.append(deck_of_cards.card_deck.pop())

    serialized_players=[]
    p_count = 0
    for aplayer in players:
        p_count+=1
        ser_player=aplayer.serialize()
        print(ser_player)
        serialized_players.append({'p'+str(p_count):ser_player})
    #session['players']=players

    json_players={'players':serialized_players}
    print(str(json_players))

    # pp = pprint.PrettyPrinter(indent=4)
    # print(json_players)
    return render_template('game_board.html', error=error,name=r, players=json_players)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play_card')
def play_card():
    print('placeholder for play_card method')
    # card_data = json.dumps(player.hand.pop())
    # render_template('game_board', card_data)





class war_card_game:


    def main(self):
        print("welcome to war game and have a fun while playing")
    # def shuffle(self):
    #     random.shuffle()
    # def deal_cards(self):
    #     self.deck.shuffle()
    #     self.deck.set


class deck:
    def __init__(self):
        self.card_deck = []
        self.suites = {'Spades', 'Hearts', 'Diamonds', 'Clubs'}

        self.ranges = range(1, 14)
        for suite in self.suites:
            for number in self.ranges:
                new_card = card(suite,number)
                # db.insert_card(new_card)
                self.card_deck.append(new_card.serialize())
                print(self.card_deck)
        random.shuffle(self.card_deck)
    #store deck in the datatbase

class card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.card_owner = ''
        self.img_src = 'image/'+(str(value) + suite + ".png")

    def __repr__(self):
        card_suite = str(self.value) + self.suite
        return card_suite

    def serialize(self):
        return {
            'suite': self.suite,
            'value': self.value,
            'card_owner':self.card_owner,
            'img_src': self.img_src
        }



class player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.win_pile =[]
    def play_card(self):
        card = self.hand.pop()

        return card
    def get_win_pile(self):
        random.shuffle(self.win_pile)
        for num in self.win_pile:
            card = self.win_pile.pop()
            card.card_owner = self.name
            self.hand.append(card)

    def own_cards(self):
        for card in self.hand:
            if card['card_owner']!=self.name:
                card['card_owner']=self.name

    def serialize(self):
        self.own_cards()
        return {
            'name':self.name,
            'hand': self.hand
        }

class game_methods:
    def __init__(self,deck):
        self.players = []
        self.deck = deck

    def check_card(self, card1, card2):

        if card1.value > card2.value:
            play_name = card1.card_owner
            for p in self.players:
                if p.name == play_name:
                    p.win_pile.append(card1)
                    p.win_pile.append(card2)

        if card2.value > card1.value:
            play_name = card2.card_owner
            for c in self.players:
                if c.name == play_name:
                    c.win_pile.append(card2)
                    c.win_pile.append(card1)






if __name__=='__main__':
    app.secret_key = '12345OKJJDAHHD@#'
    app.run(debug=True)