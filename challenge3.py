# Challenge: Gather Input from Users

# We need four things from the user:

# - The name of the event or occasion
# - The cost
# - The tip or service charge
# - How many people are splitting the bill

# 1. Replace the hardcoded values for event, cost, service_charge, and group_size with input() prompts.
# 2. Keep grand_total and total_per_person hardcoded for now. They won't be entered by the user.
# 3. Run the program and make sure your prompts are clear and the display looks right.

event = input("Enter the event name:")
cost = input("enter the cost:")
service_charge = input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%: ")
group_size =input("how many people are you with: ")
grand_total = input("Enter th amount number for the bill: ")
total_per_person = input("Enter the total for each member: ")


print()
print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for dinner at {event}:")
print(f"cost: ${Cost}")
print(f"Service charges: ${Service_charges}")
print(f"Group size: {Group_size}")
print(f"Grand total: ${Grand_total}")
print()
print(f"Each person must Payup: ${Each_person_must_PayUp}")
