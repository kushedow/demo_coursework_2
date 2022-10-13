class Player:

    def __init__(self, name=""):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f"""Player({self.name}, {self.used_words})"""


    def is_word_used(self, word):
        """
        проверка использования данного слова до этого
        :param word: слвоо
        :return: было ли использовано
        """
        return word.lower() in self.used_words

    def add_word(self, word):
        """
        Добавление слова в использованные слова (ничего не возвращает);
        :param word: новое слово
        """
        self.used_words.append(word)

    def get_name(self):
        return self.name

    def count_used_words(self):
        """
        Получение количества использованных слов (возвращает int);
        :return: количество слов
        """
        return len(self.used_words)


