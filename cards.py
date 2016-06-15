numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = [
    ('Clubs', 'black'),
    ('Diamonds', 'red'),
    ('Hearts', 'red'),
    ('Spades', 'black')]

for n in numbers:
    for (s, c) in suits:
        print "%s,%s,%s" % (s, n, c)

# print "Joker,Joker,red"
# print "Joker,Joker,black"
