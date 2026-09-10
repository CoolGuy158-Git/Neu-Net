import random
import string

# Return a 6-letter word and its reverse

def gen_train(amount):
    words = []
    for i in range(amount):
        word = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

        reversed_word = ''.join(reversed(word))

        pair = f"{word} : {reversed_word}"
        words.append(pair)
    return words

