import random
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

### Practice 1 ###
# def deal_card():
#     return random.choice(CARDS)

# def calculate_score(hand):
#     score = sum(hand)
#     ace = hand.count(11)

#     if score > 21 and ace:
#         score -= 10
#         ace -= 1
#     return score

# def compare(player_score, computer_score):
#     if player_score > 21:
#         return "You went over. You lose"
#     if computer_score > 21:
#         return "Opponent went over. You win"
#     if computer_score == player_score:
#         return "Draw"
#     if player_score > computer_score:
#         return "You win"
#     return "You lose"


# def play_game():
#     player_hand = [deal_card(), deal_card()]
#     computer_hand = [deal_card(), deal_card()]

#     game_over = False

#     while not game_over:

#         player_score = calculate_score(player_hand)
#         computer_score = calculate_score(computer_hand)

#         print(f"  your cards: {player_hand}, current score: {player_score}")
#         print(f"  Computer's first card: {computer_hand[0]}")

#         if player_score == 0 or computer_score == 0 or player_score > 21:
#             game_over = True
#         else:
#             choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#             if choice == 'y':
#                 player_hand.append(deal_card())
#             else:
#                 game_over = True

#     while calculate_score(computer_hand) < 17 and calculate_score(player_hand) <= 21:
#         computer_hand.append(deal_card())

#     player_score = calculate_score(player_hand)
#     computer_score = calculate_score(computer_hand)

#     print(f"  Your final hand: {player_hand}, final score: {player_score}")
#     print(f"  computer's final hand: {computer_hand}, final score: {computer_score}")
#     print(compare(player_score,computer_score))

# # Main loop
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
#     print("\n" + "=" * 50)
#     play_game()

### Practice 2 ###

def deal_card():
    return random.choice(CARDS)

def calculate_score(hand):
    score = sum(hand)
    ace = hand.count(11)

    if score > 21 and ace:
        score -= 10
        ace -= 1
    return score

def compare(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose 😤"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if player_score == computer_score:
        return "Draw 🙃"
    if player_score > computer_score:
        return "You win 😁"
    return "You lose 😤"

def play_game():
    # First round would allow both player to deal two cards
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # here needs to be a loop where player will come back if score is below 21 and player deal a hand
    game_over = False

    while not game_over:
        # Check/print the score, 
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"  Your cards: {player_cards}, current score: {player_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        # if player goes over 21 ==> game over
        if computer_score == 0 or player_score == 0 or player_score > 21:
            # Stop the while loop for another card
            game_over = True

        # if player is below 21 choice need to be given to deal another hand
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            player_cards.append(deal_card())
        # if the player don't want another hand ==> game over
        else:
            game_over =True

    # Computer will keep dealing it is under 17 and player is done but still under 21
    while calculate_score(computer_cards) < 17 and calculate_score(player_cards) <= 21:
        computer_cards.append(deal_card())

    # from here on code will only run if player is done with dealing cards

    # update final score
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    # Final score given
    print(f"  Your final hand: {player_cards}, final score: {player_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
    # final verdict
    print(compare(player_score, computer_score))



# Main loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" + "="*90)
    play_game()