import random

"""can use "from" if you want only one funtion insted of whole module.
for example: from random import choice
this right here imports only choice funtion"""
# pick random from list
coin = random.choice(["heads", "tails"])
print(coin)

# pick random int
number = random.randint(1, 100)
print(number)

# shuffle the given list in random order
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
