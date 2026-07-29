### Capstone project: Blackjack game ###

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