import random

#1. Display random items in a list
def display_random(lst):
    for x in lst:
        index=int(random.randint(0, len(lst)))
    print(lst[index])
