import os
from random import randrange
from time import sleep

class BlackJack:
    game_deck = []
    dealer_hand = []
    player_hand = []

    def __init__(self):
        self.player_total_points = 0
        self.dealer_total_points = 0
        self.wallet = 100
        self.bet = 0
        

    def hole_in_one(self, turn):
        if turn == 1:
            if self.player_total_points == 21:
                self.wallet += self.bet
                print("BlackJack! Your the luckiest person ever!")
                print(f"You won ${self.bet}!", end=' ')
                print(f"You now have ${self.wallet} in your wallet.")
            else:
                return

    def player_busted(self):
        if self.player_total_points > 21:
            print()
            self.wallet -= self.bet
            print(f"You went bust! Thank you for your ${self.bet} contribution to the game.")
            print(f"You now have ${self.wallet} in your wallet.")
            return True
        else:
            return False
    
    def dealer_busted(self):
        if self.dealer_total_points > 21:
            self.wallet += self.bet
            print(f"The Dealer went bust! You won ${self.bet}!", end=' ')
            print(f"You now have ${self.wallet} in your wallet.")
            return True
        else:
            return False

    def player_point_total(self, p_hand):
        total = 0
        for card in p_hand:
            total += card.points
        self.player_total_points = total
        print(f"Points: {self.player_total_points}")
    
    def dealer_point_total(self):
        total = 0
        for card in BlackJack.dealer_hand:
            total += card.points
        self.dealer_total_points = total
        

    def dealer_cards(self, d_hand, p_hand):
        counter = 1
        while counter <= 2:
            while True:
                i = randrange(52)
                card = BlackJack.game_deck[i]
                if card in d_hand or card in p_hand:
                    continue
                else: 
                    d_hand.append(card)
                    break
            counter += 1

    def show_dealer_cards(self, d_hand):
        print("\t\tDealer Hand: ", end=" ")
        print("\t", end=" ")
        for card in d_hand:
            if card == d_hand[1]:
                print('Hidden   ')
            else:
                print(f"{card}   ", end=" ")

    def Hit(self, p_hand, d_hand):
        while True:
                i = randrange(52)
                card = BlackJack.game_deck[i]
                if card in p_hand or card in d_hand:
                    continue
                else: 
                    p_hand.append(card)
                    break

    def dealer_over(self):
        if self.dealer_total_points >= 17:
                return True

    def Stand(self, d_hand, p_hand):
        while True:
            print()
            # draw = input("Ready? Y/N: ").lower()
            # if draw == 'y':
            while True:
                i = randrange(52)
                card = BlackJack.game_deck[i]
                if card in d_hand or card in p_hand:
                    continue
                else: 
                    d_hand.append(card)
                    break
            print("\t\tDealer Hand: ", end=" ")
            print("\t", end=" ")
            for card in d_hand:
                print(f"{card}   ", end=" ")
            total = 0
            for card in d_hand:
                total += card.points
            self.dealer_total_points = total
            print(f"Points: {self.dealer_total_points}\n")
            if self.dealer_total_points >= 17:
                break
            

    def initial_bet(self):
        print(f"You have ${self.wallet} in your wallet.\n")
        risk = int(input('How much would you like to bet?: '))
        self.bet = risk
        
    
    def settlement(self):
        if self.player_total_points > self.dealer_total_points:
            self.wallet += self.bet
            print(f"Congrats Player! You won ${self.bet}\n")
            print(f"You now have ${self.wallet} in your wallet.")
        elif self.player_total_points < self.dealer_total_points:
            self.wallet -= self.bet
            print(f"So sorry, you lose. Thank you for your ${self.bet} contribution to the game.\n")
            print(f"You now have ${self.wallet} in your wallet.")
        elif self.player_total_points == self.dealer_total_points:
            self.wallet -= self.bet
            print(f"So sorry, you lose. Thank you for your ${self.bet} contribution to the game.\n")
            print(f"You now have ${self.wallet} in your wallet.")

    def double_down(self, p_hand, d_hand):
        self.bet = self.bet * 2
        while True:
                i = randrange(52)
                card = BlackJack.game_deck[i]
                if card in p_hand or card in d_hand:
                    continue
                else: 
                    p_hand.append(card)
                    break
        


    
        
class Player:
    def __init__(self):
        pass
        
    def player_cards(self, p_hand):
        counter = 1
        while counter <= 2:
            i = randrange(52)
            p_hand.append(BlackJack.game_deck[i])
            counter += 1
    
    def show_player_cards(self, p_hand):
        print("\t\tPlayer Hand: ", end=" ")
        print("\t", end=" ")
        for card in p_hand:
            print(f"{card}   ", end=" ")

