
from random import random

deck = list(range(1,100))

hand = random.sample(deck,k=5)
print(hand)