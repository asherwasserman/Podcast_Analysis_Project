import base64
class Processor:
    def __init__(self, text, dangerous_words):
        self.text = text.lower
        self.text_list = text.split()
        self.dangerous_words = dangerous_words

    @staticmethod
    def encryption_key_base64(encrypted_text):
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_list = decoded_string.split(",")
        return decoded_string


    def find_dangerous_words(self):
        dangerous_find = []
        text_list = self.text_list
        for dangerous in self.dangerous_words:
            for word in text_list:
                if dangerous == word:
                    dangerous_find.append(dangerous)
        return dangerous_find

    def find_expression(self, expressions_list):
        expressions_find = []
        for dangerous in expressions_list:
            for index, word in enumerate(self.text_list):
                if dangerous[0] == word:
                    try:
                        find = True
                        counter = 0
                        for dangerous_word in dangerous:
                            if dangerous_word != self.text_list[index + counter]:
                                find = False
                                break
                            else:
                                counter += 1
                                continue
                        if find:
                            expressions_find.append(dangerous)
                    except:
                        continue
        return expressions_find

    def get_word_pairs(self):
        word_pairs = []
        for word in self.dangerous_words:
            if len(word.split()) > 1:
                word_pairs.append(word.split())
        return word_pairs


expression = [["a", "b"], ["d", "shjgfh"], ["sh", "d"], ]
text ="a b lhjk jf sh d"
dan = ["w", "a", "s b f"]

a = Processor(text, dan)
print(a.get_word_pairs())






