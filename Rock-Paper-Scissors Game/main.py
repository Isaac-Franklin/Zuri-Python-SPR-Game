import random
availableOption = ['R', 'S', 'P']

print('\nKindly Pick An Option From Any Of These: \n')
print('R for Rock, \n')
print('S for Scissors Or, \n')
print('P for Paper. \n')

selectedOption = input()

# while true:
#     selectedOption == availableOption

# while selectedOption not in availableOption:
#     print('\nKindly Select An Option From The Given Range!')
#     selectedOption = print('INVALID!')

print('\nYou Just Selected '+selectedOption)
if (selectedOption == availableOption):
    print('\nYou Just Selected: '+selectedOption)

elif(selectedOption != availableOption):
    print('\nKindly Select An Option From The Given Range!')
    # selectedOption = print(' The Option You Entered Is INVALID!')


# for item in availableOption:
#     if (selectedOption == item):
# SYSTEM SELECT OPTION
    systemSelected = random.choice(availableOption)
    print('\nSystem Has Selected: ' + systemSelected)

# elif(selectedOption != item):
#     print('Kindly Select An Option From The Given Range!')


print('\nA ratio of our selection to the system\'s selection is given below:')

print('\nPlayer Score ' + selectedOption +
      ':' + systemSelected + ' System Score')


# PLAYER WINS
if selectedOption == 'R':
    if systemSelected == 'S':
        print('Player Wins!')
elif selectedOption == 'P':
    if systemSelected == 'R':
        print('Player Wins!')
elif selectedOption == 'S':
    if systemSelected == 'P':
        print('Player Wins!')

        # START PLAYER LOOSES

if selectedOption == 'S' and systemSelected == 'R' or selectedOption == 'P' and systemSelected == 'R' or selectedOption == 'S' and systemSelected == 'P':
    # if systemSelected == 'R':
    print('Player loose!')
# elif selectedOption == 'P' and systemSelected == 'R':
#     # if systemSelected == 'R':
#     print('Player Wins!')
# elif selectedOption == 'S' and systemSelected == 'P':
#     # if systemSelected == 'P':
#     print('Player Wins!')

    # END PLAYER LOOSES

    # SYSTEM WINS
elif systemSelected == 'P' and selectedOption == 'R' or systemSelected == 'S' and selectedOption == 'P' or systemSelected == 'R' and selectedOption == 'S':
    # if selectedOption == 'R':
    print('System Wins!')
# elif systemSelected == 'S' and selectedOption == 'P':
#     # if selectedOption == 'P':
#     print('System Wins!')
# elif systemSelected == 'R' and selectedOption == 'S':
#     # if selectedOption == 'S':
#     print('System Wins!')

elif systemSelected == selectedOption:
    # if selectedOption == 'S':
    print('TIE!')
