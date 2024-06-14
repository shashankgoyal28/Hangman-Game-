import random
import hangman_stages
word_list = ["apple", "beautiful", "potato"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
# for letter in chosen_word:
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
lives = 6
while not game_over:
    guessed_letter = input("guess a letter: ").lower()
    # for letter in chosen_word:
    for position in range(len(chosen_word)):  # 0 1 2 3 4
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    # print("Match")
    # we cannot use this else here
    # else:
    #     print("No Match")
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose!")
    if '_' not in display:
        game_over = True
        print("you won!")
    print(hangman_stages.stages[lives])
