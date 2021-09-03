import random
from functools import reduce

def get_words_from_file():
  words = []
  with open("./data.txt", "r", encoding="utf-8") as f:
    for line in f:
      words.append(line.strip("\n"))
  return words

def replace_accent_mark_letters(word):
  replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
  for replacement in replacements:
    word = str(word).replace(replacement[0], replacement[1])
  return word

def get_random_word():
  words = get_words_from_file()
  return replace_accent_mark_letters(random.choice(words))

def run():
  won = False
  word_to_guess = str(get_random_word()).upper()
  guessed_word = ["_" for i in range(0, len(word_to_guess))]
  while reduce(lambda a, b: a + b, guessed_word) != word_to_guess:
    print("¡Adivina la palabra!")
    for letter_in_guessed_word in guessed_word:
      print(letter_in_guessed_word, end=" ")
    letter = input("\n\nIngresa una letra: ").upper()
    if letter in word_to_guess:
      for i in range(0, len(word_to_guess)):
        if letter == word_to_guess[i]:
          guessed_word[i] = letter
    if reduce(lambda a, b: a + b, guessed_word) == word_to_guess:
      won = True

  if won:
    print("¡Ganaste! La palabra era " + word_to_guess)
    
if __name__ == "__main__":
  run()
