#!/usr/bin/env python

from modules import display_random
import random

class Jokes:
    def __init__(self, lst, index):
        self.lst=lst
        self.index=index

jokes=[
        "Don't do drugs; it's foo expensive",
        "'Interviewer: You said you're you good with Python!', 'Me: Yeah, we have lots of them in Australia'",
        "Pythons scare me. I would rather go and see Pandas instead.",
        "Jokes on you, I'm out of them. Till we meet again!"
]

display_random(jokes)
