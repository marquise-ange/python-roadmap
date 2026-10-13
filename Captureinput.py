#input helps the user to type the information needed (to get the data we don't have)
#name=input("what is your name? ")
#print(f"nice to meet you, {name}")
# Challenge: Update the Excuse Generator to accept user input.

# Right now all the variables are hardcoded. Let's fix that.
# 1. Replace each variable's value with an input() prompt.
# 2. Print and test — make sure your output still looks like this:
#    "Sorry [Ted], I can't go to [the movies] — I have [345] [bees] to [crochet]
#     and honestly it's taking longer than expected."

name = input("what is your name? ")
event = input("which concert is this? ")
number =input("I am with? ")
noun = input("where? ")
verb = input("placing? ")

excuse = f"Sorry {name}, I can't go to {event} — I have {number} {noun} to {verb} and honestly it's taking longer than expected."

print(excuse)