class Card:
    def __init__(self, number, suit, points):
        self.number = number
        self.suit = suit
        self.points = points
        

    
    def __str__(self):
        return f"{self.number} of {self.suit}"
    

    def deck():
        ace_spade = Card('Ace', 'Spades \u2660', 11)
        two_spade = Card('2', 'Spades \u2660', 2)
        three_spade = Card('3', 'Spades \u2660', 3)
        four_spade = Card('4', 'Spades \u2660', 4)
        five_spade = Card('5', 'Spades \u2660', 5)
        six_spade = Card('6', 'Spades \u2660', 6)
        seven_spade = Card('7', 'Spades \u2660', 7)
        eight_spade = Card('8', 'Spades \u2660', 8)
        nine_spade = Card('9', 'Spades \u2660', 9)
        ten_spade = Card('10', 'Spades \u2660', 10)
        jack_spade = Card('Jack', 'Spades \u2660', 10)
        queen_spade = Card('Queen', 'Spades \u2660', 10)
        king_spade = Card('King', 'Spades \u2660', 10)
        ace_heart = Card('Ace', 'Hearts \u2665', 11)
        two_heart = Card('2', 'Hearts \u2665', 2)
        three_heart = Card('3', 'Hearts \u2665', 3)
        four_heart = Card('4', 'Hearts \u2665', 4)
        five_heart = Card('5', 'Hearts \u2665', 5)
        six_heart = Card('6', 'Hearts \u2665', 6)
        seven_heart = Card('7', 'Hearts \u2665', 7)
        eight_heart = Card('8', 'Hearts \u2665', 8)
        nine_heart = Card('9', 'Hearts \u2665', 9)
        ten_heart = Card('10', 'Hearts \u2665', 10)
        jack_heart = Card('Jack', 'Hearts \u2665', 10)
        queen_heart = Card('Queen', 'Hearts \u2665', 10)
        king_heart = Card('King', 'Hearts \u2665', 10)
        ace_diamond = Card('Ace', 'Diamonds \u2666', 11)
        two_diamond = Card('2', 'Diamonds \u2666', 2)
        three_diamond = Card('3', 'Diamonds \u2666', 3)
        four_diamond = Card('4', 'Diamonds \u2666', 4)
        five_diamond = Card('5', 'Diamonds \u2666', 5)
        six_diamond = Card('6', 'Diamonds \u2666', 6)
        seven_diamond = Card('7', 'Diamonds \u2666', 7)
        eight_diamond = Card('8', 'Diamonds \u2666', 8)
        nine_diamond = Card('9', 'Diamonds \u2666', 9)
        ten_diamond = Card('10', 'Diamonds \u2666', 10)
        jack_diamond = Card('Jack', 'Diamonds \u2666', 10)
        queen_diamond = Card('Queen', 'Diamonds \u2666', 10)
        king_diamond = Card('King', 'Diamonds \u2666', 10)
        ace_club = Card('Ace', 'Clubs \u2663', 11)
        two_club = Card('2', 'Clubs \u2663', 2)
        three_club = Card('3', 'Clubs \u2663', 3)
        four_club = Card('4', 'Clubs \u2663', 4)
        five_club = Card('5', 'Clubs \u2663', 5)
        six_club = Card('6', 'Clubs \u2663', 6)
        seven_club = Card('7', 'Clubs \u2663', 7)
        eight_club = Card('8', 'Clubs \u2663', 8)
        nine_club = Card('9', 'Clubs \u2663', 9)
        ten_club = Card('10', 'Clubs \u2663', 10)
        jack_club = Card('Jack', 'Clubs \u2663', 10)
        queen_club = Card('Queen', 'Clubs \u2663', 10)
        king_club = Card('King', 'Clubs \u2663', 10)

        BlackJack.game_deck = [ace_spade, two_spade, three_spade, four_spade, five_spade, six_spade, seven_spade, eight_spade, nine_spade, ten_spade, jack_spade, queen_spade, king_spade, ace_heart, two_heart, three_heart, four_heart, five_heart, six_heart, seven_heart, eight_heart, nine_heart, ten_heart, jack_heart, queen_heart, king_heart, ace_diamond, two_diamond, three_diamond, four_diamond, five_diamond, six_diamond, seven_diamond, eight_diamond, nine_diamond, ten_diamond, jack_diamond, queen_diamond, king_diamond, ace_club, two_club, three_club, four_club, five_club, six_club, seven_club, eight_club, nine_club, ten_club, jack_club, queen_club, king_club]

