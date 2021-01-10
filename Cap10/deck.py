import random
from card import Card


class DeckOfCards:
    NUMERO_CARTAS=52

    def __init__(self):
        self._current_card=0
        self._deck=[]

        for i in range(DeckOfCards.NUMERO_CARTAS):
            self._deck.append(Card(Card.FACES[i%13],Card.SUITS[i//13]))

    def shuffle(self):
        """Varaja las cartas e inicializa el indice de la baraja a cero"""
        self._current_card=0
        random.shuffle(self._deck)


    def deal(self):
        """Retorna una carta"""
        try:
            card=self._deck[self._current_card]
            self._current_card+=1
            return card
        except:
            return None

    def __str__(self):

        s=''

        for i in range(len(self._deck)):

            s+=f'{self._deck[i]:<19}'
            if(i+1)%4==0:
                s+='\n'
        return s



