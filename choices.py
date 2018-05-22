import string

class Option(object):
    def uppercase(self):
        chars = string.ascii_uppercase
        return chars

    def lowercase(self):
        chars = string.ascii_lowercase
        return chars

    def digits(self):
        chars = string.digits
        return chars

    def punctuation(self):
        chars = string.punctuation
        return chars

    def comb1(self):
        chars = self.uppercase() + self.lowercase()
        return chars

    def comb2(self):
        chars = self.uppercase() + self.digits()
        return chars

    def comb3(self):
        chars = self.uppercase() + self.punctuation()
        return chars

    def comb4(self):
        chars = self.lowercase() + self.digits()
        return chars

    def comb5(self):
        chars = self.lowercase() + self.punctuation()
        return chars

    def comb6(self):
        chars = self.digits() + self.punctuation()
        return chars

    def comb7(self):
        chars = self.uppercase() + self.lowercase() + self.digits()
        return chars

    def comb8(self):
        chars = self.lowercase() + self.digits() + self.punctuation()
        return chars

    def comb9(self):
        chars = self.uppercase() + self.digits() + self.punctuation()
        return chars

    def comb10(self):
        chars = self.uppercase() + self.lowercase() + self.punctuation()
        return chars

    def comb11(self):
        chars = self.uppercase() + self.lowercase() + self.digits() + self.punctuation()
        return chars