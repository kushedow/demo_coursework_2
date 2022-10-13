from utils import load_random_word
from player import Player

DATA_SOURCE = "https://api.npoint.io/d770aef14b139c431879"

print("Введите имя игрока")
user_name = input()

player = Player(user_name)
print(f"Привет, {player.get_name()}")

basic_word = load_random_word(DATA_SOURCE)

print(f"""Составьте {basic_word.count_sub_words()} слов из слова {basic_word.get_word()}""")
print("Слова должны быть не короче 3 букв")

while player.count_used_words() < basic_word.count_sub_words():

    user_input = input().strip().lower()

    if user_input in ["stop", "стоп", "хватит"]:
        break

    elif len(user_input) < 3:
        print("короткое слово")

    elif not basic_word.has_sub_word(user_input):
        print("Нет такого слова")

    elif player.is_word_used(user_input):
        print("Слово уже использовано")

    else:
        print("Верно")
        player.add_word(user_input)

print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
