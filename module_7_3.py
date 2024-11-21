class WordsFinder:
    def __init__(self, *file_names:str):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                content = file.read()
                content = content.lower()
                for char in punctuation:
                    if char in content:
                        content = content.replace(char, '')
            all_words[i] = content.split()
        return all_words

    def find(self, word:str):
        all_words = self.get_all_words()
        finders = {}
        word = word.lower()
        for key in all_words.keys():
            counter = 0
            for value in all_words[key]:
                counter += 1
                if value == word:
                    finders[key] = counter
                    break
        return finders

    def count(self, word:str):
        all_words = self.get_all_words()
        word = word.lower()
        searched = {}
        counter = 0
        for key in all_words.keys():
            for value in all_words[key]:
                if value == word:
                    counter +=1
            searched[key] = counter
        return searched


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего