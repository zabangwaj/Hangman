import random

print ('''
 /$$   /$$
| $$  | $$
| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$
| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                               /$$  \ $$
                              |  $$$$$$/
                               \______/
'''
    )

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ('abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjackflopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch  stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie').split()

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = list (random.choice (word_list))

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

word_length = len(chosen_word) #the lenght of the chosen word.

the_blank = ["_"] * (word_length) #create as many blanks as there are letters

print (' '.join(the_blank)) #print out the blanks so the player knows how many letters are in a word

#print (chosen_word) #shows which word has been chosen

end_of_game = False
lives = 0

while not end_of_game:
    print (stages[lives]) #draw hangman
    guess = input ("Guess a letter: ").lower()  #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    if guess in the_blank:
        print (f"You've already guessed {guess}")

    for position in range (word_length):
        if (guess == chosen_word[position]):
            the_blank[position] = guess
    if guess not in chosen_word: #if guessed character is not in the chosen word array
        print (f"You guessed {guess}, that's not in the word.")
        print ("You lost a life!")
        lives += 1
    print (' '.join(the_blank))

    if "_" not in the_blank: #if there are no more blanks
        end_of_game = True
        print ("You WIN!")
    if lives == 6:
        print ("Game Over!")
        print (stages[lives]) #draw hangman
        print (f"The word was {''.join(chosen_word)}!")
        end_of_game = True
