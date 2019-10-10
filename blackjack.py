import random

suits = ('Herts','Diamonds','Spades','Clubs')
runks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Qeen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Qeen':10,'King':10,'Ace':11}

playing = True

class Card():
    def __init__(self,suit,runk):
        self.suit = suit
        self.runk = runk

    def __str__(self):
        return self.runk + ' of ' + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for runk in runks:
                self.deck.append(Card(suit, runk))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.value = 0
        self.cards = []
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value +=values[card.runk]

        if card.runk == 'Ace':
            self.aces +=1

    def adjust_for_aces(self):
        while self.value>21 and self.aces:
            self.value -=10
            self.aces -=1

class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total +=self.bet
    def losse_bet(self):
        self.total -=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Какую ставку хочешь сделать? '))
        except:
            print('Кажеться ты ввёл не целое число, попробуй ещё раз.')
        else:
            if chips.bet > chips.total:
                print('Ты не можешь сделать такую ставку, у тебя на счету {} фишек'.format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Введите h чтобы сдать карту, или s - чтобы закончить игру.')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif  x[0].lower()=='s':
            print('Игрок остановил игру, вскрываемся ')
            playing = False
        else:
            print('Я не знаю такой команды')
            continue
        break

def player_busts(player, dealer, chips):
    print('Игрок перебрал!')
    chips.losse_bet()
def player_wins(player, dealer, chips):
    print('Игрок выиграл!')
    cheps.win_bet()
def dealer_busts(player, dealer, chips):
    print('Игрок выиграл!')
    cheps.win_bet()
def dealer_wins(player, dealer, chips):
    print('Игрок проиграл!')
    chips.losse_bet()
def push(player, dealer):
    print('Ничья!!!')


def show_some(player, dealer):
    print('На руках у диллера:')
    print('Одна карта скрыта')
    print(dealer.cards[1])
    print('/n')
    print('На руках у игрока:')
    for card in player.cards:
        print(card)
def show_all(player, dealer):
    print('На руках у диллера:')
    for card in dealer.cards:
        print(card)
    print('/n')
    print('На руках у игрока:')
    for card in player.cards:
        print(card)

while True:
    print('Welcom to Black Jack')
    deck=Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_chips)

        if player_hand.value <=21:
            while dealer_hand.value < player_hand.value:
                hit(deck,dealer_hand)
            show_all(player_hand, dealer_hand)

            if dealer_hand.value >21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        print('Player total chips are: {} '.format(player_chips.total))

    new_game = input('Would you like to play again? Enter Y or N')
    if new_game[0].lower() =='y':
        playing = True
        continue
    else:
        print('Thank you for game! ')
        break
