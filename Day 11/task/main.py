import random

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card

def calculate_score(userList, computerList):
    user_score = sum(userList)
    computer_score = sum(computerList)

    return user_score, computer_score


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


print(user_cards, computer_cards, sep=' and ')
print(calculate_score(user_cards, computer_cards))