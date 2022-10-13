class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"""BasicWord({self.word}, {len(self.sub_words)})"""

    def has_sub_word(self, word):
        """
        Проверяет наличие слова word в списке подслов словва
        :param word: проверяемое слово
        :return: найдено ли слово.
        """
        return word in self.sub_words

    def count_sub_words(self):
        """
        Возврващает общее количество подслов
        :return: сколько подслов всего
        """
        return len(self.sub_words)

    def get_word(self):
        return self.word

