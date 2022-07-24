class Vigenere:
    def __init__(self, key):
        self.key = key
        self.make_grid()
        self.print_grid()

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

    def print_grid(self):
        for line in self.grid:
            print(line)

    def swap(self, a, b):
        (r1, c1) = self.coords[a]
        (r2, c2) = self.coords[b]
        if r1 == r2:
            return self.grid[r1][(c1+1)%5] + self.grid[r2][(c2+1)%5]
        elif c1 == c2:
            return self.grid[(r1+1)%5][c1] + self.grid[(r2+1)%5][c2]
        else:
            return self.grid[r1][c2] + self.grid[r2][c1]

    def unswap(self, a, b):
        return ''

    def encrypt(self, plaintext):
        ciphertext = ''
        for i in range(0, len(plaintext), 2):
            (r1, c1) = self.coords[plaintext[i]]
            (r2, c2) = self.coords[plaintext[i+1]]
            if r1 == r2:
                ciphertext += self.grid[r1][(c1+1)%5] + self.grid[r2][(c2+1)%5]
            elif c1 == c2:
                ciphertext += self.grid[(r1+1)%5][c1] + self.grid[(r2+1)%5][c2]
            else:
                ciphertext += self.grid[r1][c2] + self.grid[r2][c1]
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ''
        for i in range(0, len(ciphertext), 2):
            (r1, c1) = self.coords[ciphertext[i]]
            (r2, c2) = self.coords[ciphertext[i+1]]
            if r1 == r2:
                plaintext += self.grid[r1][(c1-1)%5] + self.grid[r2][(c2-1)%5]
            elif c1 == c2:
                plaintext += self.grid[(r1-1)%5][c1] + self.grid[(r2-1)%5][c2]
            else:
                plaintext += self.grid[r1][c2] + self.grid[r2][c1]
        return plaintext


def main():
    keyword = 'VIOLET'
    vig = Vigenere(keyword)
    plaintext = 'MAVERICK'
    ciphertext = vig.encrypt(plaintext)
    print(keyword, plaintext, ciphertext)
    plaintext = 'GDIVPLKR'
    ciphertext = vig.decrypt(plaintext)
    print(keyword, plaintext, ciphertext)



if __name__ == '__main__':
    main()
