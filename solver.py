import random

wordlist = []
letterlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # List of possible letters in the word
correct_letters = '' # Letters that are confirmed to be in the word based on yellow letters
correct_word = ['','','','',''] # Word that it must be based on position of green letters
incorrect_word = ['','','','',''] # Word that it cannot be based on position of yellow letters
guess = 'SOARE' # Initial guess

with open('wordlist.txt', 'r') as list: # Import word list
    for line in list.readlines():
        wordlist.append(line[:5])

possible_words = wordlist[:] # Make duplicate of word list

print('Welcome to the Wordle Solver!')
print(f'\nStart out with the guess {guess}')
print('After making this guess, for each letter type in 1 for letter not in word (black), 2 for letter in word (yellow), and 3 for letter in correct position (green)')

while '' in correct_word: # Keep looping until the word has been solved
    print(f'\n{len(possible_words)} possible words. {1 / len(possible_words) * 100}% chance of this guess being correct.')
    print(guess)
    accuracy = input('')

    for i,letter in enumerate(accuracy): # Record the results of the guess
        if letter == '1': # If the letter is not in the word, remove it from possible letters
            if (guess[i] not in correct_letters) and (guess[i] in letterlist):
                letterlist.remove(guess[i])
            incorrect_word[i] = ''
        if letter == '2': # If letter is in the word but not the correct position, add it to correct letters and incorrect word
            if guess[i] not in correct_letters:
                correct_letters += guess[i]
            incorrect_word[i] = guess[i]
        if letter == '3': # if letter is in the word and the correct position, add it to correct word
            if guess[i] not in correct_letters:
                correct_letters += guess[i]
            incorrect_word[i] = ''
            correct_word[i] = guess[i]

    possible_words = wordlist[:] # Copy list value by value instead of by reference

    for letter in correct_letters: # Filter all words that do not contain all letters in correct_letters
        letter = letter.lower()
        wordlist = possible_words[:]
        for item in wordlist:
            if letter not in item:
                possible_words.remove(item)

    wordlist = possible_words[:]
    for word in wordlist: # Filter all words that have letters not in the letter list/appeared as black
        for letter in word:
            letter = letter.upper()
            if letter not in letterlist:
                possible_words.remove(word)
                break

    for i,letter in enumerate(correct_word): # Filter all words that do not match correct_word/green tiles
        if letter == '':
            continue
        wordlist = possible_words[:]
        for word in wordlist:
            letter = letter.lower()
            if word[i] != letter:
                possible_words.remove(word)

    for i,letter in enumerate(incorrect_word): # Filter all words that match incorrect_word/have letters that have been tried in a position that had a yellow tile
        if letter == '':
            continue
        wordlist = possible_words[:]
        for word in wordlist:
            letter = letter.lower()
            if word[i] == letter:
                possible_words.remove(word)
            
    wordlist = possible_words[:]

    guess = possible_words[random.randint(0, len(possible_words) - 1)].upper() # Choose the next guess randomly from the remaining list of possible words
    
print('\nCongratulations!')