### Capstone project: Blackjack game ###
# My version that does not work
# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player_score = 0
# computer_score = 0

# def randomCard(user_cards):
#     user_cards.append(random.choice(cards))

# def blackjack_logic(player, computer):
#     if computer > player and computer < 22:
#         return 'computer'
#     elif computer > player and computer > 21:
#         return 'player'
#     elif player > computer and player < 22:
#         return 'player'
#     elif player > computer and player > 21:
#         return 'computer'

# def score_print(p_cards, c_cards, p_score):
#     print(f"   Your cards: {p_cards}, current score: {p_score}")
#     print(f"   Computer's first card: {c_cards[0]}")


# def final_score_print(cards,score):
#     print(f"   Your final hand: {cards}, final score: {score}")

# def winner_declare(p_score,c_score,p_cards,c_cards):
#     winner = blackjack_logic(p_score, c_cards)
#     final_score_print(p_cards, p_score)
#     final_score_print(c_cards, c_score)
#     if winner == 'computer' and p_score > 21:
#         print("You went over. You lose 😤")
#     elif winner == 'computer':
#         print("You lose 😤")
#     elif winner == 'player' and c_score > 21:
#         print("Computer went over. You win 😁")
#     elif winner == 'player':
#         print("You win 😁")

# def calculate_score(p_cards,c_cards):
#     player_score = sum(p_cards)
#     computer_score = sum(c_cards)
#     return [player_score, computer_score]

# def blackjack():
#     player_cards = []
#     computer_cards = []
#     randomCard(player_cards)
#     randomCard(player_cards)
#     while sum(computer_cards) < 21:
#         randomCard(computer_cards)
#     player_score = calculate_score(p_cards=player_cards,c_cards=computer_cards)[0]
#     computer_score = calculate_score(p_cards=player_cards,c_cards=computer_cards)[1]
    
#     while player_score < 22:
#         score_print(p_cards=player_cards, c_cards=computer_cards,p_score=player_score)
#         choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#         if choice == 'n':
#             winner_declare(p_score=player_score, c_score=computer_score, p_cards=player_cards, c_cards=computer_cards)
#             player_score = 22
#         elif choice == 'y':
#             randomCard(player_cards)



    
# game_on = True
# while game_on:
#     start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     if start == 'y':
#         game_on = True
#         blackjack()
#     elif start == 'n':
#         game_on = False


#  AI version that works
import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(CARDS)

def calculate_score(hand):
    """Return the best score ≤ 21, converting Aces from 11 → 1 as needed."""
    score = sum(hand)
    aces = hand.count(11)
    while score > 21 and aces:
        score -= 10
        aces -= 1
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
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"   Your cards: {player_hand}, current score: {player_score}")
        print(f"   Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    # Dealer's turn (only if player didn't bust)
    while calculate_score(computer_hand) < 17 and calculate_score(player_hand) <= 21:
        computer_hand.append(deal_card())

    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    print(f"   Your final hand: {player_hand}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))

# Main loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" + "="*30)
    play_game()