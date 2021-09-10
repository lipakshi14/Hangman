import random
guess_list=['banana','orange','bottle','choice','python','select']


guessing_word=random.choice(guess_list).lower()
word_letters=len(guessing_word)

game_over=False
tries=6

from hangman_lives import game_name
print(game_name)



result=[]
for _ in range(word_letters):
    result+= '_'

while not game_over:
    user_guessing= input("Guess a letter: ")
    print(f'the letter you guessed is {user_guessing}')

    for i in range(word_letters):
        letter=guessing_word[i]
        if letter==user_guessing:
            result[i]=letter
        
    if user_guessing not in guessing_word:
        print(f'The letter {user_guessing} you select is wrong. you loose a try ')
        tries -= 1
        if tries==0:
            game_over=True
            print(f'You loose the game!!. better luck next time. word was {guessing_word}')
        
        print(f"{' '.join(result)}")
    if '_' not in result:
            game_over=True
            print("Congo You Win!!!")
        
    from hangman_lives import lives
    print(lives[tries])
