class Vigenere:
    def __init__(self, key):
        self.key = key
        self.make_grid()

    def make_grid(self):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        my_alphabet = ''
        for c in self.key:
            if c not in my_alphabet:
                my_alphabet += c
        for c in alphabet:
            if c not in my_alphabet:
                my_alphabet += c
        self.grid = []
        for i in range(0,25,5):
            self.grid.append(my_alphabet[i:i+5])
        self.coords = {}
        for row in range(5):
            for col in range(5):
                self.coords[self.grid[row][col]] = (row, col)

    def swap(self, a, b):
        return ''

    def unswap(self, a, b):
        return ''

    def encrypt(self, plaintext):
        ciphertext = ''
        for i in range(0, len(plaintext), 2):
            a = plaintext[i]
            b = plaintext[i+1]
            ciphertext += self.swap(a, b)
        return ciphertext


def main():
    keyword = 'VIOLET'
    vig = Vigenere(keyword)
    ciphertext = vig.encrypt('MAVERICK')
    print(ciphertext)


if __name__ == '__main__':
    main()
