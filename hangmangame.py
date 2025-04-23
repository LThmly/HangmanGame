import random
import os

os.system('cls')

def hangman_draw(ver):
    match ver:
        case 0:
            hangman = '\n _______\n |     |\n |     |\n |      \n |     \n |     \n |      \n___     '
        case 1:
            hangman = '\n _______\n |     |\n |     |\n |     O \n |     \n |     \n |      \n___     '
        case 2:
            hangman = '\n _______\n |     |\n |     |\n |     O \n |     | \n |     \n |      \n___   '
        case 3:
            hangman = '\n _______\n |     |\n |     |\n |     O \n |    /| \n |     \n |      \n___     '
        case 4:
            hangman = '\n _______\n |     |\n |     |\n |     O \n |    /|\ \n |     \n |      \n___     '
        case 5:
            hangman = '\n _______\n |     |\n |     |\n |     O \n |    /|\ \n |    /  \n |      \n___     '
        case 6:
            hangman = '\n _______\n |     |\n |     |\n |     O \n |    /|\ \n |    / \ \n |      \n___     '
    print(hangman)

phraselist = 'phrases.txt'

#opens text file of 100 phrases and picks a random one
with open(phraselist, 'r') as file:
    phrases = file.readlines()
    phrase = random.choice(phrases).strip().lower()

#print(phrase)
#sets up the visual word and letter underlines
layout = []
visual = []
num_letters = 0
for character in phrase:
    if character.isspace() == True:
        print('  ', end = '')
        visual.append('  ')
    elif character.isalnum():
        print('_ ', end = '')
        visual.append('_ ')
        num_letters += 1
    else:
        print(character + ' ', end = '')
        visual.append(character + ' ')
    layout.append(character)

#creates variables for letters solved, errors, and instances of letters
solved = 0
errors = 0
instances = 0
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

#main game loop that runs until either the player recieves a win or loss
while solved != num_letters:
    hangman_draw(errors)
    print('\n' + letters)
    current_letter = input('\nEnter a letter: ')
    
    os.system('cls')
    
    if current_letter.isalnum():
        if current_letter in letters:
            letters = letters.replace(current_letter, '~')
            for i in range(len(layout)):
                if layout[i] == current_letter:
                    visual[i] = current_letter + ' '
                    solved += 1
                    instances += 1
            if instances == 0:
                errors += 1
                if errors == 6:
                    break
        instances = 0
            
    for i in range(len(visual)):
        print(visual[i], end = '')    

#tells the player if they won or lost
os.system('cls')
for i in range(len(visual)):
        print(visual[i], end = '')
hangman_draw(errors)
print('\n' + letters)
if errors != 6:
    print('\n\nYou win!')
else:
    print(f"\n\nYou lose!\nThe correct phrase was {phrase}")
