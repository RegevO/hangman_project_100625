import random



list_of_words = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic"
]

def choose_a_random_word(word_list: list):
    len_of_list = len(word_list)
    random_index = random.randint(a=0, b=len_of_list - 1)
    return word_list[random_index]


def print_hidden_word(word):
    word_len = len(word)
    print('_ ' * word_len)


if __name__ == '__main__':
    print("Welcome to Hangman game!!")
    word = choose_a_random_word(list_of_words)
    print(word)
    print_hidden_word(word)


