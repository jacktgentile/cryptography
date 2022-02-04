class Vigenere:
    def __init__(self, key):
        self.key = key
        self.make_grid()

    def make_grid(self):
        pass

    def swap(self, a, b):
        return ''

    def encrypt(self, plaintext):
        ciphertext = ''
        for i in range(0, len(plaintext), 2):
            a = plaintext[i]
            b = plaintext[i+1]
            ciphertext += self.swap(a, b)
        return ciphertext


def main():
    keyword = 'violet'
    vig = Vigenere(keyword)
    ciphertext = vig.encrypt('maverick')
    print(ciphertext)


if __name__ == '__main__':
    main()