def main():
    turns = 1
    blackjack = BlackJack()
    player = Player()
    end_game = False
    while end_game == False:
        dealer_hand = []
        player_hand = []
        # Ask the player what they would like to bet.
        # Welcome screen
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\tWelcome to the BlackJack table!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        sleep(2)
        blackjack.initial_bet()
        print()
        sleep(2)
        print("May luck be ever in your favor. >:D\n")
        sleep(2)
        print("Lets begin!\n")
        sleep(2)
        # The Dealer will shuffle the deck to randomize the deck
        print("Shuffling...\n")
        sleep(2)
        # Deal the player 2 cards and the dealer 2 cards while one is hidden (Player should be able to see both of their cards but only one of the dealers cards)
        print("Dealing cards...\n")
        Card.deck()
        player.player_cards(player_hand)
        player.show_player_cards(player_hand)
        blackjack.player_point_total(player_hand)
        print()
        blackjack.dealer_cards(dealer_hand, player_hand)
        blackjack.show_dealer_cards(dealer_hand)
        print()
        # Check if the player got Blackjack or If the player Bust
        if blackjack.hole_in_one(turns):
            break
        blackjack.player_busted()
        # Ask the player if they would like to double down
        # Ask the player would they like to "hit" or "stand"
        to_do = input("What would you like to do? 'Hit', 'Stand', 'Double' down, or 'Quit': ").lower()
        print()
        # If "hit"
        if to_do == 'hit':
            # Update player turn count
            turns += 1
            while True:
                # Player recieves new card
                blackjack.Hit(player_hand, dealer_hand)
                # Show player hand
                player.show_player_cards(player_hand)
                # Display player points
                blackjack.player_point_total(player_hand)
                print()
                blackjack.show_dealer_cards(dealer_hand)
                # Check if player busted
                if blackjack.player_busted():
                    break
                print()
                to_do = input("What would you like to do? 'Hit', or 'Stand': ").lower()
                print()
                if to_do == 'hit':
                    # Update player turn count
                    turns += 1
                    continue
                elif to_do == 'stand':
                    player.show_player_cards(player_hand)
                    blackjack.player_point_total(player_hand)
                    # Count up Dealer points
                    blackjack.dealer_point_total()
                    # Check if dealer points over 17 already
                    if blackjack.dealer_over():
                        blackjack.settlement()
                        break
                    # Dealer "Hits" until his card total is >= 17
                    # Reveal dealers card
                    blackjack.Stand(dealer_hand, player_hand)
                    # Check if Dealer Busted
                    print()
                    if blackjack.dealer_busted():
                        break
                    # Determine who wins
                    blackjack.settlement()
                    break
        elif to_do == 'double':
            # Increase bet 2x and draw one card
            blackjack.double_down(player_hand, dealer_hand)
            # Show player cards
            player.show_player_cards(player_hand)
            # Count and print player total points
            blackjack.player_point_total(player_hand)
            # Check if player busted
            if blackjack.player_busted():
                play_again = input("Would you like to play again? Y/N: ").lower()
                if play_again == 'y':
                    continue
                elif play_again == 'n':
                    break
            # Count up Dealer points
            blackjack.dealer_point_total()
            # Check if dealer points over 17 already
            if blackjack.dealer_over():
                blackjack.settlement()
                print()
                play_again = input("Would you like to play again? Y/N: ").lower()
                if play_again == 'y':
                    continue
                elif play_again == 'n':
                    break
            # Start Stand Phase
            blackjack.Stand(dealer_hand, player_hand)
            # Check if Dealer Busted
            if blackjack.dealer_busted():
                print()
                play_again = input("Would you like to play again? Y/N: ").lower()
                if play_again == 'y':
                    continue
                elif play_again == 'n':
                    break
            # Determine who wins if dealer didnt bust
            blackjack.settlement()
            print()
            play_again = input("Would you like to play again? Y/N: ").lower()
            if play_again == 'y':
                continue
            elif play_again == 'n':
                break
        elif to_do == 'stand':
            player.show_player_cards(player_hand)
            blackjack.player_point_total(player_hand)
            # Count up Dealer points
            blackjack.dealer_point_total()
            # Dealer "Hits" until his card total is >= 17
            # Reveal dealers card
            blackjack.Stand(dealer_hand, player_hand)
            # Check if Dealer Busted
            print()
            if blackjack.dealer_busted():
                print()
                play_again = input("Would you like to play again? Y/N: ").lower()
                if play_again == 'y':
                    continue
                elif play_again == 'n':
                    break
            else:
                # Determine who wins
                blackjack.settlement()
                play_again = input("Would you like to play again? Y/N: ").lower()
                if play_again == 'y':
                    continue
                elif play_again == 'n':
                    break
            
        elif to_do == 'quit':
            end_game == True
        
        play_again = input("Would you like to play again? Y/N: ").lower()
        if play_again == 'y':
            continue
        elif play_again == 'n':
            break
        

        # blackjack.Stand()
        # blackjack.who_won()
main()