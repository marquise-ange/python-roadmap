#from the example_output.md
# Challenge: Create the output display for the PayUp app.

# 1. Check out the example output in `example_output.md`
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now —
#    we'll do the math later!
# 3. Build the display line by line using print() and f-strings. 
#    Remember: an empty print() creates a blank line.
# 4. Run it and make sure it matches the example.

#answer:
event_name="Fantastic Pizza"
Cost= 300
Service_charges= 30
Group_size= 3
Grand_total= 330
Each_person_must_PayUp= 110

print()
print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for dinner at {event_name}:")
print(f"cost: ${Cost}")
print(f"Service charges: ${Service_charges}")
print(f"Group size: {Group_size}")
print(f"Grand total: ${Grand_total}")
print()
print(f"Each person must Payup: ${Each_person_must_PayUp}")
