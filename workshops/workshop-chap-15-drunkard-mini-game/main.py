from random import shuffle

'''                                                     Игра "Пьяница"
в этой игре колода делится между двумя игроками, тот у кого старше карта - забирает обе карты себе. Тот кто остался без карт - проигрывает
'''

class card:

    suits=['пика',
          'черва',
          'бубна',
          'трефа']

    vals=[None,
         None,
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '10',
         'валет',
         'дама',
         'король',
         'туз']

    def __init__(self,v,s):
        ''' s,v - int '''
        self.value=v
        self.suit=s

    def ___lt___(self,card2):

        if self.value < card2.value:
            return True

        elif self.value == card2.value:

            if self.suit < card2.suit:
                return True
            else:
                return False

        else:
            return False

    def __gt__(self,card2):

        if self.value > card2.value:
            return True

        elif self.value == card2.value:

            if self.suit > card2.suit:
                return True
            else:
                return False

        else:
            return False

    def __repr__(self):
        return '{}, {}'.format(self.vals[self.value],self.suits[self.suit])

class deck:

    def __init__(self):

        self.cards=[]

        for i in range(2,15):
            for j in range(4):
                self.cards.append(card(i,j))

        shuffle(self.cards)

    def rm_cards(self):

        if len(self.cards)==0:
            return None

        return self.cards.pop()

class player:

    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class game:

    def __init__(self):

        name_1=input('Введите имя первого игрока: ')
        name_2=input('Введите имя второго игрока: ')
        self.deck=deck()
        self.p1=player(name_1)
        self.p2=player(name_2)

    def wins(self,winner):

        print('{} - забирает карты'.format(winner))

    def draw(self,p1_name,p2_name,p1_card,p2_card):

        print('{} кладет {}, а {} кладет {}'.format(p1_name,p1_card,p2_name,p2_card))

    def winner(self,p1,p2):
        if self.p1.wins>self.p2.wins:
            return self.p1.name
        elif self.p1.wins<self.p2.wins:
            return self.p2.name
        return 'Ничья'

    def play_game(self):

        cards=self.deck.cards
        print('Игра началась!')
        while len(cards)>=2:
            r=input('Введите X (англ.) для выхода, для продолжения нажмите любую клавишу: ')
            if r == 'X':
                break

            p1c=self.deck.rm_cards()
            p1n=self.p1.name

            p2c=self.deck.rm_cards()
            p2n=self.p2.name

            self.draw(p1n,p2n,p1c,p2c)

            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)

        win=self.winner(self.p1,self.p2)
        if win!='Ничья':
            print('Игра окончена! Игрок с именем {} победил!'.format(win))
        else:
            print('Ничья!')

game=game()
game.play_game()
