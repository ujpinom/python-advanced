
class Card:
    FACES=['Ace', '2', '3', '4', '5', '6','7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS=['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self,faces,suits):
        self._faces=faces
        self._suits=suits

    @property
    def faces(self):
        return self._faces
    @property
    def suits(self):
        return self._suits

    @property
    def image_name(self):
        return str(self).replace(' ','_')+'.png'

    def __repr__(self):
        return (f'Card(faces={self._faces},suits={self._suits})')

    def __str__(self):
        return f'{self._faces} of {self._suits}'

    def __format__(self, format):
        return f'{str(self):{format}}'


