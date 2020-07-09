#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:


from random import choice

#We first create a function that returns the amount of money that the player wants to bet:
def initial_bet():
    n = 1
    while n > 0:
        bet_string = input("Please enter the amount of money with which you want to play: ")
        if bet_string.isdigit():
            bet = float(bet_string)
            if bet > 0:
                return bet
#We build a function that returns the player's decision
def decision():
    n = 1
    while n > 0:
        x = input("Hit or Stand?")
        if x == "Hit" or x == "Stand":
            return x
#We create a function that returns the player's decision to double its bet:
def doubling_decision():
    x = input("Would you like to double your amount? [y/n]")
    while x != "y" and x != "n":
        x = input("Would you like to double your amount? [y/n]")
    return x
            
        
#And we start playing:
def play_blackjack():
    #We then create a function that returns the player's bet in a specific round:
    def round_bet():
        n = 1
        while n > 0:
            try:
                x = float(input"You have " + str(money_count) + " euros left. Please enter your bet for this round: ")
                if x >= 0 and x <= money_count:
                    return x
            except:
                print("Please enter a number")
    #We now create a dictionary with each card's value
    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card_values = dict(zip(cards,values))
    #We crate a list with the doubling bet card possibilities
    doubling_values = [9,10,11]
    #We then create a counter with the player's total money and start the game, which will end if this counter ends in 0
    #the player bets 0 in a certain round
    money_count = initial_bet()
    while money_count > 0:
        bet = round_bet()
        if bet > 0:
            #We create a list of the remaining cards in the deck (i.e. those that have not been given to the dealr or player)
            remain_cards = []
            for e in cards:
                remain_cards += 4*[e]
            #We then create two lists with the dealer's and player's cards and two variables with their respective scores
            player_cards = []
            dealer_cards = []
            player_score = 0
            dealer_score = 0
            #We handle the first 4 cards and update the player's and dealer's scores, their cards and the remaining cards in the deck:
            for i in range(2):
                card_for_player = choice(remain_cards)
                player_cards.append(card_for_player)
                remain_cards.remove(card_for_player)
                player_score += card_values[card_for_player]
                card_for_dealer = choice(remain_cards)
                dealer_cards.append(card_for_dealer)
                remain_cards.remove(card_for_dealer)
                dealer_score += card_values[card_for_dealer]
            player_string = "Your cards: " + player_cards[0] + " " + player_cards[1]
            dealer_string = "Dealers' cards: " + dealer_cards[0]
            #We check if the player has a blackjack:
            if player_score == 21:
                print(player_string)
                print(dealer_string + " " + dealer_cards[1])
                if dealer_score < 21:
                    print("Blackjack!! You win!")
                    money_count += bet
                else:
                    print("Dealer and player have a blackjack. It is a tie")
            #We then check if the player has the right to double its bet and offer him/her the possibility to do so:
            elif player_score in doubling_values and money_count >= 2*bet:
                print(player_string)
                print(dealer_string)
                d = doubling_decision()
                if d == "y":
                    bet = 2*bet
                    print("Your current bet is of " + str(bet) + " euros.")
            #We then continue with the game if the player does not have a blackjack:
            if player_score < 21:
                print(player_string)
                print(dealer_string)
                #We continue handling cards to the player, creating two variables: one with the number of handled cards
                ##and the other one with the number of ases that the player has counted as 1 (they can count 1 or 11)
                n = 2
                ases_used_player = 0
                #If the player has two A, he/she will count one of them as 1:
                if player_score == 22:
                    player_score -= 10
                    ases_used_player += 1
                player_decision = decision()
                #If the player's score is under 21, he/she has the chance to ask for another card or to stand:
                while player_score < 21 and player_decision == "Hit":
                    card_for_player = choice(remain_cards)
                    player_cards.append(card_for_player)
                    remain_cards.remove(card_for_player)
                    player_score += card_values[card_for_player]
                    player_string += " " + player_cards[n]
                    ases_player = player_cards.count("A")
                    print(player_string)
                    #If the player has gone over 21 and has an A counting as 11, he/she will count it as 1:
                    if player_score > 21:
                        if ases_used_player < ases_player:
                            player_score -= 10
                            ases_used_player += 1
                            player_decision = decision()
                        else:
                            print("Over 21! You lose.")
                            money_count -= bet
                            player_decision = "Stand"
                    elif player_score == 21:
                        player_decision = "Stand"
                    else:
                        player_decision = decision()
                    n += 1  
                if player_score <= 21:
                    print("Your score is " + str(player_score) + ". Dealers' turn")
                    #We now handle the rest of the cards to the dealer, who plays automatically:
                    dealer_string += " " + dealer_cards[1]
                    if dealer_score == 21:
                        print(dealer_string)
                        print("The dealer has a blackjack! You lose.")
                        money_count -= bet
                    else:
                        n = 2
                        ases_used_dealer = 0
                        if dealer_score == 22:
                            dealer_score -= 10
                            ases_used_dealer += 1
                        while dealer_score < 17:
                            card_for_dealer = choice(remain_cards)
                            dealer_cards.append(card_for_dealer)
                            remain_cards.remove(card_for_dealer)
                            dealer_score += card_values[card_for_dealer]
                            dealer_string += " " + dealer_cards[n]
                            ases_dealer = dealer_cards.count("A")
                            if dealer_score > 21 and ases_used_dealer < ases_dealer:
                                dealer_score -= 10
                                ases_used_dealer += 1
                            n += 1
                        print(dealer_string)
                        #We finally check the result:
                        if dealer_score > 21 or dealer_score < player_score:
                            print("You win!")
                            money_count += bet
                        elif dealer_score == player_score:
                            print("It is a tie!")
                        else:
                            print("You lose.")
                            money_count -= bet
        else:
            return "Game ended. You end up with " + str(money_count) + " euros."
    return "Game ended. You end up with " + str(money_count) + " euros."

