# EX4 Instructions
# Recap – What is a float? What is the difference between an integer and a float?
print('Integers are whole numbers (including negative) and float are decimal numbers (also including negative)')

# Create a list containing the following sequence [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5] (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

sequence = []
for i in range(1,6):
    decimal = i + 0.5
    sequence.append(i)
    sequence.append(decimal)   

print(sequence[1:-1])
print(type(sequence[0]))
print(type(sequence[1]))


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# ages = input('enter the ages of your family members, separated by space').split()
# total_cost = 0

# for each_age in ages:
#     if each_age < 3:
#         total_cost += 0
#     elif each_age <= 12:
#         total_cost += 10
#     elif each_age > 12:
#         total_cost += 15
#     else:
#         print('invalid input, try again')

# print(total_cost)


family_size = int(input('how many ppl will watch the movie?'))

total_cost2 = 0
i = 1
while i <= family_size:
    age = int(input('How old is the member?'))
    if age < 3:
        total_cost2 += 0
    elif age <= 12:
        total_cost2 += 10
    elif age > 12:
        total_cost2 += 15
    i +=1
else: 
    print('we got all info we needed')
    

print(total_cost2)






# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.