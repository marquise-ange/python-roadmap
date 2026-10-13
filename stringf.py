#f->is format (it help us to print the declared variable in a sentence)
name="marquise"
color="grey"
restaurant="beau thai"

about_me=f"My name is {name}, my favourite color is {color} and my favourite place is {restaurant}."
print(about_me)

# Challenge: Excuse Generator

# Don't feel like going out tonight? Write a program that generates excuses for why you have to stay in.

# 1. Define these variables: first_name, event, number, noun, and verb. Use whatever values you want, as long as they match the format. 
# 2. Write an f-string using your variables that generates a one-sentence excuse. Here's an example of what your output should look like: 
#    "Sorry [Ted], I can't go to [the movies] — I have [345] [bees] to [crochet] and honestly it's taking longer than expected."
# 3. Print it! Change some or all of the values to create a new excuse. Print again. 

first_name="Ange"
event="bonjour"
number=5
noun="boy"
verb="walk"

event_night=f"Sorry {first_name}, I can't go to {event} — I have {number} {noun} to {verb} and honestly it's taking longer than expected."

print(event_night)