from operator import itemgetter


# IO routine

dic = dict([(str(i), i) for i in xrange(2, 10)])
dic['T'] = 10
dic['J'] = 11
dic['Q'] = 12
dic['K'] = 13
dic['A'] = 14


def parse():
    f = open('54.txt')
    for line in f:
        cards = line.split()
        yield cards


class Game:
    def __init__(self, cards):
        self.hand1 = Hand(cards[0:5])
        self.hand2 = Hand(cards[5:10])

    def winner(self):
        p1 = self.best_hand(self.hand1.cards)
        p2 = self.best_hand(self.hand2.cards)
        if p1[0] == p2[0]:
            if p1[1] > p2[1]:
                return 1
            else:
                return 2
        else:
            if p1[0] < p2[0]:
                return 1
            else:
                return 2

    def best_hand(self, cards):
        vals = []
        vals.append(self.royal_flush(cards))
        vals.append(self.straight_flush(cards))
        vals.append(self.four_of_a_kind(cards))
        vals.append(self.full_house(cards))
        vals.append(self.flush(cards))
        vals.append(self.straight(cards))
        vals.append(self.three_of_a_kind(cards))
        vals.append(self.two_pairs(cards))
        vals.append(self.high_card(cards))
        for val in vals:
            if val[0] != 1000:
                return val

    def get_high_card(self, cards):
        return cards[-1][0]

    def check_sequence(self, cards):
        for i in xrange(0, len(cards)-1):
            if cards[i][0]+1 != cards[i+1][0]:
                return False
        return True

    def check_flush(self, cards):
        for i in xrange(0, len(cards)-1):
            if cards[i][1] != cards[i+1][1]:
                return False
        return True

    def check_royal(self, cards):
        royal = [10, 11, 12, 13, 14]
        card_vals = [cards[i][0] for i in xrange(len(cards))]
        return royal == card_vals

    def royal_flush(self, cards):
        if self.check_sequence(cards) and self.check_flush(cards) and \
            self.check_royal(cards):
            return 0, self.get_high_card(cards)
        return 1000, 0

    def straight_flush(self, cards):
        if self.check_sequence(cards) and self.check_flush(cards):
            return 1, self.get_high_card(cards)
        return 1000, 0

    def four_of_a_kind(self, cards):
        arr = [0 for i in xrange(0, 15)]
        for card in cards:
            arr[card[0]] += 1
        for idx, count in enumerate(arr):
            if count == 4:
                return 2, idx
        return 1000, 0

    def full_house(self, cards):
        arr = [0 for i in xrange(0, 15)]
        for card in cards:
            arr[card[0]] += 1
        if 2 in arr and 3 in arr:
            for idx, count in enumerate(arr):
                if count == 3:
                    return 3, idx
        return 1000, 0

    def flush(self, cards):
        if self.check_flush(cards):
            return 4, self.get_high_card(cards)
        return 1000, 0

    def straight(self, cards):
        if self.check_sequence(cards):
            return 5, self.get_high_card(cards)
        return 1000, 0

    def three_of_a_kind(self, cards):
        arr = [0 for i in xrange(0, 15)]
        for card in cards:
            arr[card[0]] += 1
        if 2 not in arr and 3 in arr:
            for idx, count in enumerate(arr):
                if count == 3:
                    return 6, idx
        return 1000, 0

    def two_pairs(self, cards):
        arr = [0 for i in xrange(0, 15)]
        for card in cards:
            arr[card[0]] += 1
        high_card = -100
        pairs = 0
        for idx, count in enumerate(arr):
            if count == 2:
                pairs += 1
                if idx > high_card:
                    high_card = idx
        if pairs == 2:
            return 7, high_card
        elif pairs == 1:
            return 8, high_card
        return 1000, 0

    def high_card(self, cards):
        return 9, self.get_high_card(cards)

class Hand:
    def __init__(self, cards):
        self.process(cards)

    def process(self, cards):
        out = []
        for card in cards:
            out.append([dic[card[0]], card[1]])
        out = sorted(out, key=itemgetter(0))
        self.cards = out

def check_sequence(cards):
    for i in xrange(0, len(cards)-1):
        if cards[i]+1 != cards[i+1]:
            return False
    return True

one = 0
two = 0
parse_obj = parse()
while True:
    try:
        g = Game(parse_obj.next())
        win = g.winner()
        if win == 1:
            one += 1
        else:
            two += 1
    except:
        break

print one, two

