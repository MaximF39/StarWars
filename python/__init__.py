triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]
v1 = "wha" + "tis" + "up"
v2 = "wh" + "at" + "is" + "up"
"wh" "ha" "at" "ti" "is" "su" "up"
res = "whatisup"


def recoverSecret(triplets):
    frozenset_symbols = frozenset(symbol for triplet in triplets for symbol in triplet)
    for triplet in triplets:
        word = triplet[0] + triplet[1]
        word = find_symbols(word, frozenset_symbols)

def find_symbols(word, frozenset_symbols):
    for symbol in __find_symbol(word[-1]):
        word += symbol
        print(word)
        find_symbols(word)
        if frozenset_symbols == frozenset(word):
            return word

def __find_symbol(word_symbol):
    for triplet in triplets:
        for index, symbol in enumerate(triplet):
            if word_symbol == symbol and index != 2:
                yield triplet[index + 1]

if __name__ == '__main__':
    print(recoverSecret(triplets))

